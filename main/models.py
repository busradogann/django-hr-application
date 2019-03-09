from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    number_of_people = models.PositiveIntegerField(default=1)
    last_application_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resumes')

    def __str__(self):
        return self.name

