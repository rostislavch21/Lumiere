from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from main.forms import BookingForm
from main.models import Booking, Service, Specialist


# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'main/index.html'

class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "main/book.html"
    success_url = reverse_lazy("main:booking_success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        context["specialists"] = Specialist.objects.all()
        return context

    def form_valid(self, form):
        booking = form.save(commit=False)
        booking.save()
        form.save_m2m()

        total_price = sum(
            service.price for service in booking.services.all()
        )

        booking.total_price = total_price
        booking.save()

        return super().form_valid(form)


class StoryTemplateView(TemplateView):
    template_name = 'main/story.html'

class BookingSuccessView(TemplateView):
    template_name = "main/success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["booking"] = Booking.objects.last()
        return context