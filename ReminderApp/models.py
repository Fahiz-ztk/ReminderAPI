from django.db import models


class Reminder(models.Model):
    Date = models.DateField()
    Time = models.TimeField()
    Message = models.CharField(max_length=200)
    options = [
        ( "Email" ,"Email"),
        ( "SMS" ,"SMS" )
    ]
    ReminderType = models.CharField(choices=options,max_length=20)