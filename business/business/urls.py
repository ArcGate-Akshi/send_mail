
from django.contrib import admin
from django.urls import path
from promomail import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home),

    path('mail_list',views.mail_list),
    path('home', views.home),
]
# path('send_mail', views.send_mail),
# path('individual', views.individual),
# path('send_selected', views.send_selected),
