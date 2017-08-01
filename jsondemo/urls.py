
from django.conf.urls import url
from django.contrib import admin
from appjson import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^demo/', views.get_data),
]
