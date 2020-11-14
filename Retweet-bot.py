# Retweet-bot para Twitter, usando Python y Tweepy.
# Búsqueda mediante hashtag o palabra clave.

import tweepy
from time import sleep

# Importa claves y tokens secretos de tu aplicación de Twitter.
# Asegúrese de que su archivo keys.py se encuentre en el mismo directorio que este archivo.

from keys import keys

consumer_key = keys['consumer_key']
consumer_key_secret = keys['consumer_key_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Donde q='#example', cambie #example a cualquier hashtag o palabra clave que desee buscar.
# De items(5), cambie 5 a la cantidad de retweets que desea twittear.
# Asegúrese de leer las reglas de Twitter sobre automatización, ¡no haga spam!

for tweet in tweepy.Cursor(api.search, q='#example').items(5):
    try:
        print('\nRetweet-Bot encontro tweet de @' + tweet.user.screen_name + '. ' + 'Intentando retweet.')

        tweet.retweet()
        print('Retweet publicado con éxito.')

        # De sleep(10), se mide en segundos.
        # Cambie 10 a la cantidad de segundos que desea tener entre retweets.
        # Lea las reglas de Twitter sobre automatización. ¡No spam!
        sleep(10)

     # Errores básicos. Imprimirá el error al retweet.
    except tweepy.TweepError as error:
        print('\nError. Retweet no exitoso. Razón: ')
        print(error.reason)

    except StopIteration:
        break
