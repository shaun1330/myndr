from django.db import models
from croniter import croniter
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def validate_crontab(value):
    """Validate that the provided value is a valid crontab string."""
    if not croniter.is_valid(value):
        raise ValidationError(f"{value} is not a valid crontab expression")


class Tag(models.Model):
    name = models.CharField(max_length=100)
    hex_color = models.CharField(max_length=7, default='#2778a9')


class Category(models.Model):
    name = models.CharField(max_length=100)


class Task(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)


class TaskSchedule(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(null=True, blank=True)
    crontab =models.CharField(max_length=100, validators=[validate_crontab])


class TaskRecord(models.Model):
    """
    Occurrences of each task
    """
    statuses = [
        ("COMPLETED", "Completed"),
        ("FAILED", "Failed"),
        ("SKIPPED", "Skipped"),
        ("PENDING", "Pending"),
    ]

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    status = models.CharField(max_length=100, choices=statuses)
    notes = models.TextField(null=True, blank=True)




