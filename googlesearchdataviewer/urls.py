from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.views.generic import TemplateView

from googlesearchdataviewer.apps.keywords.views import HomeView



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('auth/', include('googlesearchdataviewer.apps.users.urls')),
    path('keywords/', include('googlesearchdataviewer.apps.keywords.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns