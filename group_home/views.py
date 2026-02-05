# group_home/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Max, Min
from django.http import JsonResponse
from datetime import date

from .models import Resident, DailyRecord, DailyRecordItem
from .forms import ResidentForm, DailyRecordForm, DailyRecordItemForm

from google import genai

import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import traceback

# APIキーを設定（本来は環境変数にすべきですが、まずは直接記述でOKです）
# genai.configure(api_key="AIzaSyBC1SUDiSigHMIXQr-PZMg-GpJfg5adOc8")
client = genai.Client(api_key='AIzaSyBC1SUDiSigHMIXQr-PZMg-GpJfg5adOc8')

@csrf_exempt
def ai_format_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            raw_text = data.get('text', '')
            
            print(f"--- AI Formatting Start ---")
            print(f"Input: {raw_text}")

            # モデル名は 'gemini-1.5-flash' (models/ は不要) を指定
            # もしこれでダメなら 'gemini-2.0-flash-exp' など最新版を試すのも手です
            response = client.models.generate_content(
                model='gemini-2.0-flash',  # 1.5-flash で 404 が出るならここを 2.0 に変更
                contents=f"あなたはプロの介護士です。次の内容を適切な介護記録に整形して：\n{raw_text}"
            )

            if response.text:
                formatted_text = response.text.strip()
                print(f"Result: {formatted_text}")
                return JsonResponse({'formatted_text': formatted_text})
            else:
                return JsonResponse({'error': 'AIから空の応答が返りました'}, status=500)

        except Exception as e:
            print("--- AI ERROR START ---")
            traceback.print_exc()
            print("--- AI ERROR END ---")
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)

"""
@csrf_exempt
def ai_format_api(request):
    if request.method == 'POST':
        try:
            # モデル名の指定をより明示的なものに変更します
            # 'gemini-1.5-flash' -> 'models/gemini-1.5-flash'
            model = genai.GenerativeModel('models/gemini-2.5-flash')
            import traceback # 追加 debug
            data = json.loads(request.body)
            raw_text = data.get('text', '')
            print(f"--- AI Formatting Start ---") # デバッグ用
            print(f"Input: {raw_text}")            # デバッグ用

            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"あなたはプロの介護士です。次の内容を適切な介護記録に整形して：{raw_text}"

            model = genai.GenerativeModel('models/gemini-1.5-flash')
            
            # APIからの応答を確認
            if response.text:
                formatted_text = response.text.strip()
                print(f"Result: {formatted_text}") # デバッグ用
                return JsonResponse({'formatted_text': formatted_text})
            else:
                return JsonResponse({'error': 'AIから空の応答が返りました'}, status=500)

        except Exception as e:
            # ここが重要：エラーの内容をターミナルに強制的に表示します
            import traceback
            print("--- AI ERROR START ---")
            traceback.print_exc() 
            print("--- AI ERROR END ---")
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)
"""
# --- 1. 利用者一覧 ---
class ResidentListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        residents = Resident.objects.all().order_by('name')
        return render(request, 'group_home/resident_list.html', {'residents': residents})

# --- 2. 基本情報編集 ---
class ResidentUpdateView(LoginRequiredMixin, UpdateView):
    model = Resident
    form_class = ResidentForm
    template_name = 'group_home/resident_form.html'
    success_url = reverse_lazy('resident_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "利用者基本情報の編集"
        return context

# --- 3. 監査ログ（履歴） ---
def audit_log_view(request, resident_id):
    resident = get_object_or_404(Resident, pk=resident_id)
    records = DailyRecord.objects.filter(resident=resident).order_by('-record_date')
    return render(request, 'group_home/audit_log.html', {'resident': resident, 'records': records})

# --- 4. 日報・バイタル入力 ---
class DailyRecordCreateView(LoginRequiredMixin, View):
    def get(self, request, resident_id):
        resident = get_object_or_404(Resident, pk=resident_id)
        return render(request, 'group_home/record_form.html', {
            'form': DailyRecordForm(), 'item_form': DailyRecordItemForm(), 'resident': resident
        })

    def post(self, request, resident_id):
        resident = get_object_or_404(Resident, pk=resident_id)
        form = DailyRecordForm(request.POST)
        item_form = DailyRecordItemForm(request.POST)

        if form.is_valid() and item_form.is_valid():
            record = form.save(commit=False)
            record.resident = resident
            record.save()
            
            item = item_form.save(commit=False)
            item.daily_record = record
            item.save()
            return redirect('audit_log', resident_id=resident.id)
            
        return render(request, 'group_home/record_form.html', {
            'form': form, 'item_form': item_form, 'resident': resident
        })

# --- 5. モニタリング報告書（月次集計） ---
class MonitoringReportView(LoginRequiredMixin, DetailView):
    model = Resident
    template_name = 'group_home/monitoring_report.html'
    context_object_name = 'resident'
    pk_url_kwarg = 'resident_id'

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
                
        # 該当月の記録取得
        records = DailyRecord.objects.filter(
            resident=self.object,
            record_date__year=year,
            record_date__month=month
        ).prefetch_related('dailyrecorditem_set')

        # 該当月のバイタル集計
        vital_stats = DailyRecordItem.objects.filter(
            daily_record__resident=self.object,
            daily_record__record_date__year=year,
            daily_record__record_date__month=month
        ).aggregate(
            avg_temp=Avg('body_temperature'),
            max_bp_high=Max('blood_pressure_high'),
            min_bp_low=Min('blood_pressure_low'),
            avg_pulse=Avg('pulse')
        )

        context.update({
            'year': year, 'month': month, 'records': records,
            'stats': vital_stats, 'report_date': date.today(),
        })
        return context

# --- 6. API・その他 ---
def vital_graph_data(request, resident_id):
    data = {'labels': ['2/1', '2/2', '2/3'], 'temps': [36.2, 36.5, 36.4]}
    return JsonResponse(data)

def finalize_revision(request, revision_id):
    # 実装に合わせてモデルを調整してください
    return redirect('resident_list')