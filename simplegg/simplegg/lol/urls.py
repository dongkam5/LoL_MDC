from django.urls import re_path
from . import views
app_name = "lol"
urlpatterns = [
        re_path(r"^tier/$",views.getTier.as_view(),name='getTier'),
        re_path(r"^rate/$",views.getRate.as_view(),name='getRate'),
        re_path(r"^ingame/$",views.getIngame.as_view(),name='getIngame'),
]