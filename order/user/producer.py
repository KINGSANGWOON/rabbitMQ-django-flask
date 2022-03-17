import pika
import json

params = pika.URLParameters('amqps://oeldbxyy:JI3gcG7Ts9o0uSQcq4AO4Ar1bYH-c9sC@dingo.rmq.cloudamqp.com/oeldbxyy') #자신의 메시지 브로커의 AMOQ URL을 넣어주면 된다

connection = pika.BlockingConnection(params) # rabbitMQ를 연결하기 위한 함수

channel = connection.channel() # connection을 연결해주기 위해 접근 경로를 생성함

def publish(method,body):  #  이 함수는 producer과 같은 역할이다 즉 어떤 메시지를 보낼지를 정한다
    propertie = pika.BasicProperties(method)
    channel.basic_publish(exchange= '',routing_key='shopkeeper',body=json.dumps(body),properties=propertie)  #basic_puclish 함수는 가장 기초적인 정보만 제공하겠다는 것이다 routing_key:바인딩할 queue(저장할 대상), body:대상에 전달할 메시지
    # producer는 exchange에 보내는 것이다
    # python 의 개체를 json 문자열로 반환해주기 위해서는 dumps 함수가 필요하다


