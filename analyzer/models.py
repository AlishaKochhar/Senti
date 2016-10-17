from django.db import models

class EnterSenti(models.Model):
    sentiment=models.CharField(max_length=120,null=True,blank=True)

    def __str__(self) :
        return str(self.sentiment)
