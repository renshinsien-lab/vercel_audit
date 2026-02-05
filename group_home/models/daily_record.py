# group_home/models/daily_record.py
from django.db import models
from django.utils import timezone
from .base import TimeStampedModel
from .master import Resident, Office

class DailyRecord(TimeStampedModel):
    """日次記録の親モデル：誰が、いつ、どの事業所で記録されたか"""
    resident = models.ForeignKey(
        Resident,
        on_delete=models.PROTECT,
        verbose_name="利用者"
    )
    # Officeモデルとの連携も維持
    office = models.ForeignKey(
        Office,
        on_delete=models.PROTECT,
        verbose_name="事業所"
    )
    record_date = models.DateField(
        verbose_name="記録日"
    )
    
    # --- forms.py の FieldError を解消するために追加 ---
    wakeup_time = models.TimeField(null=True, blank=True, verbose_name='起床時刻')
    sleep_time = models.TimeField(null=True, blank=True, verbose_name='就寝時刻')

    class Meta:
        db_table = 'daily_record'
        # 同じ日に同じ利用者の記録が重複しないように制限
        unique_together = ('resident', 'record_date')
        verbose_name = '日次記録'
        verbose_name_plural = '7. サービス実施記録'

    def __str__(self):
        return f"{self.resident.name} ({self.record_date})"

class DailyRecordItem(TimeStampedModel):
    """実施詳細モデル：バイタルや具体的な活動内容"""
    daily_record = models.ForeignKey(
        DailyRecord, on_delete=models.CASCADE, related_name='items'
    )
    # 監査対応: どの目標に基づく支援か
    target_goal_no = models.PositiveIntegerField(
        verbose_name='対象目標番号', 
        help_text='計画書の「目標番号」を入力',
        null=True, blank=True
    )
    # 実施内容のテキスト
    item_value = models.TextField(verbose_name='実施内容・結果')

    # --- バイタル項目（forms.pyと完全に一致） ---
    body_temperature = models.DecimalField(
        max_digits=4, decimal_places=1, null=True, blank=True, verbose_name="体温"
    )
    blood_pressure_high = models.IntegerField(null=True, blank=True, verbose_name="血圧(高)")
    blood_pressure_low = models.IntegerField(null=True, blank=True, verbose_name="血圧(低)")
    pulse = models.IntegerField(null=True, blank=True, verbose_name="脈拍")

    class Meta:
        db_table = 'daily_record_item'
        verbose_name = '実施詳細'
        verbose_name_plural = '実施詳細'