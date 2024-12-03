from django.db import models
class Tests(models.Model):
    
    HighBP = models.BooleanField()
    HighChol = models.BooleanField()
    CholCheck = models.BooleanField()
    BMI = models.FloatField()
    Smoker = models.BooleanField()
    Stroke = models.BooleanField()
    HeartDiseaseorAttack = models.BooleanField()
    PhysActivity = models.BooleanField()
    Fruits = models.BooleanField()
    Veggies = models.BooleanField()
    HvyAlcoholConsump = models.BooleanField()
    AnyHealthcare = models.BooleanField()
    NoDocbcCost = models.BooleanField()
    GenHlth = models.IntegerField()
    MentHlth = models.IntegerField()
    PhysHlth = models.IntegerField()
    DiffWalk = models.BooleanField()
    Sex = models.BooleanField()
    Age = models.IntegerField()
    Education = models.IntegerField()
    Income = models.IntegerField()
    Diabetes_binary = models.BooleanField()

    def __str__(self):
        return f"Test ID: {self.id}"
    