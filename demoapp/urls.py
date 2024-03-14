from django.urls import path

from demoapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('user_registration/',views.user_registration,name='user_registration'),
    path('donmngmt_registration/',views.donmngmt_registration,name='donmngmt_registration'),
    path('recipient_registration/',views.recipient_registration,name='recipient_registration'),
    path('branch_registration/',views.branch_registration,name='branch_registration'),
    path('loginview',views.loginview,name='loginview'),
    path('register/',views.register,name='register'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('userhome',views.userhome,name='userhome'),
    path('donationhome',views.donationhome,name='donationhome'),
    path('recipienthome',views.recipienthome,name='recipienthome'),
    path('branchhome',views.branchhome,name='branchhome'),

    path('recipient_approval_list',views.recipient_approval_list,name='recipient_approval_list'),
    path('approve_recipient/<int:user_id>/',views.approve_recipient,name='approve_recipient'),
    path('reject_recipient/<int:user_id>/',views.reject_recipient,name='reject_recipient'),

    path('branch_approval_list', views.branch_approval_list, name='branch_approval_list'),
    path('approve_branch/<int:user_id>/', views.approve_branch, name='approve_branch'),
    path('reject_branch/<int:user_id>/', views.reject_branch, name='reject_branch'),

    path('add_donation',views.add_donation,name='add_donation'),
    path('viewDonation',views.viewDonation,name='viewDonation'),
    path('AdmviewDonation',views.AdmviewDonation,name='AdmviewDonation'),
    path('approve_donation/<int:id>',views.approve_donation,name='approve_donation'),
    path('reject_donation/<int:id>',views.reject_donation,name='reject_donation'),

    path('request_donation',views.request_donation,name='request_donation'),
    path('view_reqDonation',views.view_reqDonation,name='view_reqDonation'),
    path('AdmviewDonationRequest',views.AdmviewDonationRequest,name='AdmviewDonationRequest'),
    path('approve_donationrequest/<int:id>',views.approve_donationrequest,name='approve_donationrequest'),
    path('reject_donationrequest/<int:id>',views.reject_donationrequest,name='reject_donationrequest'),


]
