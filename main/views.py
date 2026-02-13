from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, DetailView

from main.forms import BookingForm
from main.models import Booking, Service, Specialist


# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'main/index.html'

class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "main/book.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        context["specialists"] = Specialist.objects.all()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        form.save_m2m()

        total_price = sum(
            service.price for service in self.object.services.all()
        )

        self.object.total_price = total_price
        self.object.save()
        self.object.send_booking_email()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("main:booking_success", kwargs={"pk": self.object.pk})


class StoryTemplateView(TemplateView):
    template_name = 'main/story.html'


class BookingSuccessView(DetailView):
    model = Booking
    template_name = "main/success.html"
    context_object_name = "booking"