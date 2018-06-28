from django.contrib import admin

from .models import UserAccount
from .models import Article
from .models import Comment
from .models import Rating

admin.site.register(UserAccount)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Rating)
