from django.urls import path
from . import views

# localhost:8000/chai
urlpatterns = [
    path("", views.all_chai, name='all_chai'),
    path("<int:chai_id>/", views.chai_detail, name='chai_detail'), 
    # '<int: means if I get any integer, it should be named as 'chai_id' (because in views.py as well, we are receiving chai_id)
    path("chai_stores/", views.chai_store_view, name='chai_stores'), 
]
