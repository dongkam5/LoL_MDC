from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import getTier as tier
from . import getInGame as ingame
from . import 승률 as odds
from django.db.models import Q

class getTier(APIView):
    def get(self, request, format=None):
        summoner_name = request.query_params.get('summoner_name', None)
        if summoner_name is not None:
            api_key = models.Riot.objects.get().api_key
            summoner_tier = tier.getTier(api_key,summoner_name)
            response_data = {}
            response_data['tier'] = summoner_tier
            return Response(data=response_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class getRate(APIView):
    def get(self, request, format=None):
        summoner_name = request.query_params.get('summoner_name', None)
        if summoner_name is not None:
            api_key = models.Riot.objects.get().api_key
            summoner_rate = odds.getOdds(api_key,summoner_name)
            response_data = {}
            response_data['rate'] = summoner_rate
            return Response(data=response_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class getIngame(APIView):
    def get(self, request, format=None):
        summoner_name = request.query_params.get('summoner_name', None)
        if summoner_name is not None:
            api_key = models.Riot.objects.get().api_key
            summoner_ingame = ingame.getIngame(api_key,summoner_name)
            response_data = {}
            response_data['ingame'] = summoner_ingame
            return Response(data=response_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)