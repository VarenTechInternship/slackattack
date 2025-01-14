from django.urls import path
from rest_framework.authtoken import views as authviews
from . import views


urlpatterns = [
    path('employees/', views.ListEmployees.as_view(), name="employees"),
    path('employees/<int:emp_ID>/', views.SingleEmployeeID.as_view()),
    path('employees/<str:username>/', views.SingleEmployeeName.as_view()),
    path('pictures/', views.ListPictures.as_view(), name="allpictures"),
    path('pictures/<int:emp_ID>/', views.EmployeePictures.as_view()),
    path('pictures/<str:name>/', views.SinglePicture.as_view()),
    path('token-auth/', authviews.obtain_auth_token),
]
