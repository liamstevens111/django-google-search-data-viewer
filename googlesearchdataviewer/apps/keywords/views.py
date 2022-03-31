from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import KeywordResult, KeywordUpload, KeywordUploadProfile
from .forms import UploadCsvKeywordsForm

from django.forms import ValidationError

from django.http import HttpResponseRedirect

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

        if keyword_qs:
            keywords = KeywordResult.objects.filter(keyword__icontains=keyword_qs)
        else:
            keywords = self.request.user.profile.uploaded_keywords.distinct()
        
        return keywords


class KeywordDetailView(LoginRequiredMixin, DetailView):
    model = KeywordResult
    template_name = 'keywords/detail.html'

    def get_object(self, queryset=None):
        return KeywordResult.objects.get(id=self.kwargs['id'])


def parse_keywords_from_csv(file):
    return file.read().decode('UTF-8').splitlines()


def validate_keywords(keywords):
    if len(keywords) == 0 or len(keywords) > 100:
        raise ValidationError('Too many keywords', code='invalid')


def keyword_file_upload(request):
    if request.method == 'POST':
        form = UploadCsvKeywordsForm(request.POST, request.FILES)
        if form.is_valid():
            keywords = parse_keywords_from_csv(request.FILES['file'])

            validate_keywords(keywords)

            # Create KeywordUpload to start process for user
            begin_keyword_search(profile=request.user.profile, keywords = keywords)

            # Return message to user it is in progress
            messages.success(request, 'Keywords were sent, now in progress.')

            return HttpResponseRedirect('/')
    else:
        form = UploadCsvKeywordsForm()
    return render(request, 'keywords/upload-keywords.html', {'form': form})
            
