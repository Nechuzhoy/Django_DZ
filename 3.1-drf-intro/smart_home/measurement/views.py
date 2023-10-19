from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response

from .models import Measurement, Sensor
from .serializers import SensorListSerializer, SensorDetailSerializer, MeasurementSerializer


class CreateAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        review = SensorDetailSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response({'status': 'Успех!'})


class ListCreateAPIView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        review = MeasurementSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response({'status': 'Успех!'})


class RetrieveUpdateAPIView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        serializer = SensorDetailSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class ListSensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer
