from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #тип удаления(удаляем и юзера и его статьи) CASCADE

    def __str__(self):
        return f"{self.title}-{self.content[:50]}"
