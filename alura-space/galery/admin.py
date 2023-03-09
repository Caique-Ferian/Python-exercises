from django.contrib import admin
from galery.models import Photography


class ListingPhotography(admin.ModelAdmin):
    list_display = ("id", "name", "subtitle")
    list_display_links = ("id", "name")
    search_fields = ("name",)


admin.site.register(Photography, ListingPhotography)
