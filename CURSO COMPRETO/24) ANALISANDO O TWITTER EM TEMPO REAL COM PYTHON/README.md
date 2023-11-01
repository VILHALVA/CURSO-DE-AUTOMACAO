# ANALISANDO O TWITTER EM TEMPO REAL COM PYTHON
Para analisar o Twitter em tempo real com Python, você pode usar a API do Twitter para coletar tweets em tempo real e bibliotecas de processamento de dados, como Tweepy e TextBlob, para analisar os tweets. Abaixo, vou mostrar os passos para configurar a coleta de tweets e realizar análises simples de sentimentos em tempo real.

**Passo 1: Configurar a Conta do Desenvolvedor no Twitter**

Antes de começar, você precisa criar uma conta de desenvolvedor no Twitter e criar um aplicativo para obter as credenciais de API, incluindo a chave de acesso (API key), a chave secreta de acesso (API secret key), o token de acesso (Access token), e o token secreto de acesso (Access token secret). Isso permite que você acesse a API do Twitter.

**Passo 2: Instalar Bibliotecas**

Você deve instalar as bibliotecas Tweepy e TextBlob. Use o seguinte comando para instalar essas bibliotecas:

```bash
pip install tweepy textblob
```

**Passo 3: Escrever o Código Python**

Aqui está um exemplo de código Python que coleta tweets em tempo real com base em uma palavra-chave e realiza análises de sentimentos simples usando o TextBlob:

```python
import tweepy
from textblob import TextBlob

# Configurações da API do Twitter
consumer_key = 'SUA_API_KEY'
consumer_secret = 'SUA_API_SECRET_KEY'
access_token = 'SEU_ACCESS_TOKEN'
access_token_secret = 'SEU_ACCESS_TOKEN_SECRET'

# Autenticação com a API do Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Criar um objeto API
api = tweepy.API(auth)

# Palavra-chave para buscar tweets em tempo real
palavra_chave = "Python"

# Coletar tweets em tempo real
tweets = api.search(q=palavra_chave, count=10)

for tweet in tweets:
    print(f'Texto do Tweet: {tweet.text}')
    analysis = TextBlob(tweet.text)

    # Análise de sentimento
    if analysis.sentiment.polarity > 0:
        sentimento = "positivo"
    elif analysis.sentiment.polarity == 0:
        sentimento = "neutro"
    else:
        sentimento = "negativo"

    print(f'Sentimento: {sentimento}')
    print('---')
```

Certifique-se de substituir as variáveis `SUA_API_KEY`, `SUA_API_SECRET_KEY`, `SEU_ACCESS_TOKEN` e `SEU_ACCESS_TOKEN_SECRET` pelas credenciais que você obteve ao criar seu aplicativo no Twitter.

Este código faz o seguinte:

1. Autentica-se com a API do Twitter usando Tweepy.
2. Define uma palavra-chave para buscar tweets em tempo real.
3. Coleta os tweets em tempo real que correspondem à palavra-chave.
4. Realiza uma análise de sentimentos simples para cada tweet usando o TextBlob.

Você pode personalizar e aprimorar as análises conforme necessário. Além disso, é importante observar que a API do Twitter tem limitações em relação à quantidade de tweets que você pode coletar em tempo real. Certifique-se de revisar as políticas da API do Twitter para entender as restrições.