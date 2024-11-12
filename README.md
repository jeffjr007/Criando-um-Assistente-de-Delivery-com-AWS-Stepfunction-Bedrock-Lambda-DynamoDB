# 🚀 AWS Delivery Workflow  

Este projeto implementa um fluxo para processar pedidos de um aplicativo de delivery utilizando **AWS Step Functions**, **Lambdas**, **DynamoDB** e **SNS**. Ele segue a seguinte estrutura:

1️⃣ **Registro do pedido** no banco de dados.  
2️⃣ **Envio de notificações** ao cliente e restaurante.  
3️⃣ **Gerenciamento do status do pedido**.  

---

## 🛠️ Tecnologias Utilizadas  
- **⚙️ AWS Step Functions**: Orquestração do fluxo de trabalho.  
- **💻 AWS Lambda**: Execução de tarefas individuais.  
- **🗂️ DynamoDB**: Armazenamento do histórico de pedidos.  
- **📢 SNS**: Envio de notificações push.

---

## 📂 Estrutura do Projeto  

- 📁 `step-functions/`: Definição da máquina de estado.  
- 📁 `lambdas/`: Código-fonte das funções Lambda.  
- 📁 `dynamodb/`: Configuração da tabela DynamoDB.  
- 📁 `sns/`: Tópicos de notificações.

---

## 🛠️ Como Executar  

1. 🔑 **Configure as permissões IAM** necessárias para Lambda, DynamoDB e SNS.  
2. ⬆️ **Suba o código** das funções Lambda.  
3. 🔄 **Implemente a máquina de estado** no AWS Step Functions.  
4. ⚙️ **Configure os recursos DynamoDB e SNS** com as definições fornecidas.  

---

## 📜 Licença  

Este projeto está licenciado sob a [MIT License](LICENSE).  
