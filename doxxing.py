import os
from colorama import Fore

while True:
  print('')
  print(f'''
   ___      _       _  _____           _ 
  / _ \ ___(_)_ __ | ||_   _|__   ___ | |
 | | | / __| | '_ \| __|| |/ _ \ / _ \| |
 | |_| \__ \ | | | | |_ | | (_) | (_) | |
  \___/|___/_|_| |_|\__||_|\___/ \___/|_|
                                          
                          #Almigthy                              ''')

  print('')


  print(f'           ' + '   [1] Name & state'+ f'{Fore.WHITE}     ')
  print(f'           ' + '   [2] Phone Number'+ f'{Fore.WHITE}       ' )
  print(f'           ' + '   [3] Address' + f'{Fore.WHITE}            ')
  print(f'          ' + '    [4] IP' + f'{Fore.WHITE}                 ')
  print('')
  print('')
  menu = input(f'~> ')

  if menu == "1":
    firstname = input("[Question?] What is their first name? > ")
    lastname = input("[Question?] What is their last name? > ")
    state = input("[Question?] What City, State, or Zip do they live in? >")
    print(f"[Clear] https://www.fastpeoplesearch.com/name/{firstname}-{lastname}_{state}\nhttps://www.whitepages.com/name/{firstname}-{lastname}/{state}?fs=1&searchedName={firstname}%20{lastname}&searchedLocation={state}")

  elif menu == "2":
    first = input("[Question?] What is the first 3 digits? > ")
    middle = input("[Question?] What is the next 3 digits? > ")
    last = input("[Question?] What is the last 4 digits? > ")
    print(f"[Clear] https://www.fastpeoplesearch.com/{first}-{middle}-{last}\nhttps://www.whitepages.com/phone/1-{first}-{middle}-{last}")

  elif menu == "3":
    house = input("[Question?] What's the house number?")
    street = input("[Question?] Street? > ")
    city = input("[Question?] City? > ")
    state = input("[Question?] State? > ")
    print(f"[Clear] https://www.fastpeoplesearch.com/address/{house}-{street}_{city}-{state}")

  elif menu == "4":
    ip = input("[Question?] IP? > ")
    print(f"[Clear] https://www.geolocation.com/?languageCode=en_US&ip={ip}#ipresult")

