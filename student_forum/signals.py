# from django.db.models.signals import post_save
# 	#I have used django user model to use post save, post delete.
# from accounts.models import Account
# from .models import StudentFeedback, CompanyInternship
# from dashboard.models import StudentsPerCompanyInfo
# from django.dispatch import receiver

# @receiver(post_save,sender=StudentFeedback)
# def verify_student(sender,instance,created,**kwargs):
#     if created:
#         if instance.is_checked is not True:
#             account = Account.objects.filter(email=instance.email)
#             if account:
#                 instance.is_verified = True
#                 instance.is_checked = True
#                 instance.feedback_given_by = account[0]
#                 print("Account does exist")
#                 instance.save()
#             else:
#                 instance.is_checked = True
#                 instance.save()
#                 print("Account does not exist")
#         else:
#             print("Feedback is checked once")


# # @receiver(post_save,sender=CompanyInternship)
# # def post_save_increase_students_per_company(sender,instance,created,**kwargs):
# #     if created:
# #         try:
# #            obj, created = StudentsPerCompanyInfo.objects.get_or_create(company=instance.company)
# #            query_set = CompanyInternship.objects.filter(company=instance.company)
# #            obj.number_of_students = len(query_set)
# #            obj.save()
# #            print("saved...")
# #         except:
# #             pass
# #     else:
# #         query_set = CompanyInternship.objects.filter(company=instance.company)
# #         obj = StudentsPerCompanyInfo.objects.filter(company=instance.company)
# #         obj.number_of_students = len(query_set)
# #         obj.save()
    

