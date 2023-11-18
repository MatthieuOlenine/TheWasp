import WaspService

Service = WaspService.Service()

Service.AtributResponse()
Service.AtributWallet()

watched = Service.GetWatched()
normed = Service.GetNormed()
pointer = Service.GetPointer()
spotwallet = Service.GetSpotWallet()

print('\nMarket TheWasp is looking at :\n')
for a in watched:
    print(f"{watched[watched.index(a)][0]}: {watched[watched.index(a)][1]}")
print('\ncurrent prices of devices\n')
for b in normed:
    print(f"{normed[normed.index(b)][0]}: {normed[normed.index(b)][1]} USDT")
print('\nWallet pointed by TheWasp :\n')
for c in spotwallet:
    print(f"{spotwallet[spotwallet.index(c)][0]}: {spotwallet[spotwallet.index(c)][1]} -> {spotwallet[spotwallet.index(c)][2]} USDT")
print(f"\nWallet to transfer -> {pointer[0]}: {pointer[1]} -> {pointer[2]} USDT\n")
