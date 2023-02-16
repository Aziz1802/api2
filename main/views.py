from main.models import Students
from main.serializes import StudentsSerializer
from rest_framework import generics
from rest_framework.response import Response
# Create your views here.

# class StudentView(APIView):
#     def get(self, request):
#         lst = Student.objects.all().values()
#         return Response({'Student':list(lst)})

#     def post(self, request):
#         post_new = Student.objects.create(
#             first_name = request.data['first_name'],
#             last_name = request.data['last_name'],
#             gender = request.data['gender'],
#             age = request.data['age'],
#         )
#         return Response({'post':model_to_dict(post_new)})

class StudentlistView(generics.ListAPIView):
    queryset=Students.objects.all()
    serializer_class = StudentsSerializer


class StudentCreateView(generics.CreateAPIView):
    queryset=Students.objects.all()
    serializer_class = StudentsSerializer

class StudentRetrieveView(generics.RetrieveAPIView):
    queryset=Students.objects.all()
    serializer_class = StudentsSerializer


class StudentsUpdateView(generics.UpdateAPIView):
    queryset=Students.objects.all()
    serializer_class = StudentsSerializer    

class StudentsDestroyView(generics.DestroyAPIView):
    queryset=Students.objects.all()
    serializer_class = StudentsSerializer 

