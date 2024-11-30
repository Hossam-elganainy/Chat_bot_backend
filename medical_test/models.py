from django.db import models
from users.models import User

class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='tests')
    attachment = models.ImageField(upload_to='test images')
    response = models.FloatField(blank= True , null= True)

    def __str__(self):
        return f'{self.user.email} - Test {self.pk}'