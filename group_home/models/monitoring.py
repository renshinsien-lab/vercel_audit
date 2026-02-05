from django.db import models
# ディレクトリ構成に基づき、同じフォルダ内のファイルを相対インポート
from .base import TimeStampedModel  # base.py で定義されている名前を確認してください
from .plan_detail import SupportPlanRevision  # plan_detail.py にあるクラス名

class Monitoring(TimeStampedModel):
    """
    モニタリング評価モデル
    監査対策として、評価時点の目標内容をスナップショットとして保持できるようにします。
    """
    ACHIEVEMENT_CHOICES = [
        ('A', '達成（継続）'),
        ('B', '一部達成（内容変更）'),
        ('C', '未達成（計画見直し）'),
        ('D', '目標消滅'),
    ]

    # ForeignKey
    support_plan_revision = models.ForeignKey(
        SupportPlanRevision, 
        on_delete=models.CASCADE,  # 監査用として履歴を残すならPROTECTも検討
        related_name='monitorings',
        verbose_name='対象計画リビジョン'
    )
    
    # 既存のDB構造(target_goal_no)に合わせる
    target_goal_no = models.PositiveIntegerField(
        verbose_name='対象目標番号'
    )
    
    monitoring_date = models.DateField(
        verbose_name='モニタリング実施日'
    )

    # --- CSVからのインポートデータ保持用 (監査証跡) ---
    # 計画が変わっても評価の根拠が残るようにスナップショットを保持
    long_term_goal_snapshot = models.TextField(
        verbose_name='当時の長期目標', 
        blank=True, 
        null=True
    )
    short_term_goal_snapshot = models.TextField(
        verbose_name='当時の短期目標', 
        blank=True, 
        null=True
    )

    achievement_status = models.CharField(
        max_length=1, 
        choices=ACHIEVEMENT_CHOICES, 
        verbose_name='進捗評価'
    )
    
    # CSVの「モニタリング結果」やAI整形文を保存
    comment = models.TextField(
        verbose_name='評価コメント・特記事項'
    )

    class Meta:
        db_table = 'monitoring'  # 既存テーブルに合わせる
        verbose_name = 'モニタリング'
        verbose_name_plural = 'モニタリング'
        # ordering = ['-monitoring_date'] # 必要に応じて追加

    def __str__(self):
        return f"{self.monitoring_date} - 目標{self.target_goal_no}"