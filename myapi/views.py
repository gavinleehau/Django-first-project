from copy import error
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapi.models import Reporter
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import ReporterSerializer
# Create your views here.


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def api_all_reporter(request):
    reporters = Reporter.objects.all()
    # muốn coi all ( so nhieu ) thi truyen cho no many True
    mydata = ReporterSerializer(reporters, many=True)
    # results=[]
    # for reporter in reporters:
    #     results.append({
    #         'first_name': reporter.first_name,
    #         'last_name': reporter.last_name,
    #         'email': reporter.email,
    #     })
    return Response(data=mydata.data, status=200)

# R
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def api_view_reporter(request, reporter_id):
    try:
        reporter= Reporter.objects.get(id=reporter_id)
        mydata = ReporterSerializer(reporter)
        
        # result = {
        #     'first_name': reporter.first_name,
        #     'last_name': reporter.last_name,
        #     'email': reporter.email,
        # }
        return Response(data=mydata.data, status=200)
    except Reporter.DoesNotExist:
        return Response(data={"message": f"Reporter id{reporter_id} not found !!!"}, status=404)

# C
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def api_add_reporter(request):
    data = ReporterSerializer(data=request.data)
    if data.is_valid():
        print(data.validated_data)
        data.save()
        # return thanh cong
        return Response(data={
            'message':f"Reporter id created:{dict(data.validated_data)}"
        }, status=201)
    else:
        print(data.errors)
        return Response(data={
        'message':data.errors
    }, status=400)
    # creates_id = Reporter.objects.create(**request.data)
    

# U
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def api_upate_reporter(request, reporter_id):
    try:
        reporter= Reporter.objects.get(id=reporter_id)
        reporter.first_name = request.data.get('first_name',reporter.first_name)
        reporter.last_name = request.data.get('last_name',reporter.last_name)
        reporter.email = request.data.get('email',reporter.email)
        reporter.save()
        result = {
            'first_name': reporter.first_name,
            'last_name': reporter.last_name,
            'email': reporter.email,
        }
        return Response(data={
            'message':f"Update reporter id{reporter_id} successful ",
            'data':result
        }, status=200)
    except Reporter.DoesNotExist:
        return Response(data={"message": f"Reporter id{reporter_id} not found !!!"}, status=404)

# D
@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def api_delete_reporter(request,reporter_id):
    try:
        reporter= Reporter.objects.get(id=reporter_id)
        reporter.delete()
        return Response(data={
            'message':f"Delete reporter id{reporter_id} successful ",
        }, status=200)
    except Reporter.DoesNotExist:
        return Response(data={"message": f"Reporter id{reporter_id} not found !!!"}, status=404)




# Classsssssssssssssssss
class ReporterListView(APIView):
    def get(self, request):
        reporters = Reporter.objects.all()
        results=[]
        for reporter in reporters:
            results.append({
                'first_name': reporter.first_name,
                'last_name': reporter.last_name,
                'email': reporter.email,
            })
        return Response(data=results, status=200)
    
    def post(self, request):
        creates_id = Reporter.objects.create(**request.data)
        return Response(data={
            'message':f"Reporter id created:{creates_id}"
        }, status=201)

# API co tham so
class ReporterAPI(APIView):

    def get(self, request, reporter_id):
        try:
            reporter= Reporter.objects.get(id=reporter_id)
            result = {
                'first_name': reporter.first_name,
                'last_name': reporter.last_name,
                'email': reporter.email,
            }
            return Response(data=result, status=200)
        except Reporter.DoesNotExist:
            return Response(data={"message": f"Reporter id{reporter_id} not found !!!"}, status=404)
      
    def put(self, request, reporter_id):
        try:
            reporter= Reporter.objects.get(id=reporter_id)
            reporter.first_name = request.data.get('first_name',reporter.first_name)
            reporter.last_name = request.data.get('last_name',reporter.last_name)
            reporter.email = request.data.get('email',reporter.email)
            reporter.save()
            result = {
                'first_name': reporter.first_name,
                'last_name': reporter.last_name,
                'email': reporter.email,
            }
            return Response(data={
                'message':f"Update reporter id{reporter_id} successful ",
                'data':result
            }, status=200)
        except Reporter.DoesNotExist:
            return Response(data={"message": f"Reporter id{reporter_id} not found !!!"}, status=404)
    
    def delete(self, request, reporter_id):
        try:
            reporter= Reporter.objects.get(id=reporter_id)
            reporter.delete()
            return Response(data={
                'message':f"Delete reporter id{reporter_id} successful ",
            }, status=200)
        except Reporter.DoesNotExist:
            return Response(data={"message": f"Reporter id{reporter_id} not found !!!"}, status=404)
    
        
    

	