from django.urls import path
from . import views


urlpatterns = [
    path('update_comment', views.update_comment, name='update_comment'),
    #path('send_mail', views.send_mail, name='send_mail'),
]