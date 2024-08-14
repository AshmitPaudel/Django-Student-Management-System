from django.contrib import admin
from django.urls import path, include
from student.views import home_view  

urlpatterns = [
    path('', home_view, name='home'),  # Redirects to the home view (student form)
    path('admin/', admin.site.urls),  # Admin site for managing models
    path('students/', include('student.urls')),  # Includes URLs from the student app
]
