from django.core.exceptions import ValidationError

def validate_account_avatar_file_size(value):
    filesize= value.size
    
    if filesize > 10485760:
        raise ValidationError("Image size should be less than 10Mb.")
    else:
        return value
    
