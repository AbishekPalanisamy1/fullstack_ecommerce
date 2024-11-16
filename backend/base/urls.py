from django.urls import path

from . import views


urlpatterns = [
    path("", views.getroutes, name="getroutes"), 
    path("products/", views.getproducts, name="getproducts"), 
    path("products/", views.getproducts, name="getproducts"), 

   path("products/<str:pk>/", views.getproduct, name="product"), 

]