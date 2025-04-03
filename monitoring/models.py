from django.db import models

class SoilData(models.Model):
    pH = models.FloatField()
    moisture = models.FloatField()
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Soil Data - {self.timestamp}"
