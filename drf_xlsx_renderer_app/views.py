from django.contrib.auth.models import User
from rest_framework import permissions
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from drf_renderer_xlsx.renderers import XLSXRenderer
from drf_renderer_xlsx.mixins import XLSXFileMixin


class UserView(APIView):
    """
    API endpoint that allows users to be viewed.
    """
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [JSONRenderer, XLSXRenderer, XLSXFileMixin]

    @staticmethod
    def get(request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


