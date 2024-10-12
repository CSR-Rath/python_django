from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apiApp.models import Product
from apiApp.serializer import ProductSerializer


@api_view(["GET"])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(data={
        "response": {
            "status": 200,
            "message": "Products found",
        },
        "results": serializer.data,
    }, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({
            "response": {
                "status": 404,
                "message": "Product not found."
            }
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def post_product(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "response": {
                "status": 201,
                "message": "Product successfully created!",
                "product": serializer.data
            },
        }, status=status.HTTP_201_CREATED)

    return Response({
        "response": {
            "status": 400,
            "message": serializer.errors
        }
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def put_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({
            "response": {
                "status": 404,
                "message": "Product not found."
            }
        }, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "response": {
                "status": 200,
                "message": "Product successfully updated!",
                "product": serializer.data
            },
        }, status=status.HTTP_200_OK)

    return Response({
        "response": {
            "status": 400,
            "message": serializer.errors
        }
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return Response(data={
            "response": {
                "status": 204,
                "message": "Product successfully deleted!"
            },
        }, status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return Response({
            "response": {
                "status": 404,
                "message": "Product not found."
            }
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def filter_products(request):
    products = Product.objects.all()

    # Filter by ID if provided
    product_id = request.query_params.get('id')
    if product_id:
        products = products.filter(id=product_id)

    # Filter by name if provided
    product_name = request.query_params.get('name')
    if product_name:
        products = products.filter(name__icontains=product_name)

    # Check if products were found
    if not products.exists():
        return Response(data={
            "response": {
                "status": 404,
                "message": "No products found matching the criteria."
            }
        }, status=status.HTTP_404_NOT_FOUND)

    # Serialize the filtered products
    serializer = ProductSerializer(products, many=True)

    return Response(data={
        "response": {
            "status": 200,
            "message": "Products retrieved successfully",
        },
        "results": serializer.data,
    }, status=status.HTTP_200_OK)
#
# def filter_products(request):
#     products = Product.objects.all()
#
#     # Filter by ID if provided
#     product_id = request.query_params.get('id')
#     if product_id:
#         products = products.filter(id=product_id)
#
#     # Filter by name if provided
#     product_name = request.query_params.get('name')
#     if product_name:
#         products = products.filter(name__icontains=product_name)
#
#     # Serialize the filtered products
#     serializer = ProductSerializer(products, many=True)
#
#     return Response(data={
#         "response": {
#             "status": 200,
#             "message": "Products retrieved successfully",
#         },
#         "results": serializer.data,
#     }, status=status.HTTP_200_OK)