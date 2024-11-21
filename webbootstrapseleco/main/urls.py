# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('team/', views.team, name='team'),
    path('blog/', views.blog, name='blog'),
    
    path('blog/<int:blog_id>/', views.blog_details, name='blog-details'),
    path('add_blog/', views.add_blog, name = 'add_blog'),
    path('service-details/', views.service_details, name='service-details'),
    path('death_application_submitted/',views.death_application_submitted,name='death_application_submitted'),
    path('death_application/',views.death_application,name='death_application'),
    path('pan_application/',views.pan_application,name='pan_application'),
    path('pan_application_submitted/',views.pan_application_submitted, name='pan_application_submitted'),
    path('driving_license_application/',views.driving_license_application,name='driving_license_application'),
    path('driving_license_application_submitted/',views.driving_license_application_submitted,name='driving_license_application_submitted'),
    path('ration_card_application/', views.ration_card_application, name='ration_card_application'),
    path('ration_card_application_submitted/',views.ration_card_application_submitted,name='ration_card_application_submitted'),
    path('address_change_application/',views.address_change_application,name='address_change_application'),
    path('address_change_application_submitted/',views.address_change_application_submitted,name="address_change_application_submitted"),
    path('voter_registration/', views.voter_registration, name='voter_registration'),
    path('voter_registration_submitted',views.voter_registration_submitted,name='voter_registration_submitted'),

    path('check_pan_card_status/',views.check_pan_card_status, name='check_pan_card_status'),
    path('pan_card_status/',views.pan_card_status,name='pan_card_status'),
    path('check_driving_license_status/',views.check_driving_license_status,name='check_driving_license_status'),
    path('driving_license_status/',views.driving_license_status,name='driving_license_status'),
    path('check_ration_card_status/',views.check_ration_card_status,name='check_ration_card_status'),
    path('ration_card_status/',views.ration_card_status,name='ration_card_status'),
    path('check_pension_status/', views.check_pension_status,name='check_pension_status'),
    path('pension_status/',views.pension_status,name='pension_status'),


    path('download_services_pdf/', views.download_services_pdf, name='download_services_pdf'),
    path('download_services_doc/', views.download_services_doc, name='download_services_doc')
    # Add additional URL patterns for other templates
]
