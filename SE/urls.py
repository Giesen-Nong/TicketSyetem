from django.contrib import admin
from django.urls import path
from TicketSystem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('index/',views.index),
    path('login/',views.login),
    path('book/',views.book),
    path('logout/',views.logout),
    path('register/',views.register),
]
