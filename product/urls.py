from django.urls import path, include
from .views import Home,Categorys
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'products',Home, basename='products')
router.register(r'category',Categorys,basename='category')

urlpatterns = [
    path('',include(router.urls))
]
