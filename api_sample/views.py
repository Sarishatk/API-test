from django.shortcuts import render
from rest_framework.views import APIView
from api_sample.models import StudentModel
from api_sample.serializers import StudentSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
# Create your views here.



class StudentListCreateView(APIView):

    def get(self, request): 
        # used to list all the data from db to the client as response
        # get all objects from the Model

        student_details = StudentModel.objects.all()

        serializer = StudentSerializer(student_details, many = True)

        # conver into json

        return Response(serializer.data)
    
    def post(self, request):
     serializer = StudentSerializer(data=request.data)

     if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

     return Response(serializer.errors, status=400)
    
class StudentUpdateRetriveDeleteView(APIView):

    def get(self, request, **kwargs):

        id = kwargs.get('pk')

        student = get_object_or_404(StudentModel, id=id)  

        serializer = StudentSerializer(student)  

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, **kwargs):
       
       id = kwargs.get('pk')

       student = get_object_or_404(StudentModel,id = id)

       serializer = StudentSerializer(student, data = request.data)

       if serializer.is_valid():
          
          serializer.save()

          return Response(serializer.data, status=status.HTTP_201_CREATED)
       
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, **kwargs):
       
       id = kwargs.get('pk')

       student = get_object_or_404(StudentModel, id = id)

       student.delete()

       return Response({"message":"object deleted successfullt"},status=status.HTTP_200_OK)


