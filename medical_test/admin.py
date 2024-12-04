from django.contrib import admin
from .models import   Medical


@admin.register(Medical)
class TestAdmin(admin.ModelAdmin):
    list_display = ( 'HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits')


