from django.urls import path
from video.views import FontView, AeVersionView


urlpatterns = [
    path('fonts/', FontView.as_view({'get': 'list', 'post': 'create'}), name='font-list'),
    path('fonts/<int:pk>/', FontView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='font-detail'),
    path('ae-versions/', AeVersionView.as_view({'get': 'list', 'post': 'create'}), name='ae-version-list'),
    path('ae-versions/<int:pk>/', AeVersionView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='ae-version-detail'),
]
