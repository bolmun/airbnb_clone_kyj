from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Information",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Time", {"fields": ("check_in", "check_out")},),
        (
            "Space Information",
            {"fields": ("room_type", "guests", "bedrooms", "beds", "baths")},
        ),
        (
            "Convenience information",
            {"fields": ("amenities", "facilities", "house_rules")},
        ),
    )

    list_display = (
        "name",
        "price",
        "country",
        "city",
        "address",
        "bedrooms",
        "beds",
        "baths",
        "guests",
        "count_amenities",
        "count_photos",
        "check_in",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "city",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "country",
    )

    search_fields = ("city", "^host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition """

    pass
