from django.db import models
from django.contrib.auth.models import User

#this is the user accounts model. the User import already has all the necessary
#username, email, password etc. built in. No need to add it.
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.TextField(max_length = 11, null=True ,blank = True)
# model to allow us to store the article data
class Article(models.Model):
    category = models.TextField(max_length=None, null=True, blank=True)
    name = models.TextField(max_length=None, null=True, blank=True)
    description = models.TextField(max_length=None, null=True, blank=True)
    image = models.TextField(max_length=None, null = True, blank=True)
# model to allow us to store the comments data
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_full_name = models.TextField(max_length = None, null=True, blank=True)
    user_email = models.TextField(max_length=None, null=True, blank=True)
    comment = models.TextField(max_length=None, null=True, blank=True)
    pub_date = models.DateTimeField('date published')
# model to allow us to store the rating data
class Rating(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_email = models.TextField(max_length=None, null=True, blank=True)
    rating_type = models.BooleanField()
