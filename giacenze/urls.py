"""msa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.giacenze, name='lista_giacenze'),
    path('aggiungipc', views.aggiungipc_in_giacenza, name='aggiungi_pc'), 
    path('aggiungitelefono', views.aggiungitelefono_in_giacenza, name='aggiungi_telefono'),
    path('aggiungiperiferica', views.modifica_periferiche, name='aggiungi_periferica')
]
