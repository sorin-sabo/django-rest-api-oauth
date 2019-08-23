# django
from django.urls import path

# local api
from apps.warehouse_api import views


urlpatterns = [
    path(
        route='list/',
        view=views.ProductList.as_view(),
        name='product_list'
    ),
    path(
        route='create/',
        view=views.ProductCreate.as_view(),
        name='product_create'
    ),
    path(
        route='<int:product_id>/',
        view=views.ProductDetails.as_view(),
        name='product_details'
    ),
    path(
        route='external/<uuid:product_uuid>/',
        view=views.ExternalProductDetails.as_view(),
        name='external_product_details'
    ),

]
