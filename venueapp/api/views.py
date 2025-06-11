from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from venueapp.models import PopularPlaces, FeaturedPlaces, OurServices, Question_Answer, PricingTables, Include, Message, Sosial, SiteSettings


from venueapp.api.serializers import ( PopularPlacesSerializer, PopularPlacesCreateSerializer, FeaturedPlacesSerializer,  OurServicesSerializer,
 OurServicesCreateSerializer, Question_AnswerSerializers, Question_AnswerCreateSerializer, PricingTablesSerializer,
 PricingTablesCreateSerializer, IncludeSerializer, IncludeCreateSerializer, MessageSerializer, MessageCreateSerializer, MessageUpdateSerializer,
    SosialSerializer, SosialCreateSerializer, SosialUpdateSerializer, SiteSettingsSerializer, FeaturedPlacesCreateSerializer
 )



    
class PopularPlacesListAPIView(ListAPIView):
    queryset = PopularPlaces.objects.all()
    serializer_class = PopularPlacesSerializer
    
    
class PopularPlacesCreateAPIView(CreateAPIView):
    queryset = PopularPlaces.objects.all()
    serializer_class =PopularPlacesCreateSerializer
   
    

    
class FeaturedPlacesListAPIView(ListAPIView):
    queryset = FeaturedPlaces.objects.all()
    serializer_class = FeaturedPlacesSerializer
    
class FeaturedPlacesCreateAPIView(CreateAPIView):
    queryset = FeaturedPlaces.objects.all()
    serializer_class = FeaturedPlacesCreateSerializer

    
    
class OurServicesListAPIView(ListAPIView):
    queryset = OurServices.objects.all()
    serializer_class = OurServicesSerializer
    
class OurServicesCreateAPIView(CreateAPIView):
    queryset = OurServices.objects.all()
    serializer_class = OurServicesCreateSerializer

    
 
class Question_AnswerListAPIView(ListAPIView):
    queryset = Question_Answer.objects.all()
    serializer_class = Question_AnswerSerializers

    
class Question_AnswerCreateAPIView(CreateAPIView):
    queryset =Question_Answer.objects.all()
    serializer_class = Question_AnswerCreateSerializer
    
class PricingTablesListAPIView(ListAPIView):
    queryset = PricingTables.objects.all()
    serializer_class = PricingTablesSerializer

    
class PricingTablesCreateAPIView(CreateAPIView):
    queryset = PricingTables.objects.all()
    serializer_class = PricingTablesCreateSerializer

    
    
class  IncludeListAPIView(ListAPIView):
    queryset =  Include.objects.all()
    serializer_class =  IncludeSerializer
    
class  IncludeCreateAPIView(CreateAPIView):
    queryset =  Include.objects.all()
    serializer_class =  IncludeCreateSerializer

    
    
class  MessageListAPIView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class =  MessageSerializer
    
    
class  MessageCreateAPIView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class =  MessageCreateSerializer
    
class  MessageUpdateAPIView(UpdateAPIView):
    queryset =  Message.objects.all()
    serializer_class =  MessageUpdateSerializer

    
class  SosialListAPIView(ListAPIView):
    queryset =  Sosial.objects.all()
    serializer_class =  SosialSerializer
    
    
class SosialCreateAPIView(CreateAPIView):
    queryset = Sosial.objects.all()
    serializer_class = SosialCreateSerializer
    
    
class  SosialUpdateAPIView(UpdateAPIView):
    queryset =  Sosial.objects.all()
    serializer_class =  SosialUpdateSerializer

    

class SiteSettingsListAPIView(ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer
    