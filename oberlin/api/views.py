
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics #importing the generic views
from .models import College #importing the model
from .serializers import CollegeSerializer #importing the serializer
from rest_framework.views import APIView

class CollegeListCreate(generics.ListCreateAPIView):
    queryset = College.objects.all() #querying all the objects of the model
    serializer_class = CollegeSerializer #using the CollegeSerializer class

    # overlide http method
    # we can't overide generic views

    def delete(self, request, *args, **kwargs):
        College.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CollegeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView): #deleting view
    queryset = College.objects.all() #querying all the objects of the model
    serializer_class = CollegeSerializer #using the CollegeSerializer class
    lookup_field = 'pk' ##using the primary key as the lookup field

# making our own view that does not inherit from the generic views
class CollegeList(APIView):

    def get(self,request,*args,**kwargs):
        name = request.query_params.get('name','')
        if(name):
            # filtering the colleges based on the college name
            colleges = College.objects.filter(name__icontains=name)
        else:
            # if no title provided, return all the colleges
            colleges = College.objects.all()

        # serializing the data
        serializer = CollegeSerializer(colleges,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


