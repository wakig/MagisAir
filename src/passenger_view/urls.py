from django.urls import path
from .views import (
    home_view,
    flight_select_view,
    pass_info_view
                    )


app_name = 'passenger_view'
urlpatterns = [
    path('', home_view, name='pass_home'),
    path('flights/', flight_select_view, name='pass_flights'),
    # path('flights/<id:pk>'),
    path('pass_info/', pass_info_view, name='pass_info')
]
