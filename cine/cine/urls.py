"""cine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sala.Controllers.IndexController import IndexController
from sala.Controllers.Salas_Controller import Salas_Controller

urlpatterns = [
    path("",IndexController.index, name='index'),
    path('/about', IndexController.about, name='about'),
    path('admin/', admin.site.urls),
    path('salas/', Salas_Controller.index, name='salas'),
    path('salas/detalleSala/<int:numero>/', Salas_Controller.detalleSala, name='detalleSala'),
    path('salas/cartelera/', Salas_Controller.cartelera, name='cartelera'),

]
