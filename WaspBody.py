import WaspService
from time import sleep
 
RUNNING = True
Service = WaspService.Service()         # Donne accès au service de TheWasp

while RUNNING:

    Service.LogIn()                         # connexion necessaire pour mettre à jour les datas
    Service.AtributResponse()               # charge les données du marché et les trie dans 'Watched' et 'Normed' en conservant la dernière itération
    Service.CompareMarket()                 # compare les dernières données du market avec la dernière itération
    Service.AtributWallet()                 # charge les donnée du portefeuille et localise le wallet avec les fonds : 'pointer'

    winner = Service.GetWinner()            # transfere le nom du marché avec la plus haute perf dans 'winner'
    normed = Service.GetNormed()            # transfere les dernières données de 'Normed' dans 'normed'
    pointer = Service.GetPointer()          # transfere les données de 'Pointer' dans 'pointer'
    spotwallet = Service.GetSpotWallet()    # transfere les données de 'SpotWallet' dans 'spotwallet'

    print('\ncurrent prices of devices\n')
    for b in normed:
        print(f"{normed[normed.index(b)][0]}: {normed[normed.index(b)][1]} USDT")
    print('\nWallet pointed by TheWasp :\n')
    for c in spotwallet:
        print(f"{spotwallet[spotwallet.index(c)][0]}: {spotwallet[spotwallet.index(c)][1]} -> {spotwallet[spotwallet.index(c)][2]} USDT")
    print(f"\nWallet to transfer -> {pointer[0]}: {pointer[1]} -> {pointer[2]} USDT")
    print(f"Destination wallet -> {winner[0]}: ↑ de {winner[1]*-1} pts\n________________________")

    sleep(60)