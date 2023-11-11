from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.public_home_page),
    path('login',views.login_all),
    path('admin_home',views.admin_home),
    path('admin_manage_block',views.manage_block),
    path('update_block/<id>',views.update_block),
    path('delete_block/<id>',views.delete_block),
    path('admin_manage_district',views.manage_district),
    path('update_district/<id>',views.update_district),
    path('delete_district/<id>',views.delete_district),
    path('admin_manage_type',views.manage_type),
    path('update_type/<id>',views.update_type),
    path('delete_type/<id>',views.delete_type),
    path('admin_manage_officer',views.manage_officer),
    path('delete_officer/<id>',views.delete_officer),
    path('admin_view_users',views.view_users),
    path('admin_view_post',views.view_post),
    path('admin_view_complaints',views.view_complaints),
    path('send_reply',views.send_reply),
    
    path('officer_home',views.officer_home),
    path('officer_view_post',views.officer_view_post),
    path('officer_update/<id>',views.officer_update),
    path('admin_manage_officer',views.manage_officer),
    path('ad_manage_officer',views.ad_manage_officer),
    path('ad_update_officer/<id>',views.ad_update_officer),
    path('ad_delete_officer/<id>',views.ad_delete_officer),

    path('user_home',views.user_home),
    path('user_registration',views.user_registration),
    path('user_send_complaint',views.user_send_complaint),
    path('user_view_reply',views.user_view_reply),
    path('user_post',views.add_post),
    path('user_post_comment',views.user_post_comment),
    path('comments',views.comments),

]