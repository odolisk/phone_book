from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import (EmployeeViewSet, OrganizationViewSet,
                    EditorAddView, EditorsListView, EditorRemoveView,
                    MyOrgView, obtain_token)


API_VERSION = 'v1'

v1_router = DefaultRouter()

v1_router.register('organizations', OrganizationViewSet,
                   basename='organizations')
v1_router.register(r'organizations/(?P<organization_id>\d+)/editors',
                   EditorsListView,
                   basename='editors_list')

v1_router.register(r'organizations/(?P<organization_id>\d+)/employees',
                   EmployeeViewSet,
                   basename='employees')

v1_router.register('my_org', MyOrgView, basename='my_org')


auth_patterns = [
   path('token/', obtain_token,
        name='obtain_token'),
]

urlpatterns = (
    path(f'{API_VERSION}/auth/', include(auth_patterns)),
    path(f'{API_VERSION}/organizations/<int:organization_id>/add_editor/',
         EditorAddView, name='editor_add'),
    path(f'{API_VERSION}/organizations/<int:organization_id>/remove_editor/',
         EditorRemoveView, name='editor_remove'),
    path(f'{API_VERSION}/', include(v1_router.urls)),
)
