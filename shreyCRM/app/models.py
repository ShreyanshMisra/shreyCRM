from django.db import models


class Lead(models.Model):

    date = models.DateTimeField(auto_now_add=True)

    first = models.CharField(max_length=15)
    last = models.CharField(max_length=15)
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    linkedin = models.URLField(max_length=300)
    location = models.CharField(max_length=300)
    notes = models.CharField(max_length=1000)


    def __str__(self):
        return self.first + " " + self.last
    
    def save(self, *args, **kwargs):
        countLeads = Lead.objects.all().count()+1
        self.id = countLeads
        super(Lead, self).save(*args, **kwargs)
