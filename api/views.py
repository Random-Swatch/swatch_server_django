# Create your views here.
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.serializers import ColorSerializer
from api.swatch_generator import SwatchGenerator


class SwatchView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        serializer = ColorSerializer(SwatchGenerator().generate(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    queryset = ''
