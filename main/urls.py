from django.conf.urls.static import static
from django.urls import path

from Lumiere import settings
from main.views import IndexTemplateView, BookingCreateView, StoryTemplateView, BookingSuccessView

app_name = 'main'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('book/', BookingCreateView.as_view(), name='book'),
    path('story/', StoryTemplateView.as_view(), name='story'),
    path("booking-success/", BookingSuccessView.as_view(), name="booking_success"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)