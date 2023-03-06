# from django.db.models.signals import post_save
# 	#I have used django user model to use post save, post delete.
# from .models import (
#     StudentCurrentEducationInfo, 
#     GraduationExamName,
#     PostGraduationExamName,
#     GraduationInfo,
#     PostGraduationInfo

# )
# from django.dispatch import receiver

# @receiver(post_save,sender=StudentCurrentEducationInfo)
# def create_student_university_profile(sender,instance,created,**kwargs):
#     if created:
#         if instance.university_level == "graduation":
#             try:
#                 exam_name = GraduationExamName.objects.filter(id=instance.exam_name)[0]
#                 print(exam_name)
#                 GraduationInfo.objects.create(
#                                 account=instance.account,
#                                 exam=exam_name,
#                                 subject=instance.subject,
#                                 university=instance.university,
#                                 which_year_student=instance.which_year_student,
#                             )
#             except GraduationExamName.DoesNotExist:
#                 print("Ups... Something is wrong")
            
#         if instance.university_level == "post_graduation":
#             try:
#                 exam_name = PostGraduationExamName.objects.filter(id=instance.exam_name)[0]
#                 print(exam_name)
#                 PostGraduationInfo.objects.create(
#                                 account=instance.account,
#                                 exam=exam_name,
#                                 subject=instance.subject,
#                                 university=instance.university,
#                                 which_year_student=instance.which_year_student,
#                             )
#             except PostGraduationExamName.DoesNotExist:
#                 print("Ups... Something is wrong")



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
    

