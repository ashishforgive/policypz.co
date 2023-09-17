from rest_framework import viewsets
from . serializers import *
from django.http import JsonResponse

class PartyDataViewSet(viewsets.ModelViewSet):

    def partyCreate(self, request):
        try:
            data = request.data

            try:
                name = PartyData.objects.get(name=data.get('name'))
            except:
                name = None

            if name is not None:
                return JsonResponse({"status": 202, "message": "Party name already exist!!"})
            
            try:
                email = PartyData.objects.get(email=data.get('email'))
            except:
                email = None

            if email is not None:
                return JsonResponse({"status": 202, "message": "Email already exist!!"})
            
            serializer = PartyDataSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

                return JsonResponse({"status": 200, "message": "Party data has been successully submited!!", "payload": serializer.data})
            
            return JsonResponse({"status": 202, "message": "Data isn't valid!!", "errors": serializer.errors})

        except Exception as ex:
            return JsonResponse({"status": 400, "message": f"Something went wrong!! Like - {ex}."})

class CondidateDataViewSet(viewsets.ModelViewSet):

    def condidateCreate(self, request):
        try:
            data = request.data

            try:
                email = CondidateData.objects.get(email=data.get('email'))
            except:
                email = None

            if email is not None:
                return JsonResponse({"status": 202, "message": "Email already exist!!"})
            
            serializer = CondidateDataSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

                return JsonResponse({"status": 200, "message": "Condidate data has been successully submited!!", "payload": serializer.data})
            
            return JsonResponse({"status": 202, "message": "Data isn't valid!!", "errors": serializer.errors})

        except Exception as ex:
            return JsonResponse({"status": 400, "message": "Something went wrong!! Like - {ex}."})
