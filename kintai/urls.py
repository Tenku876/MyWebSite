from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "kintai"

urlpatterns = [
    path('', views.index, name='index'),
    path("shukkin/", views.shukkin_view, name="shukkin_view"),
    path("taikin/", views.taikin_view, name="taikin_view")
]