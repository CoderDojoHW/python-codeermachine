#!/usr/local/bin/python3

alfabet = 'abcdefghijklmnopqrstuvwxyz'

nieuwBericht = ''
  
bericht = input('Voer een gecodeerde bericht in: ')

sleutel = input('Geef een sleutel (1-26): ')
sleutel = int(sleutel)

for teken in bericht:
  if teken in alfabet:
    positie = alfabet.find(teken)
    nieuwePositie = (positie - sleutel) % 26
    nieuwTeken = alfabet[nieuwePositie]
    nieuwBericht += nieuwTeken
  else:
    nieuwBericht += teken

print('Het bericht is: ', nieuwBericht)