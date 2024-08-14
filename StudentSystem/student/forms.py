from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    """
    Form for creating and updating Student instances.
    """
    class Meta:
        model = Student
        fields = ['name', 'age', 'address', 'grade', 'major']
