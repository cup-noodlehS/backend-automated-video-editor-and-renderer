from django.urls import path
from video.views import FontView, AeVersionView, VideoTemplateView, DetailedVideoTemplateView, StaticLayerView, DynamicLayerView


urlpatterns = [
    path('fonts/', FontView.as_view({'get': 'list', 'post': 'create'}), name='font-list'),
    path('fonts/<int:pk>/', FontView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='font-detail'),
    path('ae-versions/', AeVersionView.as_view({'get': 'list', 'post': 'create'}), name='ae-version-list'),
    path('ae-versions/<int:pk>/', AeVersionView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='ae-version-detail'),
    path('video-templates/', VideoTemplateView.as_view({'get': 'list', 'post': 'create'}), name='video-template-list'),
    path('video-templates/<int:pk>/', DetailedVideoTemplateView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='video-template-detail'),
    path('static-layers/', StaticLayerView.as_view({'get': 'list', 'post': 'create'}), name='static-layer-list'),
    path('static-layers/<int:pk>/', StaticLayerView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='static-layer-detail'),
    path('dynamic-layers/', DynamicLayerView.as_view({'get': 'list', 'post': 'create'}), name='dynamic-layer-list'),
    path('dynamic-layers/<int:pk>/', DynamicLayerView.as_view({'get': 'retrieve', 'put': 'update', ' delete': 'destroy'}), name='dynamic-layer-detail'),
]
