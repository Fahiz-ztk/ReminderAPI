from django.contrib import admin
from django.urls import path
from ReminderApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addreminder/', SaveReminder.as_view())
]
