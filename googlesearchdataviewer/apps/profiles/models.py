from django.db import models
from googlesearchdataviewer.apps.common.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(
        'users.BaseUser', on_delete=models.CASCADE
    )

    uploaded_keywords = models.ManyToManyField('keywords.KeywordResult', through='keywords.KeywordUploadProfile', related_name='uploaded_by')

    def __str__(self):
        return self.user.email
