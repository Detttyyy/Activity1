from django.contrib import admin
from .models import Post
from .models import User, Event, Facility, Booking, Feedback


admin.site.register(Post)
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Facility)
admin.site.register(Booking)
admin.site.register(Feedback)
