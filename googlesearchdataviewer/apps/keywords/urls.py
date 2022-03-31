from django.urls import path

from . import views


urlpatterns = [
    path('', views.KeywordListView.as_view(), name='keyword-list'),
    path('<int:id>', views.KeywordDetailView.as_view(), name='keyword-detail'),
    path('upload', views.keyword_file_upload, name='keyword-file-upload'),
]