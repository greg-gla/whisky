from django.db import models

# Create your models here.
# super user: admin ; password: 123
class User(models.Model):
    NICK_NAME_MAX_LENGTH = 128
    PASSWORD_MAX_LENGTH = 32

    id = models.IntegerField(primary_key=True)
    nickname = models.CharField(max_length=NICK_NAME_MAX_LENGTH)
    email = models.EmailField()
    password = models.CharField(max_length=PASSWORD_MAX_LENGTH)
    last_login = models.DateTimeField()

    def __str__(self) :
        return self.nickname

class Distillery(models.Model):
    NAME_MAX_LENGTH = 128
    LOCATION_MAX_LENGTH = 512
    DESCRIPTION_MAX_LENGTH = 1024

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    logo = models.ImageField(upload_to='logo_images',blank=True)
    location = models.CharField(max_length=LOCATION_MAX_LENGTH)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH)
    
    class Meta:
        verbose_name_plural = 'Distilleries'


    def __str__(self) :
        return self.name

class Whisky(models.Model):
    NAME_MAX_LENGTH = 128
    DESCRIPTION_MAX_LENGTH = 512

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    age = models.IntegerField(default=0)
    abv = models.IntegerField(default=0)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH)
    image = models.ImageField(upload_to='whiskey_images',blank=True)
    distillery = models.ForeignKey(Distillery,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Whiskies'

    def __str__(self):
        return self.name

class Rating(models.Model):
    VERBAL_RATING_MAX_LENGTH = 512

    id = models.IntegerField(primary_key=True)
    numeric_rating = models.FloatField(default=0.0)
    verbal_rating = models.CharField(max_length=VERBAL_RATING_MAX_LENGTH)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    whisky_id = models.ForeignKey(Whisky,on_delete=models.CASCADE)

    def __str__(self) :
        return self.verbal_rating





