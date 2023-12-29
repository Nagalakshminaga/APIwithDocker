from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
# def student_details(request):
#     if request.method == 'GET':
#         students = Student.objects.all().values()
#         print("myfirststudent",students)
#         return JsonResponse({'students': list(students)})
    
# @csrf_exempt    
# def add_student(request):
#     if request.method == 'POST':
#         data = request.POST
#         student = Student.objects.create(
#             name=data.get('name'),
#             standard=data.get('standard'),
#             blood_Group=data.get('blood_Group'),
#             address=data.get('address'),
#         )
#         student.save()
#         return JsonResponse({'id': student.id}, status=201)

# @csrf_exempt
# def student_get(request, pk):
#     try:
      
#         if request.method == 'GET':
#             student = Student.objects.get(pk=pk)
#             student_data = {
#                 'id': student.id,
#                 'name': student.name,
#                 'standard': student.standard,
#                 'blood_Group': student.blood_Group,
#                 'address': student.address,
#             }
#         return JsonResponse(student_data)
#     except Student.DoesNotExist:
#         return JsonResponse({'message': 'Student not found'}, status=404)

   
    
# @csrf_exempt
# def student_update(request, pk):
#     if request.method == 'PUT':
#         student = Student.objects.get(pk=pk)
#         data = request.POST
#         student.name = data.get('name')
#         student.standard = data.get('standard')
#         student.blood_Group = data.get('blood_Group')
#         student.address = data.get('address')
#         student.save()
#         return JsonResponse({'message': 'Student updated successfully'})
    
# @csrf_exempt
# def student_delete(request,pk):
#     student = Student.objects.get(pk=pk)
#     if request.method == 'DELETE':
#         student.delete()
#         return JsonResponse({'message': 'Student deleted successfully'}, status=204)

@api_view(['GET', 'POST'])
def add_student(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def student_get_update_delete(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'message': 'Student not found'}, status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        student.delete()
        return Response({'message': 'Student deleted successfully'}, status=204)
# import json

# # Create your views here.
# @api_view(['GET', 'POST'])
# def add_student(request):
    
#     if request.method == 'GET':
#         students =Student.objects.all()
#         return Response(students.data)

#     elif request.method == 'POST':
#         data = request.POST
#         student = Student.objects.create(
#             name=data.get('name'),
#             standard=data.get('standard'),
#             blood_Group=data.get('blood_Group'),
#             address=data.get('address'),
#         )
#         student.save()
#         return Response({'id': student.id}, status=201)

    
#     return Response ("good morning everyone")