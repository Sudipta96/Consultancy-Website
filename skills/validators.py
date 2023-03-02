from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize= value.size
    
    if filesize > 20971520:
        raise ValidationError("You cannot upload file more than 20Mb")
    else:
        return value