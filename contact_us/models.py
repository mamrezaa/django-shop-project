from django.db import models

# Create your models here.

class ContactUs(models.Model):
    fullName = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(max_length=100,null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta():
        verbose_name = 'ارتباط با'
        verbose_name_plural = 'ارتباط با ما'


    def __str__(self):
        return self.fullName