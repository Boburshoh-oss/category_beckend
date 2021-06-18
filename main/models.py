from django.db import models
from django.urls import reverse
# Create your models here.
class Catigory(models.Model):
    name=models.CharField(max_length=100)
    
        
    class Meta:
        verbose_name = "Catigory"
        verbose_name_plural = "Catigorys"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Catigory_detail", kwargs={"pk": self.pk})

class Blog(models.Model):
    title         = models.CharField(max_length=250)
    post_image    = models.ImageField(upload_to='blog_rasm')
    description   = models.TextField(max_length=250)
    categories    = models.ForeignKey(Catigory, on_delete=models.CASCADE,null=True)
    

    class Meta:
        verbose_name = ("Blog")
        verbose_name_plural = ("Blogs")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Blog_detail", kwargs={"pk": self.pk})
