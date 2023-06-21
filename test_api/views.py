from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TestView(APIView):
    def get(self, request, *args, **kwargs):  
        result = {"name":"test"}
        return Response({'status': 'success', "students":result}, status=200)  
    def post(self, request): 
        print(request.data)
        if(request.data=="ts"):
            return Response({"status": "success", "data": "valid"}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": "inValid"}, status=status.HTTP_400_BAD_REQUEST)  




