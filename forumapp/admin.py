from django.contrib import admin
from forumapp.models import Question,Answer,Upvote

admin.site.register([Question,Answer,Upvote])

# Register your models here.
