from django.db import models
import re
# Create your models here.
class PlayerManager(models.Manager):
    def player_validator(self,postdata):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
        if len(postdata['username'])<1:
            errors['username']="Your user name must be more than 1 character"
        if not EMAIL_REGEX.match(postdata['email']):
            errors['email']="Email must be a valid format"
        if len(postdata['password'])<8:
            errors['password']="Password must be at least 8 characters"
        if postdata['password'] != postdata['confirmpassword']:
            errors['confirmpassword']="Your password and confirm password should match"
        return errors

class ThemeManager(models.Manager):
    def theme_validator(self,postdata):
        errors={}
        if len(postdata['title'])<8:
            errors['title']="Title must be more than 7 characters"
        if len(postdata['description'])<50:
            errors['description']="Description must be more than 50 characters"
        return errors

class Player(models.Model):
    username=models.CharField(max_length=255, unique=True)
    email=models.CharField(max_length=255, unique=True)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=PlayerManager()   

class Theme(models.Model): # will be manually entered in the shell until we have an admin mode
    title=models.CharField(max_length=255)
    description=models.TextField()
    status=models.CharField(max_length=255, default="Not Started")
    #player=models.ForeignKey(Player, related_name="player_theme", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ThemeManager()

class Puzzle(models.Model): # will be manually entered in the shell until we have an admin mode
    question=models.CharField(max_length=255)
    hint=models.CharField(max_length=255)
    story=models.TextField()
    status=models.CharField(max_length=255, default="Not Started")
    answer=models.CharField(max_length=255)
    #theme=models.ForeignKey(Theme, related_name="puzzle_theme", default="", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



