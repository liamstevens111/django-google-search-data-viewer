from django.views.generic import ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from googlesearchdataviewer.apps.keywords.utils import parse_keyword_csv_file

from .models import KeywordResult, KeywordUpload, KeywordUploadProfile
from .forms import UploadCsvKeywordsForm

from django.contrib import messages

from .services import begin_keyword_search

class HomeView(LoginRequiredMixin, ListView):
    model = KeywordUpload
    template_name = 'keywords/index.html'

    def get_queryset(self):
        return self.request.user.profile.uploads.all().order_by('-created_at')


class KeywordListView(LoginRequiredMixin, ListView):
    model = KeywordResult
    template_name = 'keywords/list.html'

    def get_queryset(self):
        keyword_qs = self.request.GET.get('keyword')

        keywords = self.request.user.profile.uploaded_keywords.distinct()

        if keyword_qs:
            keywords = keywords.filter(keyword__icontains=keyword_qs)

        return keywords


class KeywordDetailView(LoginRequiredMixin, DetailView):
    model = KeywordResult
    template_name = 'keywords/detail.html'

    def get_object(self, queryset=None):
        return KeywordResult.objects.get(id=self.kwargs['id'])

class KeywordFileUploadView(LoginRequiredMixin, FormView):
    template_name = 'keywords/upload-keywords.html'
    form_class = UploadCsvKeywordsForm
    success_url = '/'
    
    def form_valid(self, form):
        keywords = parse_keyword_csv_file(self.request.FILES['file'])

        begin_keyword_search(profile=self.request.user.profile, keywords = keywords)

        messages.success(self.request, 'Keywords were sent, now in progress.')
        return super().form_valid(form)
            
