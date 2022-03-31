from googlesearchdataviewer.apps.profiles.models import Profile
from .models import KeywordUpload, KeywordUploadProfile, KeywordResult


class MockGoogleKeywordSearchService():
    def search_keyword(self, keyword):
        return {
            'total_results': 5137355411,
            'total_links': 5,
            'total_adwords': 3,
            'html': f'<html> {keyword} </html>'
        }


def search_keywords_on_google(keywords, upload):
    google_service = MockGoogleKeywordSearchService()

    upload.status=KeywordUpload.INPROGRESS
    upload.save()

    for keyword in keywords:
        data = google_service.search_keyword(keyword)

        keyword_result, created = KeywordResult.objects.update_or_create(defaults={'keyword': keyword, **data}, keyword__iexact=keyword)

        KeywordUploadProfile.objects.create(profile=upload.uploader, keyword_result=keyword_result, upload=upload)

    upload.status=KeywordUpload.COMPLETED
    upload.save()


def begin_keyword_search(*, profile: Profile, keywords: list[str]):
    current_upload = KeywordUpload.objects.create(uploader=profile, status=KeywordUpload.AWAITING_PROCESSING)

    search_keywords_on_google(keywords, current_upload)