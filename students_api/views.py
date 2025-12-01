from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentModel
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST','DELETE'])
def students(request):
  

    if request.method == "GET":
        # students_instance=StudentModel.objects.all()
        ser_py_data = StudentSerializers(StudentModel.objects.all(),many=True)#old data
        return Response(ser_py_data.data)
    

    if request.method == 'POST':
        ser_data=StudentSerializers(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response({"msg":"data stored"})
        
    
    if request.method == 'DELETE':
        StudentModel.objects.all().delete()
        return Response({"msg":" all data deleted"})

    



@api_view(['GET','PUT','DELETE'])        
def student(request,pk):

    try:
        stu=StudentModel.objects.get(id=pk)#old data
    except:
        return Response({'msg':'requested id record is not existed in db'})
            

    
    if request.method == "GET":
    
        ser_py_data = StudentSerializers(stu)#old data
        return Response(ser_py_data.data)
    
    if request.method == "PUT":
        ser_data=StudentSerializers(stu,data=request.data,partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response({"msg":"data updated"})
    
    if request.method == "DELETE":
        stu.delete()
        return Response({"msg":"data delete"})
        
    