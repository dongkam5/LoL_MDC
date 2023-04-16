from django.db import models

class Riot(models.Model):   
    api_key = models.CharField(max_length=50,null=True)
    def __str__(self) -> str:
        return self.api_key
    