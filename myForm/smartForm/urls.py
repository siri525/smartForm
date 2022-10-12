from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formAccept',views.formAccept,name="formAccept")
]
