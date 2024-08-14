from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, student_form_view, delete_student_view, student_list_view

# Seting up the router for the API
router = DefaultRouter()
router.register(r'students', StudentViewSet)  # Registering the StudentViewSet for API routes

urlpatterns = [
    # URL patterns for student views
    path('students/', student_list_view, name='student_list_view'),  # View for listing students
    path('students/add/', student_form_view, name='student_form'),    # View for adding a new student
    path('students/<int:pk>/update/', student_form_view, name='student_update'),  # View for updating a student
    path('students/<int:pk>/delete/', delete_student_view, name='student_delete'),  # View for deleting a student
    path('api/', include(router.urls)),  # Including API routes for the StudentViewSet
]
