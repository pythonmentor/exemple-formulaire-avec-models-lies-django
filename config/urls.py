"""
URL configuration for Example project.
"""

from django.contrib import admin
from django.urls import path, include

from example import views as example_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", example_views.home, name="home"),
    path(
        "parent/create/",
        example_views.parent_creation_view,
        name="parent-create",
    ),
]
