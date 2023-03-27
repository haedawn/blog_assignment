from django.db import models

# Create your models herce.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    introduce = models.TextField()
    content=models.TextField()


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]
        