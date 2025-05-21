from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Reminder
from .Serialisers import ReminderSrl

class SaveReminder(APIView):
    def post(self,request):
        data= ReminderSrl(data=request.data)
        if data.is_valid():
            data.save()
            return Response({"message": f"Created New Reminder For {data.validated_data['Message']} on {data.validated_data['Date']} at {data.validated_data['Time']}"}, status=status.HTTP_201_CREATED)
        else:
            return Response(data.errors,status=status.HTTP_400_BAD_REQUEST)
