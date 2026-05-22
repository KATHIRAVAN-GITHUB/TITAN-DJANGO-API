from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .services import ProductCardService
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_products(request):
    products = ProductCardService.get_all_products()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product_by_id(request, id):
    product = ProductCardService.get_product_by_id(id)

    if product:
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        product = ProductCardService.save_product(serializer.validated_data)
        return Response(ProductSerializer(product).data, status=201)

    return Response(serializer.errors, status=400)