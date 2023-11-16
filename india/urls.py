from india.views import *
from django.urls import path
app_name='hi'
urlpatterns=[
    path('virat',virat,name='virat'),
    path('rohith',rohith,name='rohith'),
]