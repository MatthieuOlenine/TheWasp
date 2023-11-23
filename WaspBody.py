import WaspService
from time import sleep
 
latency = 1                                     # 'latency' correspond au temps que dure une itération en minute (must be 'int')
RUNNING = True
PREVENTFIRSTTRADE = True
Service = WaspService.Service()                 # Donne accès au service de TheWasp

while RUNNING:

    Service.LogIn()                             # connexion necessaire pour mettre à jour les datas
    Service.AtributResponse()                   # charge les données du marché et les trie dans 'Watched' et 'Normed' en conservant la dernière itération
    Service.CompareMarket()                     # compare les dernières données du market avec la dernière itération
    Service.AtributWallet()                     # charge les donnée du portefeuille et localise le wallet avec les fonds : 'pointer'

    winner = Service.GetWinner()                # transfere le nom du marché avec la plus haute perf dans 'winner'
    normed = Service.GetNormed()                # transfere les dernières données de 'Normed' dans 'normed'
    pointer = Service.GetPointer()              # transfere les données de 'Pointer' dans 'pointer'
    spotwallet = Service.GetSpotWallet()        # transfere les données de 'SpotWallet' dans 'spotwallet'

<<<<<<< HEAD
    if not PREVENTFIRSTTRADE:
        print('________________________\n\ncurrent prices of devices\n')
        for b in normed:
            print(f"{normed[normed.index(b)][0]}: {normed[normed.index(b)][1]} USDT")
        print('\nWallet pointed by TheWasp :\n')
        for c in spotwallet:
            print(f"{spotwallet[spotwallet.index(c)][0]}: {spotwallet[spotwallet.index(c)][1]} -> {spotwallet[spotwallet.index(c)][2]} USDT")
        print(f"\nWallet to transfer -> {pointer[0]}: {pointer[1]} -> {pointer[2]} USDT")
        print(f"Destination wallet -> {winner[0]}: ↑ de {winner[1]*-1} pts")
        
        if winner[0] != pointer[0]:
            if winner[0][:-4] != pointer[0]:
                Service.ApplyConvert(pointer, winner)   # applique la transaction si il y en a une
                print(f"\n    ----------> {pointer[1]} {pointer[0]} converted to {winner[0][:-4]} <----------")
    else:
        PREVENTFIRSTTRADE = False

    for d in range(0, latency):
        sleep(60)               
    
    print(f"________________________\n\n{latency} min passed")
=======
    Service.ApplyConvert(pointer, winner)       # donne l'ordre de faire la transaction

    if winner[0] != pointer[0][:-4]:
        Service.ApplyConvert(pointer, winner)   # applique la transaction si il y en a une

    print('\ncurrent prices of devices\n')
    for b in normed:
        print(f"{normed[normed.index(b)][0]}: {normed[normed.index(b)][1]} USDT")
    print('\nWallet pointed by TheWasp :\n')
    for c in spotwallet:
        print(f"{spotwallet[spotwallet.index(c)][0]}: {spotwallet[spotwallet.index(c)][1]} -> {spotwallet[spotwallet.index(c)][2]} USDT")
    print(f"\nWallet to transfer -> {pointer[0]}: {pointer[1]} -> {pointer[2]} USDT")
    print(f"Destination wallet -> {winner[0]}: ↑ de {winner[1]*-1} pts\n________________________")

    sleep(60)
>>>>>>> a45212d4778f5cf1e8897df93fc58db9bfa2cbbd
