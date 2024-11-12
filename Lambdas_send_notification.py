import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    cliente_topic = "arn:aws:sns:REGION:ACCOUNT_ID:ClienteNotificacoes"
    restaurante_topic = "arn:aws:sns:REGION:ACCOUNT_ID:RestauranteNotificacoes"
    
    mensagem = f"Pedido {event['pedido_id']} foi recebido e está sendo processado."
    
    sns.publish(TopicArn=cliente_topic, Message=mensagem)
    sns.publish(TopicArn=restaurante_topic, Message=mensagem)
    
    return {"status": "success"}
