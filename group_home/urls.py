# group_home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # --- 1. 利用者管理（一覧・基本情報） ---
    # 利用者一覧
    path('', views.ResidentListView.as_view(), name='resident_list'),
    path('residents/', views.ResidentListView.as_view(), name='resident_list_alt'),
    
    # 基本情報編集
    path('resident/<int:pk>/edit/', views.ResidentUpdateView.as_view(), name='resident_edit'),

    # --- 2. 記録・ログ入力 ---
    # 監査ログ（特定利用者の履歴一覧）
    path('<int:resident_id>/', views.audit_log_view, name='audit_log'),
    
    # 日報・バイタル入力（どちらのパスでもアクセス可能に設定）
    path('record/add/<int:resident_id>/', views.DailyRecordCreateView.as_view(), name='daily_record_add'),
    path('daily-record/<int:resident_id>/add/', views.DailyRecordCreateView.as_view(), name='daily_record_create'),

    # --- 3. 分析・報告・API ---
    # 月次モニタリング報告書（集計表示）
    path('monitoring/<int:resident_id>/<int:year>/<int:month>/', 
         views.MonitoringReportView.as_view(), 
         name='monitoring_report_view'),
    
    # グラフデータ取得用API
    path('api/vital-graph/<int:resident_id>/', views.vital_graph_data, name='vital_graph_data'),
    
    # 記録の確定（承認）
    path('finalize/<int:revision_id>/', views.finalize_revision, name='finalize_revision'),
    
    # Gemini回り
    path('ai-format-api/', views.ai_format_api, name='ai_format_api'),
]
