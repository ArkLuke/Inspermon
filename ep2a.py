import time
import random
import json
import math
Insperdex=dict()
Insperdex={"Pikachu":{"poder":20,"vida_inicial":100,"vida":100,"defesa":7,"xpatual":0,"xpevol":0,"xp2":25,"proxevol":""},	
		   "Bulbasaur":{"poder":25,"vida_inicial":100,"vida":100,"defesa":8,"xpatual":0,"xpevol":50,"xp2":20,"proxevol":"Ivysaur"},
		   "Squirtle":{"poder":25,"vida_inicial":100,"vida":100,"defesa":8,"xpatual":0,"xpevol":50,"xp2":20,"proxevol":"Wartortle"},
		   "Charmander":{"poder":25,"vida_inicial":100,"vida":100,"defesa":8,"xpatual":0,"xpevol":50,"xp2":20,"proxevol":"Charmeleon"},
		   "Ivysaur":{"poder":30,"vida_inicial":110,"vida":110,"defesa":9,"xpatual":0,"xpevol":100,"xp2":20,"proxevol":"Venusaur"},
		   "Wartortle":{"poder":30,"vida_inicial":110,"vida":110,"defesa":9,"xpatual":0,"xpevol":100,"xp2":20,"proxevol":"Blastoise"},
		   "Charmeleon":{"poder":30,"vida_inicial":110,"vida":110,"defesa":9,"xpatual":0,"xpevol":100,"xp2":20,"proxevol":"Charizard"},
		   "Venusaur":{"poder":35,"vida_inicial":120,"vida":120,"defesa":10,"xpatual":0,"xpevol":0,"xp2":30,"proxevol":""},
		   "Blastoise":{"poder":35,"vida_inicial":120,"vida":120,"defesa":10,"xpatual":0,"xpevol":0,"xp2":30,"proxevol":""},
		   "Charizard":{"poder":35,"vida_inicial":120,"vida":120,"defesa":10,"xpatual":0,"xpevol":0,"xp2":30,"proxevol":""},
		   "Abra":{"poder":20,"vida_inicial":80,"vida":80,"defesa":5,"xpatual":0,"xpevol":0,"xp2":15,"proxevol":""},
		   "Tentacool":{"poder":15,"vida_inicial":60,"vida":60,"defesa":5,"xpatual":0,"xpevol":0,"xp2":10,"proxevol":""},
		   "Geodude":{"poder":20,"vida_inicial":70,"vida":70,"defesa":6,"xpatual":0,"xpevol":0,"xp2":15,"proxevol":""},
		   "Onix":{"poder":15,"vida_inicial":80,"vida":80,"defesa":9,"xpatual":0,"xpevol":0,"xp2":25,"proxevol":""},
		   "Horsea":{"poder":15,"vida_inicial":60,"vida":60,"defesa":5,"xpatual":0,"xpevol":0,"xp2":15,"proxevol":""},
		   "Zubat":{"poder":15,"vida_inicial":50,"vida":50,"defesa":5,"xpatual":0,"xpevol":0,"xp2":10,"proxevol":""},
		   "Caterpie":{"poder":15,"vida_inicial":50,"vida":50,"defesa":5,"xpatual":0,"xpevol":0,"xp2":10,"proxevol":""},
		   "Weedle":{"poder":15,"vida_inicial":50,"vida":50,"defesa":5,"xpatual":0,"xpevol":0,"xp2":10,"proxevol":""},
		   "Pidgey":{"poder":20,"vida_inicial":50,"vida":50,"defesa":5,"xpatual":0,"xpevol":0,"xp2":15,"proxevol":""},
		   "Ratata":{"poder":15,"vida_inicial":50,"vida":50,"defesa":5,"xpatual":0,"xpevol":0,"xp2":10,"proxevol":""},
		   "Ekans":{"poder":15,"vida_inicial":65,"vida":65,"defesa":5,"xpatual":0,"xpevol":0,"xp2":15,"proxevol":""},
	       "Spearow":{"poder":25,"vida_inicial":55,"vida":55,"defesa":5,"xpatual":0,"xpevol":0,"xp2":10,"proxevol":""},	
	       "Nidoran":{"poder":20,"vida_inicial":60,"vida":60,"defesa":5,"xpatual":0,"xpevol":0,"xp2":20,"proxevol":""},
		   "Vulpix":{"poder":15,"vida_inicial":60,"vida":60,"defesa":7,"xpatual":0,"xpevol":0,"xp2":20,"proxevol":""},
		   "Oddish":{"poder":15,"vida_inicial":50,"vida":50,"defesa":5,"xpatual":0,"xpevol":0,"xp2":10,"proxevol":""}}
		   
lista_de_vidas = []
for i in Insperdex:
	lista_de_vidas.append(int(Insperdex[i]["vida_inicial"]))

Computador = []
Capturados = []


probabilidadefuga1 = [0,1,2,3,4,5,6,7,8,9,10]

#FUNÇÃO RETORNA UM NÚMERO ALEATÓRIO NUMA DISTRIBUIÇÃO NORMAL CENTRADA EM NUM PARA SORTEAR FORÇA DE ATAQUE E DEFESA
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
			time.sleep(0.5)
			print("O que está acontecendo?")
			for i in range(3):
				time.sleep(0.5)
				print("?")
			print("Seu inspermon está evoluindo!!!")
			for i in range(5):	
				time.sleep(0.5)
				print(".")
				
			print("Parabéns!!! Seu "+inspermon+" acaba de evoluir para " + Insperdex[inspermon]["proxevol"])
			return (Insperdex[inspermon]["proxevol"])
	return inspermon

#FUNÇÃO DE CAPTURA
def tenta_capturar(inspermon):
	vida = Insperdex[inspermon]["vida_inicial"]
	vida_maior = max(lista_de_vidas)
	vida_menor = min(lista_de_vidas)
	Pa = 0.02   # Chance de captura do Inspemron com MAIS vida (Padrão : 0.02 = 2%) 
	Pb = 0.8    # Chance de captura do Inspemron com MENOS vida (Padrão : 0.8 = 80%)
	B = (vida_menor - vida_maior)/math.log(Pa/Pb)
	#  print(B)
	A = Pa/math.exp(-vida_maior/B)
	#  print(A)
	probabilidade = A*math.exp(-vida/B)
	variavel = random.random()
	return  variavel < probabilidade


#MAIN CODE		   
print("Bem vindo ao Inspermon")
time.sleep(0.5)

#CARREGAR JOGO
while True:
	jogo = str(input("Deseja começar um Novo Jogo(1) ou carregar um Jogo Salvo(2)?"))
	if jogo == "1" or jogo == "novo":
		data = {
				"insperdex": 
						{"inspermons": []},
				"seuinspermon":
						{"nome": "", "vida": 0, "xpatual": 0}
				}
			
		#ESCOLHA POKEMON (NOVO JOGO)
		while True:
			time.sleep(1.5)
			usuario=str(input("Escolha seu Inspermon: Bulbasaur(1), Charmander(2), Squirtle(3)"))
			if usuario == "1":
				usuario = "Bulbasaur"
			if usuario == "2":
				usuario = "Charmander"
			if usuario == "3":
				usuario = "Squirtle"
			if usuario == "Charmander" or usuario == "Bulbasaur" or usuario == "Squirtle":
				Computador.append(usuario)
				time.sleep(1)
				print("Você escolheu o {}".format(usuario))
				break
			else:
				print("Escolha um Inspermon válido")
		break
	if jogo == "2" or jogo == "salvo":
		with open("savegame.json", "r") as savegame:
			data = json.load(savegame)
		Computador = data["insperdex"]["inspermons"]
		Capturados = data["insperdex"]["capturados"]
		usuario = data["seuinspermon"]["nome"]
		Insperdex[usuario]["xpatual"] = data["seuinspermon"]["xpatual"]
		time.sleep(1)
		print("Seu Inspermon é o {} e ele está com {}/{} de vida e {} de XP!".format(usuario,Insperdex[usuario]["vida"],Insperdex[usuario]["vida_inicial"],Insperdex[usuario]["xpatual"]))
		break

print("Carregando o jogo...") 
time.sleep(1.5)
		
#COMANDO INICIAL PASSEAR/DORMIR/COMPUTADOR
while True:
	x=random.choice(list(Insperdex.keys()))
	y=random.choice(list(probabilidadefuga1))
	Insperdex[x]["vida"] = Insperdex[x]["vida_inicial"]
	a = input("Você deseja passear, dormir, ver seu computador ou restaurar a vida do seu Inspermon?")
	if a == "dormir":
		print("Você encerrou o jogo, salvando...")
		time.sleep(1)
		data["insperdex"]["capturados"] = Capturados
		data["insperdex"]["inspermons"] = Computador
		data["seuinspermon"]["nome"] = usuario
		data["seuinspermon"]["xpatual"] = Insperdex[usuario]["xpatual"]
		data["seuinspermon"]["vida"] = Insperdex[usuario]["vida"]
		with open('savegame.json', 'w') as savegame:
			json.dump(data, savegame)
		print("Jogo salvo. Até a proxima!")
		exit()
	if a == "computador":
		time.sleep(1)
		print("Acessando seus dados...")
		time.sleep(2)
		d = input("Você está no seu computador, deseja ver os seus Inspermons capturados(1) ou sua Insperdex(2)?")
		if d =="insperdex" or d =="2":
			time.sleep(1)
			print("Sua Insperdex possuí: {}" .format(Computador))
			time.sleep(2)
		if d =="capturados" or d =="1":
			time.sleep(1)
			print("Você já capturou: {}".format(Capturados))
			time.sleep(2)
	if a =="restaurar":
		Insperdex[usuario]["vida"] = Insperdex[usuario]["vida_inicial"]
		print(".")
		time.sleep(0.5)
		print(".")
		time.sleep(0.5)
		print(".")
		time.sleep(0.5)
		print("A vida do seu Inspermon foi restaurada!")
		print("Seu Inspermon está com {} de vida".format(Insperdex[usuario]["vida"]))
	if a == "passear":
		print("Passeando...")
		time.sleep(1)
		print("Aaah...Você encontrou um {} selvagem.".format(x))
		if x not in Computador:
			Computador.append(x)
	

				
	#INICIO BATALHA	
		b= input("Deseja batalhar ou fugir?")
		if b =="fugir":
			if y < 7:
				print("Você fugiu da batalha com sucesso")
					
			if y >= 10:
				print("Fuga mal sucedida!")
				b="batalhar"
				
		
		if b == "batalhar":
			print("Iniciando batalha...")
			time.sleep(1)
			print("Inspermon : {}".format(x))
			print("poder = {}".format(Insperdex[x]["poder"]))
			print("vida = {}".format(Insperdex[x]["vida"]))
			print("defesa = {}".format(Insperdex[x]["defesa"]))
			c= input("Voce deseja atacar, tentar capturar o Inspermon ou fugir?")
			if c == "fugir":
				if y < 7:
					print("Você fugiu da batalha com sucesso")
			
				if y >= 7:
					print("Fuga mal sucedida, VOCÊ TERÁ que batalhar!")
					c="atacar"	

			if c == "capturar":
				if(x in Capturados):
					print("Você já capturou um Inspermon deste tipo antes!")
					continue
				else:
					print("Você lançou uma InsperBola para tentar capturar o " + x + " selvagem ...")
					time.sleep(1)
					print(".")
					time.sleep(1)
					print(".")
					time.sleep(1)
					print(".")
					if (tenta_capturar(x)):
						Capturados.append(x)
						time.sleep(1)
						print("Parabéns, você capturou o {} com sucesso!".format(x))
						time.sleep(1)
						print("Agora o Inspermon capturado pode ser encontrado no seu computador")
						time.sleep(1)

					else:
						print("Infelizmente o " + x + " selvagem resistiu à InsperBola e fugiu !")
						time.sleep(1)




				"""if(True):
					Capturados.append(x)
					print(".")
					time.sleep(1)
					print(".")
					time.sleep(1)
					print(".")
					time.sleep(1)
					print("Parabéns, você capturou o {} com sucesso!".format(x))
					time.sleep(1)"""


			if c == "atacar":
				while Insperdex[x]["vida"]>0 and Insperdex[usuario]["vida"]>0:
						
					ataca(usuario,x)
					ataca(x,usuario)			

					print("Vida do seu Inspermon:{}".format(Insperdex[usuario]["vida"]))
					print("vida do oponente:{}".format(Insperdex[x]["vida"]))
					time.sleep(1)
					
					if Insperdex[x]["vida"]<=0:
						print("Parabens!Voce ganhou a batalha")
						print("Vida do seu Inspermon = {}".format(Insperdex[usuario]["vida"]))
						print("XP ganho = {}".format(Insperdex[x]["xp2"]))
						Insperdex[usuario]["xpatual"] += Insperdex[x]["xp2"]
						print("Seu Inspermon agora tem {} de experiência" .format(Insperdex[usuario]["xpatual"]))
						if Insperdex[usuario]["xpevol"] > 0:
							usuario = evolucao(usuario)
						time.sleep(2)

					elif Insperdex[usuario]["vida"]<=0:
						print("Voce perdeu a batalha")
						time.sleep(1)
						print("Retornando ao InsperCenter para recuperar seu Inspermon...")
						Insperdex[usuario]["vida"] = Insperdex[usuario]["vida_inicial"]
						time.sleep(1)
						print(".")
						time.sleep(0.5)
						print(".")
						time.sleep(0.5)
						print(".")
						time.sleep(0.5)
						print("A vida do seu Inspermon foi restaurada!")
						time.sleep(2)
						break

