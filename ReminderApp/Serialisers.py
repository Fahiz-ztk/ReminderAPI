from rest_framework import serializers
from .models import Reminder
class ReminderSrl(serializers.ModelSerializer):
    class Meta:
        model=Reminder
        fields="__all__"