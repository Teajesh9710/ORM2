from django.db import models
from django.contrib import admin

class CARs(models.Model):
    SNO = models.CharField(max_length=255, help_text="Car_id")
    Brand = models.CharField(max_length=100, help_text="Brand Name")
    Model = models.CharField(help_text="Model Number")
    Year = models.CharField(max_length=50, help_text="Release Year")
    Rating = models.DecimalField(max_digits=3, decimal_places=1, help_text="Cae Rating (e.g., 8.5)")
    Color = models.CharField(help_text="Car Outer color")

class CARsAdmin(admin.ModelAdmin):
    list_display = ('SNO', 'Brand', 'Model', 'Year', 'Rating','Color')
