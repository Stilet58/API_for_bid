"""API_for_bid URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from api_partners.views import *
from api_organization.views import *
from django.contrib import admin


#Роутер для автоматизации перехода по url
router = routers.DefaultRouter()
router.register(r'proposals', ProposalViewSet)
router.register(r'bids', BidViewSet)
router.register(r'forms', FormViewSet)
router.register(r'credit_organizations', CreditOrganizationViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]