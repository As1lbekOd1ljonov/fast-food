from rest_framework.pagination import CursorPagination


class CategoryPagination(CursorPagination):
    ordering = 'id'
    page_size = 2


class ProductPagination(CursorPagination):
    ordering = 'id'
    page_size = 2


class OrderPagination(CursorPagination):
    ordering = 'id'
    page_size = 2