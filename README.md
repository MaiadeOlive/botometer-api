## Como usar essa api

### Pré-requisitos I

Você precisa criar uma aplicação no Twitter para consumir a API.

1. Acesse a url: https://developer.twitter.com/en/apps
2. Crie um novo appicativo
3. Selecione o motivo de uso
4. Confirme suas informações  e anote seu usuário da conta desenvolvedor: @_your_user
5. Informe o País que você mora e como gostaria de ser chamado e em seguida clique em Próximo
6. Preencha os dados solicitados
7. Após a aprovação vá para aba "Chaves e Tokens"

### Pré-requisitos II

1. Instalar o pip use esse comando ``` sudo apt install python3-pip ``` 
2. Criar a seguinte variável de ambiente ``` export PATH="/home/<user>/.local/bin:$PATH" ```
3. Executar o seguinte comando para instalar o pipenv ```sudo -H pip3 install -U pipenv``` 

### Para subir a aplicação

1. Execute o seguinte comando ```pipenv install``` no diretório raiz desse projeto
2. Para habilitar o ambiente virtual do python ```pipenv shell```
3. Para subir o servidor execute ```python app.py```

### Para consumir a API

1. Informe as credenciais do **Bootometer** e do **Tweeter**
2. Informe os usuários separados por "," com ou sem **@**

### Obtendo o arquivo com os  dados do bootometer

1. Clique no link para baixar o arquivo. 
