from rest_framework import serializers
from venueapp.models import ( PopularPlaces, FeaturedPlaces, OurServices, Question_Answer,
PricingTables, Include, Message, Sosial, SiteSettings )



   
class PopularPlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularPlaces
        fields = '__all__'
        
class PopularPlacesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularPlaces
        fields = '__all__'
    
    
    
class FeaturedPlacesSerializer(serializers.ModelSerializer):
    product = FeaturedPlaces
    class Meta:
        model=FeaturedPlaces
        fields= '__all__'
        
        
class FeaturedPlacesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedPlaces
        fields= '__all__'
        
        
        
class OurServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServices
        fields= '__all__'
        
        
class OurServicesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServices
        fields= '__all__'
        
        


class Question_AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question_Answer
        fields= '__all__'
        # exclude = ('id',)
        
        
class Question_AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Question_Answer
        fields = "__all__"
        
        
        
    
class PricingTablesSerializer(serializers.ModelSerializer):
     class Meta:
        model = PricingTables
        fields = '__all__'
        
        
class PricingTablesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model  = PricingTables
        fields = "__all__"        
        
        
        
class  IncludeSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Include
        fields = '__all__'
        

class  IncludeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model  =  Include
        fields = "__all__"
        
        
class  MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        

class  MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model  =  Message
        fields = "__all__"
        
        
        
class  MessageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Message
        fields = '__all__'
        

class  SosialSerializer(serializers.ModelSerializer):
    class Meta:
        model  =  Sosial
        fields = "__all__"
        
        
class  SosialCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Sosial
        fields = '__all__'
        

class  SosialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model  =  Sosial
        fields = "__all__"
        
        
        
class  SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  SiteSettings
        fields = '__all__'
        