from itsdangerous import Serializer
from rest_framework import viewsets
from rest_framework import status
from .models import Shop, Order
from .serializers import ShopSerializer, OrderSerializer
from rest_framework.response import Response
from .producer import publish

class ShopViewSet(viewsets.ViewSet): 
    def list(self, request):                              #get 방식 /shop
        shops = Shop.objects.all()    # 모든 값을 불러와라
        serializer = ShopSerializer(shops, many=True)  #many=True 나열하라는 뜻이다 (즉 여러 값을 출력시 정렬할 때 사용함)
        return Response(serializer.data)    


    def create(self, request):                            #post 방식 /shop
        serializer = ShopSerializer(data=request.data)   # request.data는 우리가 인썸니아 같은 걸로 데이터를 넣어줄 때 그 데이터를 의미한다
        serializer.is_valid(raise_exception=True)   #json 형식이 module에 맞지 않을 때 error을 보내는 역할임
        serializer.save()  # 받은 데이터를 저장함
        publish('shop:create method',serializer.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED) # 잘 실행이 되었을 경우 status 200을 띄워줌


    def update(self, request, pk=None):                            #put 방식  /shop/<str:idx>
        shops = Shop.objects.get(id=pk)
        serializer = ShopSerializer(instance= shops, data=request.data)  # 해당 pk(instance) 에 data를 request.data로 change 해줘라
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('shop:update method',serializer.data)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)


    def retrieve(self, request, pk=None):
        shops = Shop.objects.all(id=pk)   #pk 값과 일치하는 id db를 가지고 온다
        serializer = Serializer(shops)
        return Response(serializer.data)                        #get방식 /shop/<str:idx>      이건 특정한 값을 보는 것이다
         

    def destroy(self, request, pk=None):                          #delete 방식 /shop/<str:idx>
        shops = Shop.objects.all(id=pk)
        shops.delete()
        publish('shop:delete method',pk)
        return Response(status=status.HTTP_204_NO_CONTENT)




class OrderViewSet(viewsets.ViewSet): 
    def list(self, request):                              #get 방식 /order                
        orders = Order.objects.all()   
        serializer = OrderSerializer(orders, many=True)  
        return Response(serializer.data)  

    def create(self, request):                            #post 방식 /order
        serializer = OrderSerializer(data=request.data)   
        serializer.is_valid(raise_exception=True)   
        serializer.save()  
        publish('order:create method',serializer.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):                            #put 방식  /order/<str:idx>
        order = Order.objects(pk=id)
        serializer = OrderSerializer(instance=order, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('order:update method',serializer.data)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

    
    def retrieve(self, request, pk=None):                         #get방식 /order/<str:idx>
        order = Order.objects(pk=id)
        serializer = OrderSerializer(order)
        return Response(serializer.data) 

    def destroy(self, request, pk=None):                          #delete 방식 /order/<str:idx>
        order = Order.objects(ok=id)
        order.delete()
        publish('order:delete method',pk)
        return Response(status.HTTP_204_NO_CONTENT)            