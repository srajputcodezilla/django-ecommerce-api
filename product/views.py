from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import *

from .serializers import *
class ProductApiView(APIView):
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    # serializer_class = ProductSerializer
    # create product ---
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    # get by id and get all ---
    def get(self, request, id=None):
        params=request.query_params.get('format', None)
        if id:
            try:
                products = Product.objects.get(id=id)
                response = ProductSerializer(products, many=False).data
            except Product.DoesNotExist:
                return Response({'message':'product does not exist'})
        else:
            products = Product.objects.all()
            response = ProductSerializer(products, many=True).data            
        return Response(response)
    def delete(self, request, id):
        try:
            category = Product.objects.get(id=id)
            category.delete()
            return Response({'message': 'Product deleted successfully'})
        except Product.DoesNotExist:
            return Response({'message': 'Product does not exist'})
        
    def put(self, request, id):
        try:
            category = Product.objects.get(id=id)
            serializer = ProductSerializer(category, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Product updated successfully'})
            return Response(serializer.errors)
        except Product.DoesNotExist:
            return Response({'message': 'Product does not exist'})
class ProductByCategoryApiView(APIView):
    # get product by category ---
    def get(self, request, id=None):
        params=request.query_params.get('format', None)
        if id:
            try:
                products = Product.objects.filter(category=id)
                response = ProductSerializer(products, many=True).data
            except Product.DoesNotExist:
                return Response({'message':'product does not exist'})
        # else:
        #     products = Product.objects.all()
        #     response = ProductSerializer(products, many=True).data            
        return Response(response)
    
class CategoryApiView(APIView):
    # create category ---
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    
    
    # get category all and by id ---
    def get(self, request, id=None):
        params=request.query_params.get('format', None)
        if id:
            try:
                category = Category.objects.get(category_id=id)
                response = CategorySerializer(category, many=False).data
            except Category.DoesNotExist:
                return Response({'message':'category does not exist'})
        else:
            category = Category.objects.all()
            response = CategorySerializer(category, many=True).data            
        return Response(response)
    def delete(self, request, id):
        try:
            category = Category.objects.get(category_id=id)
            category.delete()
            return Response({'message': 'Category deleted successfully'})
        except Category.DoesNotExist:
            return Response({'message': 'Category does not exist'})
        
    def put(self, request, id):
        try:
            category = Category.objects.get(category_id=1)
            serializer = CategorySerializer(category, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Category updated successfully'})
            return Response(serializer.errors)
        except Category.DoesNotExist:
            return Response({'message': 'Category does not exist'})
        
class ProductDetailsApiView(APIView):
     def get(self, request, id=None):
        params=request.query_params.get('format', None)
        if id:
            try:
                product_detailsS=ProductDetail.objects.get(product_id=id)
                productS=Product.objects.get(id=id)
                product_details =ProductDetailsSerializer(product_detailsS, many=False).data 
                product=ProductSerializer(productS, many=False).data 
                response = {
                    "name":product_details['product_name'],
                    "product":product_details['product_id'],
                    "images":product_details['image_url'],
                    "available_stocke":product['avilable_qnt'],
                    "price":product_details['price'],
                    "description":product_details['description'],
                    "discount":product['discount'],
                    "discount_type":product['discount_type'],
                    "vender":""
                }
            except ProductDetail.DoesNotExist:
                return Response({'message':'product does not exist'})
        # else:
        #     products = Product.objects.all()
        #     response = ProductSerializer(products, many=True).data            
        return Response(response)
     
class CreateProductDetailsApiView(APIView):
     
     def post(self, request):
        print(request.data)
        serializer = ProductDetailsSerializer(data=request.data)
        print('\n', serializer , '\n')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
     
    
