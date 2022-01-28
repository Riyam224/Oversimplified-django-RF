from django.urls import path 
from . import views 



urlpatterns = [
    path('' , views.getData , name='get_data'),
    path('add/' , views.addData , name='add_data'),
]
