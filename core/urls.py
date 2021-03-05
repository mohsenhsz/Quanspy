from django.urls import path, include
from . import views
from . import api_views


app_name = 'core'
api_urls = [
    path('questions/', api_views.QuestionsListView.as_view()),
    path('questions/create/', api_views.QuestionCreateView.as_view()),
    path('questions/update/<int:pk>/', api_views.QuestionUpdateView.as_view()),
    path('questions/delete/<int:pk>/', api_views.QuestiondeleteView.as_view()),
    path('answers/create/', api_views.AnswerCreateView.as_view()),
    path('answers/update/<int:pk>/', api_views.AnswerUpdateView.as_view()),
    path('answers/delete/<int:pk>/', api_views.AnswerDeleteView.as_view()),
    ]

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('buckets/', views.BucketHome.as_view(), name='buckets_home'),
    path('bucket_delete/<str:key>/', views.BucketDelete.as_view(), name='bucket_delete'),
    path('bucket_download/<str:key>/', views.BucketDownload.as_view(), name='bucket_download'),
    path('bucket_upload/', views.BucketUpload.as_view(), name='bucket_upload'),
    path('api/', include(api_urls)),
]

