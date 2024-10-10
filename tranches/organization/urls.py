from django.urls import path
from organization.views import OrganizationView, OrganizationMemberView, CreditsView

urlpatterns = [
    path('organizations/', OrganizationView.as_view({'get': 'list', 'post': 'create'}), name='organization-list'),
    path('organizations/<int:pk>/', OrganizationView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='organization-detail'),
    path('organization-members/', OrganizationMemberView.as_view({'get': 'list', 'post': 'create'}), name='organization-member-list'),
    path('organization-members/<int:pk>/', OrganizationMemberView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='organization-member-detail'),
    path('credits/', CreditsView.as_view({'get': 'list', 'post': 'create'}), name='credits-list'),
    path('credits/<int:pk>/', CreditsView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='credits-detail'),
]