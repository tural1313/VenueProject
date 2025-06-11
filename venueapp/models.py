from django.db import models


class PopularPlaces(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="places_imgs/")
   
    
    class Meta:
        verbose_name_plural = "Popularies"
        
    def __str__(self):
        return self.name
    
    
class FeaturedPlaces(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="featured_imgs/")
    star = models.FloatField(default=0)
    month = models.CharField(max_length=40)
    content = models.TextField()
    
    class Meta:
        verbose_name_plural = "Faturedies"  
        
    def __str__(self):
        return self.name
    
    
class OurServices(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    icon = models.TextField()
    
    class Meta:
        verbose_name_plural = "Servies"  
        
    def __str__(self):
        return self.name
    
    
class Question_Answer(models.Model):
    name = models.TextField()
    content = models.TextField()
    
    class Meta:
        ordering = ('-id',)  
        
    def __str__(self):
        return self.name

    
    
class Include(models.Model):
    content = models.TextField()
    
    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return self.content

    

class PricingTables(models.Model):
    title = models.CharField(max_length=150)
    price = models.CharField(max_length=20)
    includes = models.ManyToManyField(Include, related_name="include")
    
    class Meta:
        verbose_name_plural = "Pricinges"
        
    def __str__(self):
        return self.title
    
    
class Message(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    messages = models.TextField()
    
    class Meta:
        ordering = ('-id',)
        
    def __str__(self):
        return self.name 
    
    
class Sosial(models.Model):
    icon = models.CharField(max_length=50)
    
    class Meta:
        ordering = ('-id',)
        
    def __str__(self):
        return self.icon
        
    
class SiteSettings(models.Model):
    logo = models.CharField(max_length=50, blank=True, null=True)
    
    banner_name = models.TextField(blank=True, null=True)
    banner_content = models.TextField(blank=True, null=True)
    banner_image = models.ImageField(upload_to="site_imgs/", blank=True, null=True)
    
    
    Featured_midle_name = models.TextField(blank=True, null=True)
    middle_title = models.TextField(blank=True, null=True)
    
    bottom_title = models.TextField(blank=True, null=True)
    ebotton_title = models.TextField(blank=True, null=True)
    ebotton_content = models.TextField(blank=True, null=True)
    
    presentation_name = models.TextField(blank=True, null=True)
    presentation_content = models.TextField(blank=True, null=True)
    presentation_link = models.TextField(blank=True, null=True)
    
    about_name = models.TextField(blank=True, null=True)
    about_content = models.TextField(blank=True, null=True)
    
 
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=256, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True) 
    
    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"
        
    def save(self, *args, **kwargs):
        if not self.id and SiteSettings.objects.exists():
            return None
        return super(SiteSettings,self).save(*args, **kwargs)
        
    def __str__(self):
        return "Settings"  