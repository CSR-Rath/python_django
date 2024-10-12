from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apiApp.models import Category
from apiApp.serializer import CategorySerializer


def startup(request):
    return HttpResponse("Hello world!")


@api_view(["GET"])
def home(request):
    return Response({
        "status": 200,
        "message": "Welcome to APIApp!"
    })


@api_view(["GET"])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(data={
        "response": {
            "status": 200,
            "message": "Categories found",
        },
        "results": serializer.data,
    }, status=status.HTTP_200_OK)


# Get a single category by ID
@api_view(["GET"])
def get_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        serializer = CategorySerializer(category)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Category.DoesNotExist:
        return Response({
            "response": {
                "status": 404,
                "message": "Category not found."
            }
        }, status=status.HTTP_404_NOT_FOUND)


# Create a new category
@api_view(["POST"])
def post_category(request):
    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "response": {
                "status": 201,
                "message": "Category successfully created!",
                "category": serializer.data
            },
        }, status=status.HTTP_201_CREATED)

    return Response({
        "response": {
            "status": 400,
            "message": serializer.errors
        }
    }, status=status.HTTP_400_BAD_REQUEST)


# Update a category by ID
@api_view(["PUT"])
def put_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response({
            "response": {
                "status": 404,
                "message": "Category not found."
            }
        }, status=status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializer(category, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "response": {
                "status": 200,
                "message": "Category successfully updated!",
                "category": serializer.data
            },
        }, status=status.HTTP_200_OK)

    return Response({
        "response": {
            "status": 400,
            "message": serializer.errors
        }
    }, status=status.HTTP_400_BAD_REQUEST)


# Delete a category by ID
@api_view(["DELETE"])
def delete_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        category.delete()
        return Response(data={
            "response": {
                "status": 204,
                "message": "Category successfully deleted!"
            },
        }, status=status.HTTP_204_NO_CONTENT)
    except Category.DoesNotExist:
        return Response({
            "response": {
                "status": 404,
                "message": "Category not found."
            }
        }, status=status.HTTP_404_NOT_FOUND)
