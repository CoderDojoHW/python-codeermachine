#!/usr/local/bin/python3

alfabet = 'abcdefghijklmnopqrstuvwxyz'

nieuwBericht = ''
  
bericht = input('Voer een gecodeerde bericht in: ')

for sleutel in range(26):
  nieuwBericht = ''

  for teken in bericht:
    if teken in alfabet:
      positie = alfabet.find(teken)
      nieuwePositie = (positie - sleutel) % 26
      nieuwTeken = alfabet[nieuwePositie]
      nieuwBericht += nieuwTeken
    else:
      nieuwBericht += teken

  print(f'Sleutel ({sleutel}): ', nieuwBericht)