from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(verbose_name="Blog Title", max_length=300)

class Posts(models.Model):
	blog = models.ForeignKey(Blog, verbose_name="Blog Post", on_delete=models.CASCADE)



