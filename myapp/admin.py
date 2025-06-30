from django.contrib import admin
from myapp.models import Author,Book,Publisher
admin.site.register([Author,Book,Publisher])