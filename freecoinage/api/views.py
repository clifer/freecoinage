from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from freecoinage.coins.models import Market
from api.serializers import marketSerializer


@api_view(['GET', 'POST'])
def market_list(request):
    """
    List all markets, or create a new market.
    """
    if request.method == 'GET':
        markets = Market.objects.all()
        serializer = marketSerializer(markets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = marketSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def market_detail(request, pk):
    """
    Get, udpate, or delete a specific market
    """
    try:
        market = Market.objects.get(pk=pk)
    except Market.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = marketSerializer(market)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = marketSerializer(market, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        market.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
