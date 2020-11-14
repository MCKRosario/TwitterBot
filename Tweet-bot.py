# Tweet-bot para Twitter, usando Python y Tweepy.
# Twittea texto e imágenes directamente desde la terminal.

import os
import tweepy

# Importa claves y tokens secretos de tu aplicación de Twitter.
# Asegúrese de que su archivo keys.py se encuentre en el mismo directorio que este archivo.

from keys import keys

try:
    input = raw_input
except NameError:
    pass

def getStatus():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    status = '\n'.join(lines)
    return status

def tweetthis(type):
    if type == "Texto":
        print("\nTu Tweet " + user.name)
        tweet = getStatus()
        try:
            api.update_status(tweet)
        except Exception as e:
            print(e)
            return
    elif type == "Foto":
        print("Nombre y extensión de la Foto ejm:(pic.jpg) " + user.name)
        pic = os.path.abspath(input())
        print("Título Foto " + user.name)
        title = getStatus()
        try:
            api.update_with_media(pic, status=title)
        except Exception as e:
            print(e)
            return

    print("Tweet publicado con éxito !!!")


def initialize():
    global api, auth, user
    consumer_key = keys['consumer_key']
    consumer_key_secret = keys['consumer_key_secret']
    access_token = keys['access_token']
    access_token_secret = keys['access_token_secret']

    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    user = api.me()

def main():
    doit = int(input("\n1. Tweet\n2. Tweet + Foto\n\n"))
    initialize()
    if doit == 1:
        tweetthis("Texto")
    elif doit == 2:
        tweetthis("Foto")
    else:
        print("OK, Inténtalo de Nuevo !!")
        main()

main()
