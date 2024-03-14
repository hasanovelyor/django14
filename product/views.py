# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serial import ProductSerializer,CategorySerializer
from .models import Product,Category
# # Create your views here.
class Home(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class Categorys(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# from django.shortcuts import render
# from rest_framework.viewsets import ModelViewSet
# from .serial import ProductSerializer,CategorySerializer
# from .models import Product,Category
# # Create your views here.
# class Home(ModelViewSet):
#     queryset =Product.objects.all()
#     serializer_class = ProductSerializer

# class Asalom(ModelViewSet):
#     queryset =Category.objects.all()
#     serializer_class = CategorySerializer

# # # class Home(ModelViewSet):
# # #     queryset =categories.objects.all()
# # #     serializer_class = ProductSerializer

