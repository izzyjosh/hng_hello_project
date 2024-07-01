from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.conf import settings
from rest_framework import status

def get_city(ip_address):
    ipinfo_token = settings.IPINFO_API_TOKEN
    url = f"https://ipinfo.io/{ip_address}?token={ipinfo_token}"
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data.get("city")
        else:
            return None
    except requests.RequestException:
        print("request failed")
        return none

def get_temperature(city):
    openwhether_api_key = settings.OPENWHETHER_API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openwhether_api_key}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('main', {}).get('temp')
        else:
            return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None


class Hello(APIView):

    def get(self,request,format=None):
        visitor_name = request.GET.get("visitor_name")
        ipaddr = request.META.get("REMOTE_ADDR")
        city = get_city(ipaddr)
        temperature = get_temperature(city)

        response = {
                "client_ip":f"{ipaddr}",
                "location": f"{city}",
                "greeting":f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celcius in {city}",
                }
        return Response(response,status=status.HTTP_200_OK)

