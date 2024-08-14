import uuid
from django.core.exceptions import ValidationError
from django.db import models

# Validation for name
def validate_name(value):
    if not value.replace(" ", "").isalpha():
        raise ValidationError('Name must contain only alphabetic characters.')

# Validation for age
def validate_age(value):
    if value < 0 or value > 100:
        raise ValidationError('Age must be between 0 and 100.')

# Validation for address
def validate_address(value):
    if not all(c.isalnum() or c.isspace() or c in ",.-" for c in value):
        raise ValidationError('Address must contain only alphanumeric characters, spaces, and certain symbols (.,-)')

# Validation for major
def validate_major(value):
    if not value.replace(" ", "").isalpha():
        raise ValidationError('Major must contain only alphabetic characters.')

class Student(models.Model):
    """
    Model representing a student, with validations for name, age, address, and major.
    """
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Unique ID for each student

    GRADE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('F', 'F'),
    ]

    name = models.CharField(
        max_length=100, 
        verbose_name="Student Name",
        validators=[validate_name]  # Validation for name
    )  # Student's name (required)

    age = models.IntegerField(
        verbose_name="Student Age",
        validators=[validate_age]  # Validation for age
    )  # Student's age (required)

    address = models.CharField(
        max_length=255, 
        verbose_name="Student Address",
        validators=[validate_address]  # Validation for address
    )  # Student's address (required)

    grade = models.CharField(
        max_length=1, 
        choices=GRADE_CHOICES, 
        blank=True, 
        null=True,
        verbose_name="Student Grade"
    )  # Student's grade (optional)

    major = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        verbose_name="Student Major",
        validators=[validate_major]  # Validation for major
    )  # Student's major (optional)

    def __str__(self):
        return self.name
