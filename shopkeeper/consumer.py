import pika
import json
from main import Shop,Order,db

params = pika.URLParameters('amqps://oeldbxyy:JI3gcG7Ts9o0uSQcq4AO4Ar1bYH-c9sC@dingo.rmq.cloudamqp.com/oeldbxyy') #자신의 메시지 브로커의 AMOQ URL을 넣어주면 된다

connection = pika.BlockingConnection(params) # rabbitMQ를 연결하기 위한 함수

channel = connection.channel() # connection을 연결해주기 위해 접근 경로를 생성함

channel.queue_declare(queue='shopkeeper') #  큐를 생성해 준다.


def callback(ch,method,properties,body):   # producer의 값을 가지고 오면 출력하는 callback 함수
    data = json.loads(body)
    print(data)
    if properties.content_type == 'shop:create method':
        shop = Shop(id=data['id'], name=data['name'],shop_address=data['shop_address'])
        db.session.add(shop)
        db.session.commit()

    elif properties.content_type == 'shop:update method':
        shop = Shop.query.get(data['id'])
        shop.shop_name = data['name']
        shop.shop_address = data['shop_address']
        db.session.commit()

    elif properties.content_type == 'shop:delete method':
        shop = Shop.query.get(data)
        db.session.delete(shop)
        db.session.commit()

    elif properties.content_type == 'order:create method':
        order = Order(id=data['id'], shop=data['shop'], address=data['home_address'])
        db.session.add(order)
        db.session.commit()

    elif properties.content_type == 'order:update method':
        order = Order.query.get(data['id'])
        order.shop = data['shop']
        order.address = data['home_address']
        db.session.commit()

    elif properties.content_type == 'order:delete method':
        order = Order.query.get(data)
        db.session.delete(order)
        db.session.commit()

channel.basic_consume(queue='shopkeeper',on_message_callback=callback, auto_ack=True)  # order의 정보만 받겠다(queue) 그리고 이 메시지를 받았을 때 어떤 함수를 실행 시킬 거냐(on_message_callback) 컨슘 선언
#auto_ack는 전에 했던 로그들은 처리해준다
channel.start_consuming() #consume 실행
 
channel.close() #컨슘 끝내라