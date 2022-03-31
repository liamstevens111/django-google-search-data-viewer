from django.contrib import admin
from .models import KeywordUpload, KeywordResult, KeywordUploadProfile

admin.site.register(KeywordUpload)
admin.site.register(KeywordResult)
admin.site.register(KeywordUploadProfile)
