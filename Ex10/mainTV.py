from tv import tv
canal = int(input("Canal:"))
if canal >=21:
    print("canal inválido!")
volume = int(input("Volume:"))
if volume >=100:
    print("Volume inválido!")

tvv = tv(canal,volume)
    
tvv.mostrar()

novoCanal = int(input("Novo Canal:"))
if canal >=21:
    print("canal inválido!")
novoVolume = int(input("Novo Volume:"))
if volume >=100:
    print("Volume inválido!")
        
tvv = tv(novoCanal,novoVolume)

tvv.mostrar()
