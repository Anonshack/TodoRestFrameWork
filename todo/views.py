from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status


# 1-usul
# class TodoListCreateView(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#
#     def list(self, request, *args, **kwargs):
#         todos = self.get_queryset()
#         serializer = self.get_serializer(todos, many=True)
#         return Response(serializer.data)
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# 2-usul
class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
