from django.contrib import admin
from .models import *


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review)

admin.site.register(College)
admin.site.register(Department)
admin.site.register(Professor)

admin.site.register(Library)