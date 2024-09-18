from django.db import models

class Course(models.Model):
    course_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    course_link = models.URLField(max_length=500)
    original_price = models.CharField(max_length=50)
    image_link = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title