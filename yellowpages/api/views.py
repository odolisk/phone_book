from rest_framework import filters, viewsets

from django.shortcuts import get_object_or_404

from .models import Employee, Organization
from .paginators import CustomPageNumberPagination
from .serializers import (EmployeeSerializer, OrganizationsListSerializer,
                          OrganizationsRetriveSerializer)


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    pagination_class = CustomPageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'list':
            return OrganizationsListSerializer
        return OrganizationsRetriveSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def get_queryset(self):
        organization_id = self.kwargs.get('organization_id')
        organization = get_object_or_404(Organization, id=organization_id)
        return organization.employees.all()
