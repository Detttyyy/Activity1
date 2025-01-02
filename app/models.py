from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField() 


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organized_events")

    def __str__(self):
        return self.name


class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, null=True, blank=True)
    booking_date = models.DateField()
    booking_time = models.TimeField()

    def __str__(self):
        if self.event:
            return f"Booking for Event: {self.event.name} by {self.user}"
        return f"Booking for Facility: {self.facility.name} by {self.user}"


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.user} - Rating: {self.rating}"