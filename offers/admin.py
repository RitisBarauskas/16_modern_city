from django.contrib import admin

from offers.models import Region, City, Offer, Like, Comment, Tag


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'population', 'region')
    search_fields = ('name', 'population', 'region')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'city', 'created_at', 'expired_at')
    search_fields = ('name', 'author', 'city', 'created_at', 'expired_at')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('author', 'offer', 'created_at')
    search_fields = ('author', 'offer', 'created_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'offer', 'created_at')
    search_fields = ('author', 'offer', 'created_at')
