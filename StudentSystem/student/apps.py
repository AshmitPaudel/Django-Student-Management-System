from django.apps import AppConfig

class StudentConfig(AppConfig):
    """
    Configuration for the 'student' application.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "student"
