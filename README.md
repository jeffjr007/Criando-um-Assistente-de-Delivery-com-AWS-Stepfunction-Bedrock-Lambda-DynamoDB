# AWS Delivery Workflow

Este projeto implementa um fluxo para processar pedidos de um aplicativo de delivery usando AWS Step Functions, Lambdas, DynamoDB e SNS. Ele segue a seguinte estrutura:

1. Registro do pedido no banco de dados.
2. Envio de notificações ao cliente e restaurante.
3. Gerenciamento do status do pedido.

## Tecnologias Utilizadas
- **AWS Step Functions** para orquestrar o fluxo de trabalho.
- **AWS Lambda** para execução de tarefas individuais.
- **DynamoDB** para armazenar o histórico de pedidos.
- **SNS** para enviar notificações push.

## Estrutura
- `step-functions/`: Contém a definição da máquina de estado.
- `lambdas/`: Código-fonte das funções Lambda.
- `dynamodb/`: Configuração da tabela do DynamoDB.
- `sns/`: Tópicos de notificações.

## Como Executar
1. Configure as permissões IAM necessárias para Lambda, DynamoDB, e SNS.
2. Suba o código das Lambdas.
3. Importe a máquina de estado no AWS Step Functions.
4. Configure os recursos DynamoDB e SNS.

## Licença
Este projeto está licenciado sob [MIT License](LICENSE).
