import boto3
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Pedidos')

def lambda_handler(event, context):
    pedido = {
        "id": event["pedido_id"],
        "usuario": event["usuario_id"],
        "itens": event["itens"],
        "data": str(datetime.datetime.now()),
        "status": "recebido"
    }
    table.put_item(Item=pedido)
    return {"status": "success", "pedido_id": event["pedido_id"]}
