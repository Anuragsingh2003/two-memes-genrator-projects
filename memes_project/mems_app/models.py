from django.db import models

class CaptionImage(models.Model):
    caption1 = models.CharField(max_length=100)
    caption2 = models.CharField(max_length=100)
    caption3 = models.CharField(max_length=100)
    caption_color1 = models.CharField(max_length=7,default="#ffffff")
    caption_background_color1 = models.CharField(max_length=7,default="#ffffff")
    caption_color2 = models.CharField(max_length=7,default="#ffffff")
    caption_background_color2 = models.CharField(max_length=7,default="#ffffff")
    caption_color3 = models.CharField(max_length=7,default="#ffffff")
    caption_background_color3 = models.CharField(max_length=7,default="#ffffff")
    position1 = models.CharField(max_length=10,blank=True, null=True)
    position2 = models.CharField(max_length=10,blank=True, null=True)
    position3 = models.CharField(max_length=10,blank=True, null=True)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.caption1