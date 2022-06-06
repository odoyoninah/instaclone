from django.contrib import admin
from .models import User,Image,Comment,Like,Follow

# Register your models here.
admin.site.register(User)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Follow)
