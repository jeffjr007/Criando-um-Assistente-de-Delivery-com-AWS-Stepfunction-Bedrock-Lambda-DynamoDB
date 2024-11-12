import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Pedidos')

def lambda_handler(event, context):
    pedido_id = event["pedido_id"]
    status = event["status"]  
    
    table.update_item(
        Key={"id": pedido_id},
        UpdateExpression="SET #status = :status",
        ExpressionAttributeNames={"#status": "status"},
        ExpressionAttributeValues={":status": status}
    )
    
    return {"status": "success", "pedido_id": pedido_id, "novo_status": status}
