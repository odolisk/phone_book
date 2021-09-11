from rest_framework.routers import DefaultRouter

from django.urls import include, path

# from .views import (
#     CategoryViewSet, CommentViewSet, GenreViewSet,
#     ReviewViewSet, TitleViewSet, UserViewSet,
#     create_user_or_get_code, obtain_token)

from .views import (EmployeeViewSet, OrganizationViewSet)

API_VERSION = 'v1'

v1_router = DefaultRouter()

v1_router.register('organizations', OrganizationViewSet,
                   basename='organizations')
v1_router.register(r'organizations/(?P<organization_id>\d+)/employees',
                   EmployeeViewSet,
                   basename='employees')

urlpatterns = (
    path(f'{API_VERSION}/', include(v1_router.urls)),
)
