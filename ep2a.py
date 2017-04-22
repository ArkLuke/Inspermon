import time
import random
Insperdex=dict()
Insperdex={"Pikachu":{"poder":20,"vida":100,"defesa":7,"xpatual":0,"xpevol":0,"xp2":25,"proxevol":""},	
		   "Bulbasaur":{"poder":25,"vida":100,"defesa":8,"xpatual":0,"xpevol":1,"xp2":20,"proxevol":"Ivysaur"},
		   "Squirtle":{"poder":25,"vida":100,"defesa":8,"xpatual":0,"xpevol":1,"xp2":20,"proxevol":"Wartortle"},
		   "Charmander":{"poder":25,"vida":100,"defesa":8,"xpatual":0,"xpevol":1,"xp2":20,"proxevol":"Charmeleon"},
		   "Ivysaur":{"poder":30,"vida":110,"defesa":9,"xpatual":0,"xpevol":1,"xp2":20,"proxevol":"Venusaur"},
		   "Wartortle":{"poder":30,"vida":110,"defesa":9,"xpatual":0,"xpevol":1,"xp2":20,"proxevol":"Blastoise"},
		   "Charmeleon":{"poder":30,"vida":110,"defesa":9,"xpatual":0,"xpevol":1,"xp2":20,"proxevol":"Charizard"},
		   "Venusaur":{"poder":35,"vida":120,"defesa":10,"xpatual":0,"xpevol":0,"xp2":30,"proxevol":""},
		   "Blastoise":{"poder":35,"vida":120,"defesa":10,"xpatual":0,"xpevol":0,"xp2":30,"proxevol":""},
		   "Charizard":{"poder":35,"vida":120,"defesa":10,"xpatual":0,"xpevol":0,"xp2":30,"proxevol":""},
		   "Abra":{"poder":20,"vida":80,"defesa":5,"xpatual":0,"xpevol":0,"xp2":15,"proxevol":""},
		   "Tentacool":{"poder":15,"vida":60,"defesa":5,"xpatual":0,"xpevol":0,"xp2":10,"proxevol":""},
		   "Geodude":{"poder":20,"vida":70,"defesa":6,"xpatual":0,"xpevol":0,"xp2":15,"proxevol":""},
		   "Onix":{"poder":15,"vida":80,"defesa":9,"xpatual":0,"xpevol":0,"xp2":25,"proxevol":""},
		   "Horsea":{"poder":15,"vida":60,"defesa":5,"xpatual":0,"xpevol":0,"xp2":15,"proxevol":""},
		   "Zubat":{"poder":15,"vida":50,"defesa":5,"xpatual":0,"xpevol":0,"xp2":10,"proxevol":""}}
		   
Computador=[]

probbilidadefuga1 = [0,1,2,3,4,5,6,7,8,9,10]

#FUNÇÃO RETORNA UM NÚMERO ALEATÓRIO NUMA DISTRIBUIÇÃO NORMAL CENTRADA EM NUM
def distnormal(num):
		lisnum=[1.5,
				1.4,1.4,
				1.3,1.3,1.3,
				1.2,1.2,1.2,1.2,
				1.1,1.1,1.1,1.1,1.1,
				1.0,1.0,1.0,1.0,1.0,1.0,
				0.9,0.9,0.9,0.9,0.9,
				0.8,0.8,0.8,0.8,
				0.7,0.7,0.7,
				0.6,0.6,
				0.5]
		return(int(num*random.choice(list(lisnum))))

#FUNÇÃO DE ATAQUE
def ataca(atacante,defensor):
	ataque = distnormal(Insperdex[atacante]["poder"])
	defesa = distnormal(Insperdex[defensor]["defesa"])
	if ataque > defesa:
			Insperdex[defensor]["vida"]=Insperdex[defensor]["vida"]-((ataque-defesa))
			if Insperdex[defensor]["vida"] < 0:
				Insperdex[defensor]["vida"] = 0	

#FUNÇÂO DE EVOLUÇÂO
def evolucao(inspermon):
	if Insperdex[inspermon]["xpevol"] > 0 :
		if Insperdex[inspermon]["xpatual"] >= Insperdex[inspermon]["xpevol"]:
			print("Seu pokemon evoluiu para " + Insperdex[inspermon]["proxevol"])
			return Insperdex[inspermon]["proxevol"]

#MAIN CODE		   
print("Bem vindo ao Inspermon")
time.sleep(0.5)

print("Carregando o jogo...") 
time.sleep(1.5)

#ESCOLHA DE INSPERMON
while True:
	usuario=str(input("Escolha seu Inspermon: Bulbasaur(1), Charmander(2), Squirtle(3):"))
	if usuario == "1":
		usuario = "Bulbasaur"
	if usuario == "2":
		usuario = "Charmander"
	if usuario == "3":
		usuario = "Squirtle"
	if usuario == "Charmander" or usuario == "Bulbasaur" or usuario == "Squirtle":
		Computador.append(usuario)
		print("Você escolheu o {}".format(usuario))
		break
	else:
		print("Escolha um Inspermon válido")
		
		
#COMANDO INICIAL PASSEAR/DORMIR/COMPUTADOR
while True:
	x=random.choice(list(Insperdex.keys()))
	y=random.choice(list(probbilidadefuga1))
	a = input("Você deseja passear, dormir, ver seu computador ou restaurar a vida do seu Inspermon?")
	if a == "dormir":
		print("Você encerrou o jogo, salvando...")
		time.sleep(1)
		print("Jogo salvo. Até a proxima!")
		exit()
	if a == "computador":
		print(Computador)
	if a =="restaurar":
		print("A vida do seu Inspermon foi restaurada!")

	if a == "passear":
		print("Passeando...")
		time.sleep(1)
		print("Aaah...Você encontrou um {} selvagem.".format(x))
		Computador.append(x)

				
	#INICIO BATALHA	
		b= input("Deseja batalhar ou fugir?")
		if b =="fugir":
			if y < 5:
				print("Você fugiu da batalha com sucesso")
					
			if y >= 5:
				print("Fuga mal sucedida!")
				b="batalhar"
				
		if b == "batalhar":
			print("Iniciando batalha...")
			time.sleep(1)
			print("Inspermon : {}".format(x))
			print("poder = {}".format(Insperdex[x]["poder"]))
			print("vida = {}".format(Insperdex[x]["vida"]))
			print("defesa = {}".format(Insperdex[x]["defesa"]))
			c= input("Voce deseja atacar ou fugir?")
			if c == "fugir":
				if y < 5:
					print("Você fugiu da batalha com sucesso")
			
				if y >= 5:
					print("Fuga mal sucedida, VOCÊ TERÁ que batalhar!")
				
			elif c == "atacar":
				while Insperdex[x]["vida"]>0 and Insperdex[usuario]["vida"]>0:
						
					ataca(usuario,x)
					ataca(x,usuario)			

					print("Vida do seu Inspermon:{}".format(Insperdex[usuario]["vida"]))
					print("vida do oponente:{}".format(Insperdex[x]["vida"]))
					time.sleep(1)
					if Insperdex[x]["vida"]<=0:
						print("Parabens!Voce ganhou a batalha")
						print("Vida do seu Inspermon = {}".format(Insperdex[usuario]["vida"]))
						print("XP ganho = {}".format(Insperdex[usuario]["xpatual"]+Insperdex[x]["xp2"]))
						usuario = evolucao(usuario)
						
					Insperdex[usuario]["vida"]=Insperdex[usuario]["vida"]-(Insperdex[x]["poder"]-Insperdex[usuario]["defesa"])
					if Insperdex[usuario]["vida"]<=0:
						print("Voce perdeu a batalha")
						time.sleep(1)
						print("Retornando ao InsperCenter para recuperar seu Inspermon...")
						time.sleep(1)
						print("A vida do seu Inspermon foi restaurada!")


"""COISAS QUE FALTAM:
→ FUNCIONALIDADE 1: FEITA
→ FUNCIONALIDADE 2: FEITA
→ FUNCIONALIDADE 3: FEITA
→ FUNCIONALIDADE 4:	Evolução
→ FUNCIONALIDADE 5: Salvar jogo"""