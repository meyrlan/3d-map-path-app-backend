from django.contrib import admin
from core.models import Profile, Interest, Event, Image, User, DataSet
from django.utils.translation import ugettext_lazy as _
from rest_framework.reverse import reverse
from django.utils.html import format_html


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "phone",
    )
    search_fields = ["email", "phone"]
    fields = [
        "email",
        "phone",
    ]


# @admin.register(Profile)
# class ProfileModelAdmin(admin.ModelAdmin):
#     list_display = (
#         "first_name",
#         "last_name",
#         "user",
#         "get_interests",
#     )
#     list_filter = ["sex"]
#     search_fields = ["first_name", "last_name"]
#     fields = [
#         "first_name",
#         "last_name",
#         "bio",
#         "sex",
#         "birth_date",
#         "user",
#         "interests",
#     ]

#     def get_interests(self, profile):
#         return self.links_to_objects(profile.interests.all())

#     @classmethod
#     def links_to_objects(cls, objects):
#         interests_list = "<ol>"
#         for obj in objects:
#             link = reverse("admin:core_interest_change", args=[obj.id])
#             interests_list += "<li><a href='%s'>%s</a></li>" % (link, obj.title)
#         interests_list += "</ol>"
#         return format_html(interests_list)


# @admin.register(Interest)
# class InterestModelAdmin(admin.ModelAdmin):
#     list_display = ["title", "get_profiles"]
#     list_filter = ["title"]
#     fields = ["title"]
#     readonly_fields = ["get_profiles"]

#     def get_profiles(self, interest):
#         return self.links_to_profiles(interest.profiles.all())

#     @classmethod
#     def links_to_profiles(cls, profiles):
#         profiles_list = "<ol>"
#         for obj in profiles:
#             link = reverse("admin:core_profile_change", args=[obj.id])
#             profiles_list += "<li><a href='%s'>%s</a></li>" % (link, obj.full_name)
#         profiles_list += "</ol>"
#         return format_html(profiles_list)


# @admin.register(Event)
# class EventModelAdmin(admin.ModelAdmin):
#     list_display = [
#         "title",
#         "capacity",
#         "date_time",
#         "age_limit",
#         "description",
#         "photo",
#         "owner"
#     ]
#     list_filter = ["title"]
#     search_fields = ["title"]
#     fields = [
#         "title",
#         "capacity",
#         "date_time",
#         "age_limit",
#         "description",
#         "photo",
#         "owner",
#         "interests",
#         "attendees",
#     ]


# @admin.register(Image)
# class ImageModelAdmin(admin.ModelAdmin):
#     list_display = ["name", "image", "created_at", "event"]
#     fields = ["name", "image", "event"]
