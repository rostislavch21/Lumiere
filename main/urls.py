from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from Lumiere import settings
from main.views import IndexTemplateView, BookingCreateView, StoryTemplateView, BookingSuccessView

app_name = 'main'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('book/', BookingCreateView.as_view(), name='book'),
    path('story/', StoryTemplateView.as_view(), name='story'),
    path(
        "booking/success/<int:pk>/",
        BookingSuccessView.as_view(),
        name="booking_success",
    ),
    path("privacy/", TemplateView.as_view(
        template_name="main/privacy.html"
    ), name="privacy"),

    path("terms/", TemplateView.as_view(
        template_name="main/terms.html"
    ), name="terms"),

    path("cookies/", TemplateView.as_view(
        template_name="main/cookies.html"
    ), name="cookies"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)