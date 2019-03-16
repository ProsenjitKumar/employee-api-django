from django.db import models


class Employeer(models.Model):
    name = models.CharField(max_length=55)
    log_date = models.DateField(blank=True, null=True)
    log_time = models.TimeField(auto_now=False, null=True, blank=True)
    login = models.TimeField(auto_now=False, null=True, blank=True)
    logout = models.TimeField(auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.name

