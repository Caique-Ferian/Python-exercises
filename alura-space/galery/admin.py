from django.contrib import admin
from galery.models import Photography


class ListingPhotography(admin.ModelAdmin):
    list_display = ("id", "name", "subtitle", "published")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("category",)
    list_editable = ("published",)
    list_per_page = 10


admin.site.register(Photography, ListingPhotography)
