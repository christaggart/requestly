from django.contrib import admin
from requests.models import Request
class RequestAdmin(admin.ModelAdmin):
    pass

admin.site.register(Request, RequestAdmin)

