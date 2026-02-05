# group_home/forms.py
from django import forms
from .models import Resident, DailyRecord, DailyRecordItem

class ResidentForm(forms.ModelForm):
    """利用者基本情報の編集用フォーム"""
    class Meta:
        model = Resident
        # master.pyのフィールド名と完全に一致させています
        fields = [
            'resident_code', 'name', 'birth_date', 
            'care_level', 'room_number', 'diagnosis', 
            'emergency_contact', 'notes'
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'diagnosis': forms.Textarea(attrs={'rows': 2, 'placeholder': '既往歴や持病'}),
            'emergency_contact': forms.Textarea(attrs={'rows': 2, 'placeholder': '家族名・電話番号'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': '特記事項'}),
        }
        labels = {
            'resident_code': '利用者コード',
            'name': '氏名',
            'birth_date': '生年月日',
            'care_level': '要介護度',
            'room_number': '居室番号',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Bootstrapのスタイルを一括適用
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class DailyRecordForm(forms.ModelForm):
    """日報基本情報のフォーム"""
    class Meta:
        model = DailyRecord
        fields = ['record_date', 'wakeup_time', 'sleep_time']
        widgets = {
            'record_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'wakeup_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'sleep_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

class DailyRecordItemForm(forms.ModelForm):
    """バイタル等詳細のフォーム"""
    class Meta:
        model = DailyRecordItem
        fields = [
            'target_goal_no', 'item_value', 'body_temperature', 
            'blood_pressure_high', 'blood_pressure_low', 'pulse'
        ]