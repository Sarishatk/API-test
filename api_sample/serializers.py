from rest_framework import serializers
from api_sample.models import StudentModel

class StudentSerializer(serializers.ModelSerializer):

   class Meta:
      
      model = StudentModel

      fields = "__all__"

    #   exclude  = ("name") 