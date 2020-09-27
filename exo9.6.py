from random import *


# ETAPE 1
def crypter_char(char, decalage):
    actuel = ord(char)
    actuel += decalage
    return chr(actuel)


# ETAPE 2
def decrypter_char(char, decalage):
    actuel = ord(char)
    actuel -= decalage
    return chr(actuel)


# ETAPE 3
def crypter_phrase(phrase, decalage):
    nouvelle_phrase = ""
    for lettre in phrase:
        nouvelle_phrase += crypter_char(lettre, decalage)
    return nouvelle_phrase


# ETAPE 4
def decrypter_phrase(phrase, decalage):
    nouvelle_phrase = ""
    for lettre in phrase:
        nouvelle_phrase += decrypter_char(lettre, decalage)
    return nouvelle_phrase


# ETAPE 5
def cryptage(element):
    decalage = randrange(1, 10)
    phrase = crypter_phrase(element, decalage)
    return chr(decalage) + phrase


# ETAPE 6
def decryptage(element):
    decalage = ord(element[0])
    phrase = element[1:]
    return decrypter_phrase(phrase, decalage)


# ETAPE 7
def main():
    reponse = str(input('Voulez-vous crypter ou decrypter: '))
    while (reponse.lower() != 'crypter' and reponse.lower() != 'decrypter'):
        reponse = str(input('Voulez-vous crypter ou decrypter: '))

    if (reponse.lower() == 'crypter'):
        element = str(input('Element à crypter: '))
        print('Element crypter: ', cryptage(element))
    else:
        element = str(input('Element à decrypter: '))
        print('Element décrypter: ', decryptage(element))


# ETAPE 8
reponse = "rien"  # pour rentrer dans le while
while (reponse.lower() != 'non'):
    main()
    reponse = str(input('\nVoulez-vous recommencer? '))   
