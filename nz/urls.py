from nz.views import*
from django.urls import path
app_name='hello'
urlpatterns=[
    path('son',son,name='son'),
    path('ravindra',ravindra,name='ravindra'),
]