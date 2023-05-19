from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name = 'acc'

urlpatterns = [ 
    path ('login', views.login_view, name='login'),
    path ('logout', views.logout_view, name='logout'),
    path ('singup', views.singup_view, name='singup'),
    # path ('password', auth_views.PasswordChangeView.as_view())
    # path('reset_password', auth_views.PasswordResetView.as_view(), name='reset_password'),
    # path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('reset_password_Complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complet'),

         path('password_reset/',
          auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html',success_url=reverse_lazy('accounts:password_reset_done')),
               name="password_reset"),

     path('password_reset_sent/',
          auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),
          name="password_reset_done"),

     path('reset/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html',success_url=reverse_lazy('accounts:password_reset_complete')),
          name="password_reset_confirm"),

     path('password_reset_complete/',
          auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),
          name="password_reset_complete"),

]