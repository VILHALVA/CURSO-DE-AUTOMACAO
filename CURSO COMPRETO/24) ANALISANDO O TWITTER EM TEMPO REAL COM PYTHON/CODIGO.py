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
