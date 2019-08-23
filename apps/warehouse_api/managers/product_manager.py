# django
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import Http404
from django.db.models.query import QuerySet


class ProductManager(models.Manager):
    def get(self, product_id=None):
        """
        :param int product_id:  Product internal id
        :return: Product found
        :raise: 404 Error in case product was not found
        :rtype: object
        """

        try:
            product = super().get_queryset().get(id=product_id)
        except ObjectDoesNotExist:
            raise Http404

        return product

    def find(self, product_id=None):
        """
        :param int product_id: Product internal id
        :return: First product found with provided id
        :rtype: dict
        """

        return super().get_queryset().filter(id=product_id).first()

    def get_by_uuid(self, product_uuid=None):
        """
        :param uuid product_uuid:  Product e id
        :return: Product found
        :raise: 404 Error in case product was not found
        :rtype: object
        """

        try:
            product = super().get_queryset().get(uuid=product_uuid)
        except ObjectDoesNotExist:
            raise Http404

        return product

    def find_by_uuid(self, product_uuid=None):
        """
        :param uuid product_uuid: Product external id
        :return: First product found with provided external id
        :rtype: dict
        """

        return super().get_queryset().filter(uuid=product_uuid).first()

    def get_by_type(self, product_type=None):
        """
        :param str product_type: Product type acting as a category
        :return: Products with provided type
        :rtype: list
        """

        return (
            super().get_queryset()
                   .filter(type=product_type)
                   .order_by('name')
                   .values('id', 'uuid', 'name', 'price', 'status')
        )

    def all_active(self):
        """
        :return: Active products
        :rtype: QuerySet
        """

        return super().get_queryset().filter(status=True)
