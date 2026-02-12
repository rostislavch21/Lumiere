from django.core.mail import send_mail
from django.db import models

from Lumiere import settings


# Create your models here.
class Service(models.Model):
    service_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    service_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.service_name

class Specialist(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='specialists/', blank=True, null=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    services = models.ManyToManyField(Service)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    requests = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        services_list = ", ".join(
            service.service_name for service in self.services.all()
        )
        return f"{services_list} – {self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Bookings'

    def send_booking_email(self):
        services_list = ", ".join(
            service.service_name for service in self.services.all()
        )

        specialist_name = (
            self.specialist.name if self.specialist else "Any specialist"
        )

        formatted_date = self.booking_date.strftime("%B %d, %Y")
        formatted_time = self.booking_time.strftime("%H:%M")

        send_mail(
            subject=f"✨ Your Booking at Lumière is Confirmed",
            message=(
                f"Dear {self.first_name},\n\n"

                f"Thank you for booking with Lumière Beauty.\n\n"

                f"Here are your appointment details:\n"
                f"— Services: {services_list}\n"
                f"— Date: {formatted_date}\n"
                f"— Time: {formatted_time}\n"
                f"— Specialist: {specialist_name}\n"
                f"— Total: ${self.total_price}\n\n"

                f"If you need to reschedule or cancel, "
                f"please contact us at hello@lumiere.mail.\n\n"

                f"We look forward to welcoming you 🌿\n\n"

                f"Warm regards,\n"
                f"Lumière Beauty"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.email],
            fail_silently=False,
        )