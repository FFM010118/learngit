from django.shortcuts import render
from .models import *
from .ser import *
from rest_framework.response import Response
from rest_framework.views import APIView
class StuView(APIView):
    def get(self,request,**kwargs):
        if kwargs =={}:
            aa = Stuendt.objects.all()
            ser = StuSer(instance=aa, many=True,context={'request': request})
            return Response(ser.data)
        elif kwargs['pk']:
            aa = Stuendt.objects.filter(pk=kwargs['pk'])
            ser = StuSer(instance=aa, many=True,context={'request': request})
            return Response(ser.data)
    def post(self,request):
        ser = StuSer(data=request.data)
        print(request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.validated_data)
        else:
            return Response(ser.errors)
    def delete(self,request,pk):
        Stuendt.objects.get(pk = pk).delete()
        return Response('删除成功')
class ClsView(APIView):
    def get(self, request, **kwargs):
        if kwargs['pk']:
            aa = Cls.objects.filter(pk=kwargs['pk'])
            ser = ClsSer(instance=aa, many=True)
            return Response(ser.data)
        else:
            aa = Cls.objects.all()
            ser = ClsSer(instance=aa, many=True)
            return Response(ser.data)