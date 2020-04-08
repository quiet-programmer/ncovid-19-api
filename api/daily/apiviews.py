from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Daily
from .serializers import DailySerializer


class DailyList(APIView):
    @staticmethod
    def get(request):
        daily = Daily.objects.all()
        data = DailySerializer(daily, many=True).data
        return Response(data)


class DailyDetail(APIView):
    @staticmethod
    def get(request, date):
        state = get_object_or_404(Daily, pk=date)
        data = DailySerializer(state).data
        return Response(data)
