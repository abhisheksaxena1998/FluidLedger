from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Post)
admin.site.register(UserFeedback)
admin.site.register(Favourite)
admin.site.register(DetailedUser)