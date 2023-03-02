from django.apps import AppConfig


class StudentForumConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student_forum'

    def ready(self):
        import student_forum.signals
