from django.contrib import admin
from . import models


@admin.register(models.Riot)
class RiotAdmin(admin.ModelAdmin):

    search_fields = (
        'api_key',
    )