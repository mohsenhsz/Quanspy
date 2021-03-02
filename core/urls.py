from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('buckets/', views.BucketHome.as_view(), name='buckets_home'),
    path('bucket_delete/<str:key>/', views.BucketDelete.as_view(), name='bucket_delete'),
    path('bucket_download/<str:key>/', views.BucketDownload.as_view(), name='bucket_download'),
    path('bucket_upload/', views.BucketUpload.as_view(), name='bucket_upload'),
]
