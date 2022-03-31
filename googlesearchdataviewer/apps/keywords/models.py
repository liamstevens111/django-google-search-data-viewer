from calendar import c
from django.db import models
from googlesearchdataviewer.apps.common.models import BaseModel

from django.db.models.functions import Upper

from django.conf import settings


class KeywordUpload(BaseModel):
    AWAITING_PROCESSING = 0
    INPROGRESS = 1
    COMPLETED = 2

    STATUS_CHOICES = [
        (AWAITING_PROCESSING, 'Awaiting Processing'),
        (INPROGRESS, 'In-Progress'),
        (COMPLETED, 'Completed'),
    ]

    uploader = models.ForeignKey(
            'profiles.Profile', on_delete=models.CASCADE, related_name='uploads'
    )

    status = models.IntegerField(
            choices=STATUS_CHOICES,
            default=AWAITING_PROCESSING,
            verbose_name=('Status'),
            db_index=True,
    )

    def __str__(self):
            return f'{self.uploader} - {self.get_status_display()} - {self.created_at}'


class KeywordResult(BaseModel):
    keyword = models.CharField(max_length=255, unique=True)
    total_results = models.PositiveBigIntegerField()
    total_links = models.IntegerField()
    total_adwords = models.IntegerField()
    html = models.TextField()

    class Meta:
        constraints = [
        models.UniqueConstraint(
            Upper('keyword'), name='unique_upper_keyword_name')
        ]
  
    def __str__(self):
        return self.keyword


class KeywordUploadProfile(BaseModel):
    profile = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE)
    keyword_result = models.ForeignKey('keywords.KeywordResult', on_delete=models.CASCADE)
    upload = models.ForeignKey('keywords.KeywordUpload', on_delete=models.CASCADE)

    def __str__(self):
            return f'{self.profile} - {self.keyword_result}'
