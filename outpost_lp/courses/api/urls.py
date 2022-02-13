from django.urls import path, include
from rest_framework import routers 
from . import views

app_name = 'courses'

router = routers.DefaultRouter()
router.register(app_name, views.CourseViewSet)

urlpatterns = [
    path('subjects/', views.SubjectListView.as_view(), name='subject_list'),
    path('subjects/<int:pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),
    path('', include(router.urls)),
]
