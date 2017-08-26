from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=100)
    tag_line = models.TextField()
    description = models.TextField()
    employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    company_pic = models.ImageField(upload_to='pic_folder/', default='/pic_folder/nologo.jpg')

    def __str__(self):
        return self.name


class Feedback(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)