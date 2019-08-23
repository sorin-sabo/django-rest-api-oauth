# django
from django_filters import rest_framework as filters

# rest framework
from rest_framework import generics
from rest_framework.request import Request

# local django
from apps.crud_api.models import Product
from apps.crud_api.serializers import (
    ProductSerializer,
    BasicProductSerializer,
    ExternalProductSerializer,
)
from apps.crud_api.filters import ProductFilter

from drf_yasg.utils import swagger_auto_schema


class ProductList(generics.ListAPIView):
    """
    Product list.

    * Requires token authentication.
    * All users are authorized to access this view.
    """

    queryset = Product.objects.all_active()
    serializer_class = BasicProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProductFilter


class ProductCreate(generics.CreateAPIView):
    """
    Product create.

    * Requires token authentication
    * Only users and admins are authorized to access this view.
    """

    queryset = Product.objects.all_active()
    serializer_class = BasicProductSerializer

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            updated_by=self.request.user
        )


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Product details.

    * Requires token authentication.
    * Only users and admins are authorized to access this view.
    """

    queryset = Product.objects.all_active()
    serializer_class = ProductSerializer

    def get_object(self):
        return Product.objects.get(self.kwargs.get('product_id'))

    def get(self, request, *args, **kwargs):
        """
        Product details.

        :param Request request: client request with authorization token in header
        :param dict args: Additional arguments passed
        :param dict kwargs: Additional keyword arguments passed
        :return: Firm product requested
        :raise: 404 error in case firm admin doesn't have access to product data (product not found)
        :raise: 400 error in case product id query parameter is not provided
        """

        response = super().get(request, *args, **kwargs)

        return response

    def put(self, request, *args, **kwargs):
        """
        Update product.

        ```
        :param Request request: client request with authorization token in header
        :param dict args: Additional arguments passed
        :param dict kwargs: Additional keyword arguments passed
        :return: Firm product updated
        :raise: 404 error in case firm admin doesn't have access to product data (product not found)
        :raise: 400 error in case product id query parameter is not provided
        ```
        """

        response = super().put(request, *args, **kwargs)

        return response

    def patch(self, request, *args, **kwargs):
        """
        Partial update product.

        ```
        :param Request request: client request with authorization token in header
        :param dict args: Additional arguments passed
        :param dict kwargs: Additional keyword arguments passed
        :raise: 404 error in case firm admin doesn't have access to product data (product not found)
        :raise: 400 error in case product id query parameter is not provided
        ```
        """

        response = super().patch(request, *args, **kwargs)

        return response

    def delete(self, request, *args, **kwargs):
        """
        Delete product.

        ```
        :param Request request: client request with authorization token in header
        :param dict args: Additional arguments passed
        :param dict kwargs: Additional keyword arguments passed
        :return: Empty response with status 204
        :raise: 404 error in case firm admin doesn't have access to product data (product not found)
        :raise: 400 error in case product id query parameter is not provided
        ```
        """

        response = super().delete(request, *args, **kwargs)

        return response


class ExternalProductDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    External product details.

    * Requires token authentication.
    * Only users and admins are authorized to access this view.
    """

    queryset = Product.objects.all_active()
    serializer_class = ExternalProductSerializer

    def get_object(self):
        return Product.objects.get_by_uuid(self.kwargs.get('product_uuid'))
