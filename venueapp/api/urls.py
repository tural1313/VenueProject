from django.urls import path
from venueapp.api import views


urlpatterns = [
    path('popular-places-list/', views.PopularPlacesListAPIView.as_view()),
    path('places-create/', views.PopularPlacesCreateAPIView.as_view()),
    
    path('featured-list/', views.FeaturedPlacesListAPIView.as_view()),
    path('featured-create/', views.FeaturedPlacesCreateAPIView.as_view()),
   
    path('services-list/',views.OurServicesListAPIView.as_view()),
    path('services-create/',views.OurServicesCreateAPIView.as_view()),
    
    path('question-list/',views. Question_AnswerListAPIView.as_view()),
    path('question-create/',views.Question_AnswerCreateAPIView.as_view()),
    
    path('include-list/',views. IncludeListAPIView.as_view()),
    path('include-create/',views.IncludeCreateAPIView.as_view()),
    
    path('pricing-list/',views.PricingTablesListAPIView.as_view()),
    path('pricing-create/',views.PricingTablesCreateAPIView.as_view()),
    
    path('message-list/',views.MessageCreateAPIView.as_view()),
    path('message-create/',views.MessageUpdateAPIView.as_view()),
    
    path('sosial-list/',views.SosialListAPIView.as_view()),
    path('sosial-create/',views.SosialCreateAPIView.as_view()),
    path('sosial-update/',views.SosialUpdateAPIView.as_view()),
    
    path('Site-list/',views.SiteSettingsListAPIView.as_view()),   
]