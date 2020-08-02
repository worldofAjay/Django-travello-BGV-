from django.db import models

# Create your models here.
class Resources(models.Model):

    Resourcename = models.CharField(max_length=100)
    CID= models.IntegerField()
    GRVM= models.TextField()
    Location= models.TextField()
    TMTRequest= models.IntegerField()
    BGCRequest= models.TextField()
    BGCInitiationDate= models.DateField()
    BGCStatus= models.TextField()
    ETAClosure= models.DateField()
    PendingComponents= models.TextField()
    ActualBGCClosureDate= models.DateField()
    OnboardStatus= models.TextField()
    BGCClosedAging= models.DateField()
    ContactNumber= models.IntegerField()
    Email= models.EmailField()
    ResourceAvailableon= models.DateField()
    Comments= models.TextField()
    Documentreviewcomments= models.TextField()