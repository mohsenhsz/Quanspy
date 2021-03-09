from django.urls import path, include
from . import views
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = 'accounts'

api_views = [
    # path('api-token-auth/', obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('dashboard/<str:username>/', views.UserDashboard.as_view(), name='dashboard'),
    path('api/', include(api_views)),
]



# {
#   "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNTQwNDg1NCwianRpIjoiY2IzODlhMzU4ZjMzNGU1NjhjOWI3Y2I2MDcxN2Y2MzkiLCJ1c2VyX2lkIjoxfQ.hXdQlLZgnIoyPQEtgdTh-vwtB6i2NMCangLdU_SQmTY",
#   "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE1MzE4NzU0LCJqdGkiOiJjNTU1YTJkYTg1OGE0YmYzYjc0ZWIzYzM3N2ZkZTYyNyIsInVzZXJfaWQiOjF9.fo8FBOG-OLU8Vm0znyr2xmIc59AYSfXC32Dn1Y8lgHI"
# }








