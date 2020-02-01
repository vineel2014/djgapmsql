from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Band,Member

admin.site.register(Post)
admin.site.register(Band)
admin.site.register(Member)
