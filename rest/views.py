from django.shortcuts import render
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.generics import (CreateAPIView,
# 									ListAPIView,
# 									DestroyAPIView,
# 									UpdateAPIView,
# 									RetrieveAPIView,
# 									ListCreateAPIView,
# 	)
# Create your views here.
from rest_framework.generics import (ListAPIView,
									RetrieveAPIView,
									ListCreateAPIView,
									RetrieveUpdateDestroyAPIView,

	)
from .serializers import TodoSerializer
from .models import Todo


class ListTodo(ListCreateAPIView):
	serializer_class=TodoSerializer
	queryset=Todo.objects.all()

class DetailTodo(RetrieveUpdateDestroyAPIView):
	serializer_class=TodoSerializer
	queryset=Todo.objects.all()