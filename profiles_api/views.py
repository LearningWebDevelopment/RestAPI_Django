from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View
    """

    def get(self, request, format=None):
        """Returns a list of API Views features
        """
        an_apiview = [
            'Uses Http methods as functions (get, post, patch, delete)',
            'Is similar to traditional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!',
                         'an_apiview': an_apiview})
