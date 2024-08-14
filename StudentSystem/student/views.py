from django.shortcuts import get_object_or_404, render, redirect
from .forms import StudentForm
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    API view for handling CRUD operations on Student model.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

def student_form_view(request, pk=None):
    """
    View for adding or updating a student.
    If pk is provided, the form is populated with the existing student data.
    """
    if pk:  
        student = get_object_or_404(Student, pk=pk)  
        form = StudentForm(instance=student)  
        action = 'Update'  
    else:
        form = StudentForm()  
        action = 'Add'  

    if request.method == 'POST':
        if pk:  
            form = StudentForm(request.POST, instance=student)
        else:
            form = StudentForm(request.POST)  

        if form.is_valid():  
            form.save()  
            return redirect('student_list_view')  # Redirect to the student list view after saving

    return render(request, 'student/student_form.html', {'form': form, 'action': action})

def delete_student_view(request, pk):
    """
    View for deleting a student.
    A confirmation prompt is displayed before deletion.
    """
    student = get_object_or_404(Student, pk=pk)  
    if request.method == 'POST':
        student.delete()  
        return redirect('student_list_view')  # Redirect to the student list view after deletion
    return render(request, 'student/delete_student.html', {'student': student})

def home_view(request):
    """
    View for the home page, redirects to the student form.
    """
    return redirect('student_form')  

def student_list_view(request):
    """
    View for displaying the list of students.
    Retrieves all students from the database and renders the student list template.
    """
    students = Student.objects.all() 
    return render(request, 'student/student_list.html', {'students': students})
