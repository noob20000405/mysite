from django.db import models

# Create your models here.
class Heading(models.Model):
    heading_text = models.CharField(max_length=20)
    def __str__(self):
        return self.heading_text

class Content(models.Model):
    heading = models.ForeignKey(Heading, on_delete=models.CASCADE)
    title_text = models.CharField(max_length=50)
    content_text = models.FileField(upload_to='myapp/files', null=True)

    def __str__(self):
        return self.title_text