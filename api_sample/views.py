from django.shortcuts import render
from rest_framework.views import APIView
from api_sample.models import StudentModel
# Create your views here.



class StudentListCreateView(APIView):

    def get(self, request):

        student_details = StudentModel.objects.all()

