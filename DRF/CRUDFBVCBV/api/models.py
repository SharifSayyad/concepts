from django.db import models
from django.contrib.admin.models import LogEntry,LogEntryManager
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    city = models.CharField(max_length=30)
    created_by = models.CharField(max_length=250, blank=True, null=True)

    # def save(self):
    #     data = LogEntry.objects.select_related()
    #     print(data.__dict__)


import json
class mylog(models.Model):
    name = models.CharField(max_length=100)

    def log_action(self, user_id, content_type_id, object_id, object_repr, action_flag, change_message=''):
        if isinstance(change_message, list):
            change_message = json.dumps(change_message)
        return self.model.objects.create(
            user_id=user_id,
            content_type_id=content_type_id,
            object_id=str(object_id),
            object_repr=object_repr[:200],
            action_flag=action_flag,
            change_message=change_message,
        )
