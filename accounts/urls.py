from django.urls import path
from . import views

app_name = "accounts"

urlpatterns =  [
   path('signup/', views.signup_view, name="signup"),
   path('signin/', views.signin_view, name="signin"),
   path('signout/', views.signout_view, name="signout"),
   path('account-activation-emaail-sent/', views.account_activation_email_sent, name="account_activation_email_sent"),
   path('activate/<uidb64>/<token>/', views.activate_account, name="activate_account"),
   
   # path("profile/", views.account_profile, name="account_profile"),
   # path("profile/address/", views.account_address, name="account_address"),
   
   # path('password_recovery_email/', views.password_recovery_email, name="password_recovery_email"),
   # path('password_reset_confirm/', views.password_reset_confirm, name="password_reset_confirm"),
   # path('password_reset_complete/', views.password_reset_complete, name="password_reset_complete"),
   # path('password_reset_done/', views.password_reset_done, name="password_reset_done"),

   # ajax    
   path('load-university-contents/', views.load_university_contents, name="load-university-contents"),


] 