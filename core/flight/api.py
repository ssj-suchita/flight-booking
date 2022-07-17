from django.http import JsonResponse

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.exceptions import NotFound
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status

from core.flight.models import FlightDetails
from core.flight.serializers import FlightDetailsSerializer, FlightsListSerializer
from core.helper.api_paginator import ApiCustomPagination


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def flights_list(request):
    """
    List of All Flights Available across
    """
    data = request.query_params.copy()
    filter_fields = ['flight_number', 'source', 'destination', 'price', ]
    
    request_data = FlightsListSerializer(data=data)
    if not request_data.is_valid():
        return JsonResponse(request_data.errors, status=400)

    ordering = ['departure_date_time']
    if 'ordering' in data:
        ordering = data['ordering'].split(',')

    try:
        paginator = ApiCustomPagination()
        paginator.page_size = request_data['p_size'].value
        filter_params = prepare_search_filter_params(data, filter_fields)
        if filter_params:
            flight_objects = FlightDetails.objects.filter(**filter_params).order_by(*ordering)
        else:
            flight_objects = FlightDetails.objects.order_by(*ordering)
        result_page = paginator.paginate_queryset(flight_objects, request)
        serializer = FlightDetailsSerializer(result_page, many=True)
    except FlightDetails.DoesNotExist:
        return Response({'message': 'The flights details does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if flight_objects:
        return paginator.get_paginated_response(serializer.data)
    else:
        raise NotFound({"Info": "No flights details added yet?"}, status.HTTP_404_NOT_FOUND)


def prepare_search_filter_params(request, allowed_keys):
    """
    Prepare dictionary for given params
    """
    filters = {}
    for param in allowed_keys:
        if param in request:
            if request[param] != '':
                filters[param] = request[param]
    return filters
