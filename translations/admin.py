from django.contrib import admin
from translations.models import English, Latvian, EnLv

# Register your models here.
admin.site.register(English)
admin.site.register(Latvian)
admin.site.register(EnLv)
