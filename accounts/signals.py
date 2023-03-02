from django.db.models.signals import post_save
from .models import Account
from dashboard.models import RegistrationInfo
from django.dispatch import receiver
from datetime import datetime

@receiver(post_save,sender=Account)
def create_or_modify_registration_info(sender,instance,created,**kwargs):
    if created:
        current_month = datetime.now().strftime('%B') # February
        current_year = datetime.now().strftime('%Y')  # 2023
        try:
            registration_info_obj, created = RegistrationInfo.objects.get_or_create(current_month=current_month, current_year=current_year)
            registration_info_obj.number_of_students += 1 # num of students increases by 1 in current month
            registration_info_obj.save()
        except:
            print("Something Error Ocurred...")
