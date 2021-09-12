from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from django.db.models import Q
from django.shortcuts import get_object_or_404

from .models import Organization, User
from .paginators import CustomPageNumberPagination
from .permissions import IsAuthorOrAuthReadOnly
from .serializers import (
    EmployeeSerializer, OrganizationsListSerializer,
    OrganizationsRetriveSerializer, UserObtainTokenSerializer)


@api_view(('POST',))
@permission_classes([permissions.AllowAny])
def obtain_token(request):
    """
    Takes email and password from request and
    return access token.
    """
    serializer = UserObtainTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data['email']
    user = get_object_or_404(User, email=email)
    password = serializer.validated_data['password']

    if not user.check_password(password):
        res = {'password': f'Пароль не верен для email: {email}'}
        return Response(
            data=res,
            status=status.HTTP_400_BAD_REQUEST)

    token = AccessToken.for_user(user)
    return Response({'token': str(token)},
                    status=status.HTTP_200_OK)


class MyOrgView(viewsets.ModelViewSet):
    pagination_class = CustomPageNumberPagination
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = OrganizationsListSerializer

    def get_queryset(self):
        user = self.request.user
        return Organization.objects.filter(Q(author=user) | Q(editors=user))


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    pagination_class = CustomPageNumberPagination
    filter_backends = (filters.SearchFilter,)
    permission_classes = (IsAuthorOrAuthReadOnly, )
    search_fields = ('name',)
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'list':
            return OrganizationsListSerializer
        return OrganizationsRetriveSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def get_queryset(self):
        organization_id = self.kwargs.get('organization_id')
        organization = get_object_or_404(Organization, id=organization_id)
        return organization.employees.all()
