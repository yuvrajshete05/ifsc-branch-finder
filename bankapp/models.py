from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Branch(models.Model):
    bank = models.ForeignKey(Bank, related_name='branches', on_delete=models.CASCADE)
    branch = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=20, unique=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.branch} ({self.ifsc})"

class Branch(models.Model):
    bank = models.ForeignKey(Bank, related_name='branches', on_delete=models.CASCADE)
    branch = models.CharField(max_length=100)  # use 'branch' here
    ifsc = models.CharField(max_length=20, unique=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.branch} ({self.ifsc})"

