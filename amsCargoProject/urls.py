"""amsCargoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from amcCargoApp.views import account_closing_details, summary_details


admin.site.site_header = "AMS Cargo Company"
admin.site.site_title = "AMS Cargo Company"
admin.site.index_title = "AMS Cargo Company"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('closing-details/',  account_closing_details, name='lahore-closing'),
    path('summary-details/',  summary_details, name='summary-closing')
    
    ]