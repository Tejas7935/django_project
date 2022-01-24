
from django.contrib import admin
from .models import Post
from .models import Person
from .models import Cart

admin.site.register(Post)
admin.site.register(Person)
admin.site.register(Cart)