from django.contrib import admin
from django.urls import path
from TicketSystem import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login),
    path('index/',views.index),
    path('book/',views.book),
    path('login/',views.login),
    path('logout/',views.logout),
    path('register/',views.register),
    path('buy/',views.buy),
    path('order/',views.order),
]
