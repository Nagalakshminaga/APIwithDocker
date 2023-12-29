from django.urls import path
from . import  views

urlpatterns = [
    # path('student_details/',views.student_details, name='student_details'),
    # path('add_student/',views.add_student, name='add_student'),
    # path('student_update/<int:pk>/',views.student_update,name='student_update'),
    # path('student_delete/<int:pk>/',views.student_delete,name='student_delete'),
    # path('student_get/<int:pk>/',views.student_get,name='student_get'),
    path('add_student/',views.add_student,name='add_student'),
    path('student_get_update_delete/<int:pk>/',views.student_get_update_delete,name='student_get_update_delete'),
    ]