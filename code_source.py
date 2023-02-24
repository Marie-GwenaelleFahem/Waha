from random import randint
from time import sleep

# Personnage

class personnage:
    def __init__ (self,nom,vie,attaque_legere,attaque_moyenne,attaque_lourde,endurance,demarcation,armes,essence):
        self.nom = nom
        self.vie = int(vie)
        self.attaque_legere = int(attaque_legere)
        self.attaque_moyenne = int(attaque_moyenne)
        self.attaque_lourde = int(attaque_lourde)
        self.stamina = int(endurance)
        self.demarcation = int(demarcation)
        self.armes = armes
        self.essence = essence
    
    def soin() :
      A = inventaire["Rations d'eau"]
      if A > 0 :
        if survivor.vie >= 76 :
          survivor.vie = 100
          inventaire["Rations d'eau"] -= 1
          print("Vous avez désormais", survivor.vie,"pv")
          sleep(1.5)
          print("Il vous reste ",inventaire["Rations d'eau"],"Rations d'eau") 
        else :
          inventaire["Rations d'eau"] -= 1
          survivor.vie += 50 
          print("Vous avez désormais", survivor.vie,"pv")
          print("Il vous reste ",inventaire["Rations d'eau"],"Rations d'eau")      
      else : 
        print("Vous avez consommé toutes vos rations d'eau")

    def endurance():
      A = inventaire["Rations de nourriture"]
      if A > 0 : 
        if survivor.stamina >= 26 :
          inventaire["Rations de nourriture"] -= 1
          survivor.stamina = 50 
          print("Votre endurance est égale à ",survivor.stamina)
          print("Il vous reste ",inventaire["Rations de nourriture"],"rations de nourriture")
        else : 
          inventaire["Rations de nourriture"] -= 1
          survivor.stamina += 25 
          print("Votre endurance est égale à ",survivor.stamina)
          print("Il vous reste ",inventaire["Rations de nourriture"],"rations de nourriture")
      else : 
        print("Vous avez consommé toutes vos rations de nourriture")

    def essence() :   
      A = inventaire["Bidons d'essence"]
      if A > 0 : 
        inventaire["Bidons d'essence"] -= 1
        survivor.essence += 1
        print("Vous avez désormais",survivor.essence,"litres d'essences")
        print("Il vous reste ",inventaire["Bidons d'essence"],"bidons d'essences")
      else : 
        print("Vous n'avez plus de bidons d'essences")
    
    def reservoire(survivor):
      if survivor.essence > 0 :
        survivor.essence -=1
      else:
        print("Vous n'avez plus d'essence, votre periple s'arrête ici")
        Menu()
    
    def fight(nom_ennemi):
      B = nom_ennemi.demarcation
      while nom_ennemi.vie > 0 and  B > 0 :
        print("Vous avez",survivor.stamina,"d'endurance.")
        print("Que voulez-vous faire ?")
        print("1. Attaquer")
        print("2. Se soigner")
        print("3. Restaurer son endurance")
        choice = input()
        while choice != "1" and choice != "2" and choice != "3" :
          print("Erreur")
          print("Vous avez",survivor.stamina,"d'endurance.")
          print("Que voulez-vous faire ?")
          print("1. Attaquer")
          print("2. Se soigner")
          print("3. Restaurer son endurance")
          choice = input()
        if choice == "1" :
          print("Vous attaquez")
          personnage.attack_player(nom_ennemi,survivor.armes["arme 1"],survivor.armes["arme 2"])
        if choice == "2" :
          print("Vous vous soignez")
          personnage.soin()
          print("Vous avez",survivor.vie," HP")
          personnage.attack_ennemy(nom_ennemi)
        if choice == "3" :
          print("Vous vous régénérez")
          personnage.endurance()
          print("Vous avez désormais",survivor.stamina," d'endurance")
          personnage.attack_ennemy(nom_ennemi)
  
  
      if survivor.vie <= 0 :
        print("Vous êtes mort !! :(")
        Menu()
      
      if survivor.vie >= 0 :
        print("Vous avez survécu au combat !! :)")
        if B == 3 :
          survivor.vie = 100
          current_position_advertising()
        else :
          current_position_advertising()

    def arme_usage(nom_arme,nom_ennemi):
      print("Choissisez une attaque à utiliser avec le",nom_arme["nom"])
      print("1. Attaque legère")
      print("2. Attaque moyenne")
      choice = int(input())
      while choice != 1 and choice != 2 : 
        print("Erreur")
        print("Choissisez une attaque à utiliser avec le knout")
        print("1. Attaque legère")
        print("2. Attaque moyenne")
        choice = int(input())
      if choice == 1 and survivor.stamina >= 3 : 
        print("Vous lancez une attaque légère avec votre",nom_arme["nom"])
        nom_ennemi.vie -= nom_arme["leger"]
        survivor.stamina -= 3
        if nom_ennemi.vie > 0 : 
            print("Il reste", nom_ennemi.vie," HP à votre ennemi !")
            print("")
            personnage.attack_ennemy(nom_ennemi)
        else : 
          print("Vous avez tué l'ennemi !!")
          print("Il vous reste", survivor.vie," HP")
      elif choice == 1 and survivor.stamina < 3 :
        print("Vous n'avez pas assez d'endurance pour effectuer cette attaque")
        print("Pour effectuer une nouvelle attaque, vous devez restaurer votre endurance !")
        personnage.attack_ennemy(nom_ennemi)
      if choice == 2 and survivor.stamina >= 6 : 
        print("Vous lancez une attaque moyenne avec votre", nom_arme["nom"])
        nom_ennemi.vie -= nom_arme["moyen"]
        survivor.stamina -= 6
        if nom_ennemi.vie > 0 : 
            print("Il reste", nom_ennemi.vie," HP à votre ennemi !")
            print("")
            personnage.attack_ennemy(nom_ennemi)
        else : 
          print("Vous avez tué l'ennemi !!")
          print("Il vous reste", survivor.vie," HP")
      elif choice == 2 and survivor.stamina < 6 : 
        print("Vous n'avez pas assez d'endurance pour effectuer cette attaque")
        print("Pour effectuer une nouvelle attaque, vous devez restaurer votre endurance !")
        personnage.attack_ennemy(nom_ennemi)


  
    def attack_player(nom_ennemi,nom_arme1, nom_arme2):
      print("Quelle arme voulez-vous utiliser ?")
      print("1. Le ",nom_arme1["nom"])
      print("2. Le ",nom_arme2["nom"])
      choice = int(input())
      while choice != 1 and choice != 2 :
        print("Quelle arme voulez-vous utiliser ?")
        print("1. Le ",nom_arme1["nom"])
        print("2. Le ",nom_arme2["nom"])
        choice = int(input())
      if choice == 1 : 
        personnage.arme_usage(nom_arme1,nom_ennemi)
      if choice == 2 : 
        personnage.arme_usage(nom_arme2,nom_ennemi)
      

    def attack_ennemy(nom_ennemi):
      if nom_ennemi.demarcation == 1 :
        print("Vous subissez une attaque légère !!")
        print("")
        survivor.vie -= nom_ennemi.attaque_legere
        if survivor.vie > 0 :
          print("Il vous reste",survivor.vie,"HP")
          print("")
        else :
          print("Vous n'avez plus de vie...")
          Menu()
          

      if nom_ennemi.demarcation == 2 :
        num = randint(1,3)
        if num == 1 or num == 2 :
          print("Vous subissez une attaque légère !!")
          print("")
          survivor.vie -= nom_ennemi.attaque_legere
          if survivor.vie > 0 :
            print("Il vous reste",survivor.vie," HP")
            print("")
          else :
            print("Vous n'avez plus de vie...")
            Menu()

        else : 
          print("Vous subissez une attaque moyenne !!")
          print("")
          survivor.vie -= nom_ennemi.attaque_moyenne
          if survivor.vie > 0 :
            print("Il vous reste",survivor.vie,"HP")
            print("")
          else : 
            print("Vous n'avez plus de vie...")
            Menu()
        
      if nom_ennemi.demarcation == 3 :
        num = randint(1,5)
        if num == 1 or num == 2 :
          print("Vous subissez une attaque légère !!")
          print("")
          survivor.vie -= nom_ennemi.attaque_legere
          if survivor.vie > 0 :
              print("Il vous reste",survivor.vie," HP")
              print("")
          else :
            print("Vous n'avez plus de vie...")
            Menu()      
        elif num == 3 or num == 4 :
          print("Vous subissez une attaque moyenne !!")
          print("")
          survivor.vie -= nom_ennemi.attaque_moyenne
          if survivor.vie > 0 :
            print("Il vous reste",survivor.vie,"HP")
            print("")
          else : 
            print("Vous n'avez plus de vie...")
            Menu()
        else : 
          print("Vous subissez une attaque lourde !!")
          print("")
          survivor.vie -= nom_ennemi.attaque_lourde
          if survivor.vie > 0 :
            print("Il vous reste",survivor.vie,"HP")
            print("")
          else : 
            print("Vous n'avez plus de vie...")
            Menu()

# Héros/Héroïne
survivor = personnage("",100,0,0,0,50,0,{"arme 1" : {"nom" : "knout", "leger" : 10, "moyen" : 15},"arme 2" : {"nom": "gun", "leger" : 15, "moyen": 25}},50)

# PNJ
gentil_pnj = personnage("Darla",0,0,0,0,0,0,0,0)  
mechant_pnj = personnage("Carter",0,0,0,0,0,0,0,0)


# Nix Patriam
lucius_vorenus = personnage("Lucius Vorenus",90,20,20,20,0,1,0,0)
aurelius_primo = personnage("Aurelius Primo",110,20,30,30,0,2,0,0)
imperator = personnage("Imperator",160,20,30,45,0,3,0,0)

# Desertus
dasht_e = personnage("Dasht-e",70,15,15,15,0,1,0,0)
gobi = personnage("Gobi",100,15,23,23,0,2,0,0)
karakoum = personnage("Karakoum",140,13,23,40,0,3,0,0)

# Le marais des Sombres Ecailles
madesi = personnage("Madesi",70,10,10,10,0,1,0,0)
meen_sa = personnage("Meen-Sa",100,10,20,20,0,2,0,0)
deekus = personnage("Deekus",120,10,20,36,0,3,0,0)

# Daintree
osleya = personnage("Osleya",110,25,25,25,0,1,0,0)
blodreina = personnage("Blodreina",130,25,35,35,0,2,0,0)
heda = personnage("Heda",180,25,35,49,0,3,0,0)

# Neo Polis
dum_dum = personnage("Dum Dum",50,5,5,5,0,1,0,0)
kurt = personnage("Kurt",80,5,15,15,0,2,0,0)
royce = personnage("Royce",100,5,15,30,0,3,0,0)


# Biomes

# Neo Polis (première zone)
def check_location_biome1():  

  global position
  global b
  global c
  global d
  global e
  global f
  global g
  global h
  B1 = map[4][4]
  B2 = map[5][4]
  B3 = map[5][3]
  C1 = map[1][3]
  C2 = map[2][3]
  C3 = map[3][3]
  D1 = map[1][6]
  D2 = map[2][6]
  D3 = map[3][6]
  D4 = map[4][6]
  D5 = map[5][6]
  D6 = map[6][6]
  E1 = map[2][2]
  E2 = map[6][2]
  F1 = map[5][5]
  F2 = map[6][4]
  G1 = map[2][5]
  G2 = map[3][5]
  H1 = map[4][2]
  H2 = map[5][2]


  if (position == B1 or position == B2 or position == B3) and b == False: 
    print("Il semblerait que vous ayez rencontré un ennemi")
    sleep(1.5)
    print("Dum-Dum : 'Mais qu’est-ce qu’on a là ! Un buggy en bon état…descend de là où je te bute !'")
    sleep(1.5)
    b = True
    personnage.fight(dum_dum)
  elif (position == C1 or position == C2 or position == C3) and c == False:
    print("Il semblerait que vous ayez rencontré un ennemi")
    sleep(1.5)
    print("Kurt : 'Tiens tiens, un(e) aventurier(e) perdu. Vide tes poches !'")
    sleep(1.5)
    c = True
    personnage.fight(kurt)
  elif position == D1 or position == D2 or position == D3 or position == D4 or position == D5 or position == D6 and d == False:
    print("Il semblerait que vous ayez rencontré un le boss de la zone")
    sleep(1.5)
    print("Royce : 'Crains ma puissance étranger(e), ton chemin s'arrête là !' ")
    sleep(1.5)
    d = True
    personnage.fight(royce)
  elif position == E1 and e == False: 
    print("Darla : 'Salut à toi jeune voyageur(se)'")
    sleep(1.5)
    print("Darla : 'Continue vers l'est et tu trouveras peut-être quelque chose d'intéressant'")
    sleep(1.5)
    e = True
    action()
  elif position == E2 and e == False:
    print("Darla : 'Salut à toi jeune voyageur(se)'")
    sleep(1.5)
    print("Darla : 'Continue vers l'ouest et tu trouveras peut-être quelque chose d'intéressant'")
    sleep(1.5)
    e = True
    action()
  elif (position == F1 or position == F2) and f == False:
    print("Quelle chance, vous venez de trouver un coffre !!")
    f = True
    event()
  elif (position == G1 or position == G2) and g == False: 
    print("Quelle chance, vous venez de trouver un coffre !!")
    g = True
    event()
  elif (position == H1 or position == H2) and h == False: 
    print("Quelle chance, vous venez de trouver un coffre !!")
    h = True
    event()
  elif y == 0 or x == 0 or x == 7 :
    print("Vous vous êtes perdu(e), des désosseurs vous ont tué alors que vous tentiez de les fuir...dommage")
    sleep(1.5)
    Menu()
  else : 
    print("Vous continuez à avancer dangereusement dans Néo Polis.")
    sleep(1.5)
    current_position_advertising()


# Le Marais des Sombres Ecailles (deuxième zone)
def check_location_biome2():

  global position
  global b
  global c
  global d
  global e
  global f
  global g
  global h
  B1 = map[3][2] # léger 
  B2 = map[4][2]
  B3 = map[5][2]
  C1 = map[3][4] # moyen
  C2 = map[2][4]
  C3 = map[2][5]
  D1 = map[1][6] #boss
  D2 = map[2][6]
  D3 = map[3][6]
  D4 = map[4][6]
  D5 = map[5][6]
  D6 = map[6][6]
  E1 = map[1][1] #coffre 1
  E2 = map[2][1]
  F1 = map[5][5] #coffre 2
  F2 = map[6][5]
  G1 = map[3][3] #coffre 3
  G2 = map[3][5]
  H1 = map[5][3] #pnj
  H2 = map[1][2]

  if (position == B1 or position == B2 or position == B3) and b == False: 
    print("Il semblerait que vous ayez rencontré un ennemi")
    sleep(1.5)
    print("Madesi : 'Ah ! Madesi sent qu’une proie est proche…'")
    sleep(1.5)
    b = True
    personnage.fight(madesi)
  elif (position == C1 or position == C2 or position == C3) and c == False:
    print("Il semblerait que vous ayez rencontré un ennemi")
    sleep(1.5)
    print("Meen-Sa : 'Meen-Sa voit à travers la brume…votre mort est proche étranger(e) !'")
    sleep(1.5)
    c = True
    personnage.fight(meen_sa)
  elif position == D1 or position == D2 or position == D3 or position == D4 or position == D5 or position == D6 and d == False :
    print("Il semblerait que vous ayez rencontré un le boss de la zone")
    sleep(1.5)
    print("Deekus : 'Deekus, je suis Deekus ! Chef des Sombres Ecailles. Vous vous êtes égaré(e)s ? Ahaha…Deekus n’aime pas ceux qui s’aventurent trop loin dans son marais. Vous allez mourir ahaha (rire maléfique)'")
    sleep(1.5)
    d = True
    personnage.fight(deekus)
  elif position == H1 and h == False:
    print("Carter : 'Salut à toi jeune voyageur(se)'")
    sleep(1.5)
    print("Carter: 'Continue vers le nord est où une récompense t'y attend")
    h = True
    action()
  elif position == H2 and h == False:
    print("Carter : 'Salut à toi jeune voyageur(se)'")
    sleep(1.5)
    print("Carter: 'Continue vers le nord ouest où une récompense t'y attend")
    h = True
    action()
  elif (position == F1 or position == F2) and f == False:
    print("Quelle chance, vous venez de trouver un coffre !!")
    f = True
    event()
  elif (position == G1 or position == G2) and g == False: 
    print("Quelle chance, vous venez de trouver un coffre !!")
    g = True
    event()
  elif (position == E1 or position == E2) and e == False: 
    print("Quelle chance, vous venez de trouver un coffre !!")
    e = True 
    event()
  elif y == 0 or x == 0 or x == 7 :
    print("Vous vous êtes perdu(e), vous êtes mort(e) dans d'atroces souffrances tué par le nuage toxique bordant le marais...dommage")
    sleep(1.5)
    Menu()
  else : 
    print("Vous continuez à avancer dangereusement dans le marais des Sombres Ecailles.")
    sleep(1.5)
    current_position_advertising()

# Desertus (troisième zone)
def check_location_biome3():

  global position
  global b
  global c
  global d
  global e
  global f
  global g
  global h
  B1 = map[1][1] # léger 
  B2 = map[2][1]
  B3 = map[3][2] # modifier en [3][2]
  C1 = map[5][3] # moyen
  C2 = map[4][3]
  C3 = map[4][2]
  D1 = map[1][6] #boss
  D2 = map[2][6]
  D3 = map[3][6]
  D4 = map[4][6]
  D5 = map[5][6]
  D6 = map[6][6]
  E1 = map[5][0] #coffre 1
  E2 = map[6][1]
  F1 = map[6][4] #coffre 2
  F2 = map[6][5]
  G1 = map[1][5] #coffre 3
  G2 = map[2][5]
  H1 = map[2][2] #pnj
  H2 = map[4][5]


  if (position == B1 or position == B2 or position == B3) and b == False: 
    print("Il semblerait que vous ayez rencontré un ennemi")
    sleep(1.5)
    print("Dasht-e : 'Halte là voleur(se) ! Ne t’approche pas de cette oasis !'")
    sleep(1.5)
    b = True
    personnage.fight(dasht_e)
  elif (position == C1 or position == C2 or position == C3) and c == False:
    print("Il semblerait que vous ayez rencontré un ennemi")
    sleep(1.5)
    print("Gobi : 'Tu as osé t’approcher d’une de nos oasis ! À mort !!'")
    sleep(1.5)
    c = True
    personnage.fight(gobi)
  elif position == D1 or position == D2 or position == D3 or position == D4 or position == D5 or position == D6 and d == False:
    print("Il semblerait que vous ayez rencontré un le boss de la zone")
    sleep(1.5)
    print("Karakoum : 'Je suis Karakoum, chef des Vaga. Nous n’aimons pas ceux qui convoitent l’eau de nos oasis. Pour cela, tu seras châtié(e) !'")
    sleep(1.5)
    d = True
    personnage.fight(karakoum)
  elif position == H1 and h == False:    
    print("Carter : 'Salut à toi jeune voyageur(se)'")
    sleep(1.5)
    print("Carter : 'Continue vers l'est et tu trouveras quelque chose d'intéressant")
    h = True
    action()
  elif position == H2 and h == False:
    print("Carter : 'Salut à toi jeune voyageur(se)'")
    sleep(1.5)
    print("Carter : 'Continue vers le nord et tu trouveras quelque chose d'intéressant")
    h = True
    action()
  elif (position == F1 or position == F2) and f == False:
    print("Quelle chance, vous venez de trouver un coffre !!")
    f = True 
    event()
  elif (position == G1 or position == G2) and g == False: 
    print("Quelle chance, vous venez de trouver un coffre !!")
    g = True
    event()
  elif (position == E1 or position == E2) and e == False: 
    print("Quelle chance, vous venez de trouver un coffre !!")
    e = True 
    event()
  elif y == 0 or x == 0 or x == 7 :
    print("Vous vous êtes perdu(e), vous êtes mort(e) dans la tempête de sable...dommage")
    sleep(1.5)
    Menu()
  else : 
    print("Vous continuez à avancer dangereusement au sein de Desertus.")
    sleep(1.5)
    current_position_advertising()

# Nix Patriam (quatrième zone)
def check_location_biome4():

  global position
  global b
  global c
  global d
  global e
  global f
  global g
  global h
  B1 = map[6][2] # léger 
  B2 = map[5][2]
  B3 = map[5][3]
  C1 = map[2][4] # moyen
  C2 = map[3][4]
  C3 = map[4][4]
  D1 = map[1][6] #boss
  D2 = map[2][6]
  D3 = map[3][6]
  D4 = map[4][6]
  D5 = map[5][6]
  D6 = map[6][6]
  E1 = map[2][2] #coffre 1
  E2 = map[1][3]
  F1 = map[6][4] #coffre 2
  F2 = map[6][5]
  G1 = map[4][5] #coffre 3
  G2 = map[3][5]
  H1 = map[1][4] #pnj
  H2 = map[2][3]



  if (position == B1 or position == B2 or position == B3) and b == False: 
    print("Il semblerait que vous ayez rencontré un ennemi")
    sleep(1.5)
    print("Lucius Vorenus : 'Ah un(e) voyageur(se) égaré(e), prépare toi à connaître la colère des Fils d’Aquilon !!'")
    sleep(1.5)
    b = True
    personnage.fight(lucius_vorenus)
  elif (position == C1 or position == C2 or position == C3) and c == False:
    print("Il semblerait que vous ayez rencontré un ennemi")
    sleep(1.5)
    print("Aurelius Primo : 'Je vois que tu as réussi à survivre au froid de Nix Patriam…mais tu ne survivras pas à ma fureur.'")
    sleep(1.5)
    c = True
    personnage.fight(aurelius_primo)
  elif position == D1 or position == D2 or position == D3 or position == D4 or position == D5 or position == D6 and d == False:
    print("Il semblerait que vous ayez rencontré un le boss de la zone")
    sleep(1.5)
    print("Imperator : 'Toi! Tu t’aventures sur mes terres, voles mes ressources, tue mes hommes. Tu ne quitteras jamais Nix Patriam. Meurs !'")
    sleep(1.5)
    d = True
    personnage.fight(imperator)
  elif position == H1 and h == False:
    print("Carter : 'Salut à toi jeune voyageur(se)'")
    sleep(1.5)
    print("Carter: 'Continue vers l'est où une récompense t'y attend")
    h = True
    action()
  elif position == H2 and h == False:
    print("Carter : 'Salut à toi jeune voyageur(se)'")
    sleep(1.5)
    print("Carter: 'Continue vers le nord où une récompense t'y attend")
    h = True
    action()
  elif (position == F1 or position == F2) and f == False:
    print("Quelle chance, vous venez de trouver un coffre !!")
    f = True 
    event()
  elif (position == G1 or position == G2) and g == False: 
    print("Quelle chance, vous venez de trouver un coffre !!")
    g = True
    event()
  elif (position == E1 or position == E2) and e == False: 
    print("Quelle chance, vous venez de trouver un coffre !!")
    e = True 
    event()
  elif y == 0 or x == 0 or x == 7 :
    print("Vous vous êtes perdu(e), vous êtes mort(e) dans la tempête de neige...dommage")
    sleep(1.5)
    Menu()
  else : 
    print("Vous continuez à avancer dangereusement au sein de Nix Patriam.")
    sleep(1.5)
    current_position_advertising()

# Daintree (cinquième zone)
def check_location_biome5():

  global position 
  global b
  global c
  global d
  global e
  global f
  global g
  global h
  B1 = map[3][2] # léger 
  B2 = map[4][2]
  B3 = map[5][2]
  C1 = map[1][4] # moyen
  C2 = map[2][4]
  C3 = map[6][4]
  D1 = map[1][6] #boss
  D2 = map[2][6]
  D3 = map[3][6]
  D4 = map[4][6]
  D5 = map[5][6]
  D6 = map[6][6]
  E1 = map[3][3] #coffre 1
  E2 = map[4][3]
  F1 = map[1][1] #coffre 2
  F2 = map[1][2]
  G1 = map[2][5] #coffre 3
  G2 = map[6][5]
  H1 = map[2][1] #pnj
  H2 = map[5][3]


  if (position == B1 or position == B2 or position == B3) and b == False: 
    print("Il semblerait que vous ayez rencontré un ennemi")
    sleep(1.5)
    print("")
    print("Osleya : 'Tu as pénétré sur un territoire interdit ! Prépare toi au combat !'")
    sleep(1.5)
    b = True
    personnage.fight(osleya)
  elif (position == C1 or position == C2 or position == C3) and c == False:
    print("Il semblerait que vous ayez rencontré un ennemi")
    sleep(1.5)
    print("")
    print("Blodreina : 'Heda notre chef interdit le passage dans notre forêt, tu vas regretter d’être venu(e). Yu gomplei stei odon !'")
    sleep(1.5)
    c = True
    personnage.fight(blodreina)
  elif position == D1 or position == D2 or position == D3 or position == D4 or position == D5 or position == D6 and d == False :
    print("Il semblerait que vous ayez rencontré un le boss de la zone")
    sleep(1.5)
    print("")
    print("Heda : 'Dans ma langue, Heda signifie chef. Dans ma culture, nos traditions et nos règles sont sacrées. Elles nous permettent de survivre. Et elles sont implacables, comme mon jugement. Si tu parviens à gagner ce combat, tu pourras partir. Dans le cas contraire, tu seras mort(e) en guerrier(e). Jus drein jus daun !'")
    sleep(1.5)
    d = True
    personnage.fight(heda)
  elif position == H1 and h == False :
    print("Darla : 'Salut à toi jeune voyageur(se)'")
    sleep(1.5)
    print("")
    print("Darla : 'Continue vers l'ouest et tu trouveras quelque chose d'intéressant")
    h = True
    action()
  elif position == H2 and h == False: 
    print("Darla : 'Salut à toi jeune voyageur(se)'")
    sleep(1.5)
    print("")
    print("Darla : 'Continue vers l'est et tu trouveras quelque chose d'intéressant. Si tu as déja trouvé ce quelque chose alors rend toi à l'ouest.")
    h = True
    action()
  elif (position == F1 or position == F2) and f == False:
    print("Quelle chance, vous venez de trouver un coffre !!")
    f = True 
    event()
  elif (position == G1 or position == G2) and g == False: 
    print("Quelle chance, vous venez de trouver un coffre !!")
    g = True
    event()
  elif (position == E1 or position == E2) and e == False: 
    print("Quelle chance, vous venez de trouver un coffre !!")
    e = True
    event()
  elif y == 0 or x == 0 or x == 7 :
    print("Vous vous êtes perdu(e), vous êtes mort(e) tué par une mine...dommage")
    sleep(1.5)
    print("")
    Menu()
  else : 
    print("Vous continuez à avancer dangereusement au sein de Daintree.")
    sleep(1.5)
    current_position_advertising()


# Déplacement

def move():
  print("Par où voulez-vous vous dirigez ?")
  print("")
  print("Nord, Sud, Est, Ouest ?")
  print("")
  direction = input()
  while direction != "Nord" and direction != "Sud" and direction != "Est" and direction != "Ouest" : 
    print("Erreur, direction non reconnue")
    print("")
    print("Par où voulez-vous vous dirigez ?")
    print("")
    print("Nord, Sud, Est, Ouest ?")
    direction = input()     
  if direction == "Nord" or direction == "nord":
    survivor.reservoire()
    Nord()
    
  elif direction == "Sud" or direction == "sud" : 
    survivor.reservoire()
    Sud()
    
  elif direction == "Est" or direction == "est": 
    survivor.reservoire()
    Est()
    
  elif direction == "Ouest" or direction == "ouest" :
    survivor.reservoire()
    Ouest()


def Nord():
  global x
  global y 
  global position
  global biome_number
  position = map[x][y + 1]
  y += 1
  if biome_number == 1 :
    check_location_biome1()
  elif biome_number == 2 :
    check_location_biome2()
  elif biome_number == 3 :
    check_location_biome3()
  elif biome_number == 4 :
    check_location_biome4()
  elif biome_number == 5 :
    check_location_biome5()
  

def Sud() : 
  global x
  global y 
  global position
  global biome_number
  position = map [x][y - 1]
  y -= 1
  if biome_number == 1 :
    check_location_biome1()
  elif biome_number == 2 :
    check_location_biome2()
  elif biome_number == 3 :
    check_location_biome3()
  elif biome_number == 4 :
    check_location_biome4()
  elif biome_number == 5 :
    check_location_biome5()

def Est() : 
  global x
  global y 
  global position
  global biome_number
  position = map [x + 1][y]
  x += 1
  if biome_number == 1 :
    check_location_biome1()
  elif biome_number == 2 :
    check_location_biome2()
  elif biome_number == 3 :
    check_location_biome3()
  elif biome_number == 4 :
    check_location_biome4()
  elif biome_number == 5 :
    check_location_biome5()


def Ouest() : 
  global x
  global y
  global position
  global biome_number
  position = map [x - 1][y]
  x -= 1
  if biome_number == 1 :
    check_location_biome1()
  elif biome_number == 2 :
    check_location_biome2()
  elif biome_number == 3 :
    check_location_biome3()
  elif biome_number == 4 :
    check_location_biome4()
  elif biome_number == 5 :
    check_location_biome5()


# Actions du joueur

def action():
  print("Il vous reste",survivor.essence,"litres d'essence")
  sleep(1.5)
  print("")
  print("Que voulez-vous faire ?")
  print("")
  print("(1) Ouvrir l'inventaire, (2) Se déplacer, (3) Afficher sa vie")
  print("")
  choice = input()
  while choice != "1" and choice != "2" and choice != "3" :
    print("Erreur")
    print("")
    sleep(1.5)
    print("Que voulez-vous faire ?")
    print("")
    print("(1) Ouvrir l'inventaire, (2) Se déplacer, (3) Afficher sa vie")
    print("")
    choice = input()
  if choice == "1" : 
    inventory()
  elif choice == "2" and survivor.essence > 0 : 
    move()
  elif choice == "2" and survivor.essence == 0 :
    print("Vous n'avez plus d'essence")
    if inventaire["Bidons d'essence"] > 0 :
      print("Vous remettez de l'essence dans votre buggy")
      inventaire["Bidons d'essence"] -= 1
      move()
    else :
      print("Vous n'avez plus d'essence pour continuer le jeu")
      sleep(1.5)
      print("")
      print("Vous vous êtes fait rattrapé et tué par une faction")
      sleep(1.5)
      print("")
      print("Dommage...")
      sleep(1.5)
      Menu()
  else : 
    stats()

# Map 

map = [["Z0","A0","B0","C0","D0","E0","F0"],["Z1","A1","B1","C1","D1","E1","F1"],["Z2","A2","B2","C2","D2","E2","F2"],["Z3","A3","B3","C3","D3","E3","F3"],["Z4","A4","B4","C4","D4","E4","F4"],["Z5","A5","B5","C5","D5","E5","F5"],["Z6","A6","B6","C6","D6","E6","F6"],["Z7","A7","B7","C7","D7","E7","F7"]]
global x
global y
global position
global inventaire
global biome_number
global b
global c
global d 
global e
global f 
global g 
global h 
b = False
c = False
d = False
e = False
f = False
g = False
h = False
biome_number = 0
x = 3
y = 1
position = map[x][y]
inventaire = {"Rations d'eau" : 2, "Rations de nourriture" : 3, "Bidons d'essence" : 1, "buggy" : 1}

def current_position_advertising():
  global x
  global y
  global position 
  A1 = map[1][5]
  A2 = map[1][4]
  A3 = map[1][3]
  A4 = map[1][2]
  B1 = map[2][1]
  B2 = map[3][1]
  B3 = map[4][1]
  B4 = map[5][1]
  C1 = map[6][2]
  C2 = map[6][3]
  C3 = map[6][4]
  C4 = map[6][5]
  D1 = map[1][6]
  D2 = map[2][6]
  D3 = map[3][6]
  D4 = map[4][6]
  D5 = map[5][6]
  D6 = map[6][6]

  if position == A1 or position == A2 or position == A3 or position == A4 :
    print("Attention vous êtes proche d'une zone mortelle, en continuant vers l'ouest vous mourrez")
    action()
  elif position == B1 or position == B2 or position == B3 or position == B4:
    print("Attention vous ne pouvez plus reculer, vous risqueriez de vous faire décimer par les factions derrières vous.")
    action()
  elif position == C1 or position == C2 or position == C3 or position == C4 :
    print("Attention vous êtes proches d'une zone mortelle, en continuant vers l'est vous mourrez.")
    action()
  elif position == map[6][1]:
    print("Attention vous êtes proches dd'une zone mortelle vous empêchant de continuer vers l'est , ne reculez pas non plus ou vous vous feriez décimer par les factions derrières vous.")
    action()
  elif position == map[1][1]:
    print("Attention vous êtes proche d'une zone mortelle vous empêchant d'aller vers le Sud et vers l'Ouest, changer de cap si vous ne souhaiter pas mourrir")
    action()
  elif position == D1 or position == D2 or position == D3 or position == D4 or position == D5 or position == D6 :
    biome()
  else :
    action()

# Fin du jeu
def fin(): 
  print("Vous avez vaincu le dernier ennemi")
  sleep(3)
  print("Vous êtes mal en point, mais vous voyez enfin le bout du chemin, la porte qui vous sauvera de cette enfer est à porté")
  sleep(3)
  print("Vous rassemblez vos dernières forces afin de vous lever, vos blessures vous déchirent mais les images de New Babylone, cette cité tant convoitée vous donne la force d'avancer")
  sleep(6)
  print("Les portes sont lourdes, vous les poussez de toutes vos forces")
  sleep(3)
  print("Vous poussez plus fort encore...")
  sleep(3)
  print("De toutes vos forces...")
  sleep(3)
  print("Les portes s'ouvrent enfin, voulez-vous avancer dans New Babylone?")
  choice = input()
  if choice == "non" or choice == "Non" or choice == "NON":
    print("Voulez-vous vraiment abandonner après tout ce chemin ?")
    sleep(2)
    print("Non vous ne pouvez pas abandonner après cette aventure")
    sleep(2)
    print("Alors vous continuez à avancer")
    sleep(3)
  while choice !="oui" and choice!= "non" and choice != "Oui" and choice != "Non" and choice != "OUI" and choice != "NON":
    print("Je n'ai pas bien entendu, voulez vous avancer dans New Babylone?")
  print("Vous visualisez une ville incroyable, un jardin luxuriant rempli de fruits et de baies, un nombre incalculable de couleurs traversent votre rétine, mais le doute s'installe dans votre esprit.")
  sleep(4)
  print("Vous vous sentez mal alors vous décidez de vous asseoir un instant afin de reprendre vos esprits")
  sleep(2)
  print("Avant même que vous puissiez vous asseoir, vos jambes vous lâchent")
  sleep(2)
  print("Vous entendez un cri étouffé…")
  sleep(2)
  print("Votre gorge vous fait mal…")
  sleep(2)
  print("Vous reprenez enfin votre esprit et réalisez la vérité")
  sleep(2)
  print("Les cris entendus provenaient de vous..")
  sleep(2)
  print("Cette vision que vous avez eue, cette ville et ce jardin se transforment en un amas de ruines et de poussières. Vous n'apercevez que le lit d'une rivière presque intégralement asséchée, les bâtiments sont délabrés, certains ne sont plus que ruines...")
  sleep(8)
  print("Cette cité utopique est en réalité...")
  sleep(2)
  print("Une ville fantôme !")
  sleep(2)
  print("Tout les sacrifices que vous avez réalisés, toutes les épreuves traversées pour arriver jusqu'ici. Tout défile devant vos yeux. Vous lâchez votre dernier cri de désespoir, si intense qu'il fait fuir les derniers corbeaux présents dans le lit de la rivière")
  sleep(8)
  print("Tout d'un coup votre vision se brouille de nouveau")
  sleep(2)
  print("Vous vous rendez compte")
  sleep(2)
  print("Qu'il ne vous reste que peu de temps")
  sleep(2)
  print("Vos blessures ont été fatales...")
  sleep(2)
  print("Vous récupérez vos dernières forces pour vous posez dans un coin à l'ombre, vous y passez vos derniers moments en paix loin du soleil, de la chaleur, de ce monde qui vous a tant fait souffrir...")
  sleep(5)
  print("Submergé de déception, vous chargez votre arme avec votre dernière munition et la pointez contre votre tempe...")
  sleep(4)
  print("Voulez-vous maitriser votre destin jusqu'au bout ?")
  sleep(1)
  choice = input()
  if choice == "oui" or choice == "Oui" or choice =="OUI" :
    sleep(2)
    print("*inspiration*")
    sleep(2)
    print("*bang*")
    sleep(2)
    print("*cling-cling*")
    sleep(2)
    print("La douille roule sur le sol")
    sleep(2)
    credits()
  elif choice == "non" or choice == "Non" or choice == "NON":
    sleep(2)
    print("Vous vous réveillez et apercevez un rodeur au loin..")
    sleep(2)
    print("Il court vers vous, se rapproche de plus en plus...")
    sleep(2)
    print("Vous portez le regard sur votre arme, vous la chargez.")
    sleep(2)
    print("Un dernier coup d'oeil vers lui avant qu'il ne soit trop près...")
    sleep(2)
    print("Son canon est déjà braqué sur vous")
    sleep(2)
    print("*bang*")
    sleep(0.3)
    print("*cling-cling*")
    sleep(1)
    print("*bang*")
    sleep(0.3)
    print("*cling-cling*")
    sleep(1)
    print("*bang*")
    sleep(0.3)
    print("*cling-cling*")
    sleep(2)
    credits()

def biome():
  global x
  global y 
  global biome_number
  global b
  global c
  global d
  global e
  global f
  global g
  global h
  biome_number += 1
  x = 3 
  y = 1 
  b = False
  c = False
  d = False
  e = False
  f = False
  g = False
  h = False
  if biome_number == 2 : 
    print("Votre victoire face au boss de la faction vous a permis de ramasser une arme")
    print("")
    print("Vous avez récupéré une masse couverte de crochets de serpents qui empoisonne l’ennemi en plus de lui enlever instantanément 10 points de vie + 2 points de vie par seconde pendant 6 secondes à mesure que le venin agit.")
    sleep(1.5)
    print("Vous remplacez votre knout par cette nouvelle arme")
    print("")
    survivor.armes = {"arme 1" : { "nom" : "gun", "leger" : 15, "moyen" : 20},"arme 2" : {"nom": '"I wish a motherfucker would"', "leger" : 20, "moyen" : 40}}
    print("Vous arrivez dans le marais des Sombres Ecailles. Territoire envahie par des vapeurs toxiques et denses, cette zone marécageuse est inhospitalière pour tous ceux qui s’y aventurent. Les Sombre Ecailles contrôlent la zone et connaissent tous les chemins à travers ce marais sinueux. Les vapeurs émanant de ce lieu rendent la conduite dangereuse. Faites attention à vous", player_name," !")
  elif biome_number == 3 : 
    print("Votre victoire face au boss de la faction vous a permis de ramasser une arme")
    print("")
    print("Vous avez récupéré un AK-47 qui permet de prévenir le danger à distance en tuant tout ce qui s’approche.")
    sleep(1.5)
    print("Vous remplacez votre gun par cette nouvelle arme")
    print("")
    survivor.armes = {"arme 1" : {"nom": '"I wish a motherfucker would"', "leger" : 15, "moyen" : 30},"arme 2" : {"nom": "AK-47", "leger" : 25, "moyen" : 50}}
    print("Vous êtes désormais à Dersertus, ancienne prairie réduite à l’état de désert aride et dangereux à la suite d’un conflit armé très violent il y a très longtemps. Desertus est un espace où règne le silence sous un soleil de plomb. Des tempêtes de sable viennent parfois perturber ce calme apparent. Des oasis parsèment ce désert mais elles sont farouchement gardées par les Vaga, la puissante faction contrôlant la zone. Restez sur vos gardes",player_name)
  elif biome_number == 4 : 
    print("Votre victoire face au boss de la faction vous a permis de ramasser une arme")
    print("")
    print('Vous avez récupéré "Dracarys" : une arme puissante pouvant brûler les ennemis et les réduisant en cendres. Attention "Dracarys" est une arme de courte distance. À éviter pour le coprs à corps')
    sleep(1.5)
    print('Vous remplacez le "I wish a motherfucker would" par cette nouvelle arme.')
    print("")
    survivor.armes = {"arme 1" : {"nom": "AK-47", "leger" : 25, "moyen" : 50},"arme 2" : {"nom": "Dracarys", "leger" : 30, "moyen" : 60}}
    print("Vous voici à Nix Patriam, contrée glaciale balayée par une tempête perpetuelle rendant les conditions de vies très difficiles. Au centre de la zone, se trouve la plus haute montagne du monde, le mont Atlas. Les Fils d’Aquilon rôdent dans la zone et traquent les voyageurs solitaire pour les dépouiller. Gardez votre arme près de vous,",player_name)
  elif biome_number == 5 : 
    print("Votre victoire face au boss de la faction vous a permis de ramasser une arme")
    print("")
    print("Vous avez récupéré le Railgun : un fusil à propulsion électro-magnétique qui détruit l’ennemi et tout ce qu’il y a autour. C'est une arme ultime à utiliser seulement en cas d’extrême urgence.")
    sleep(1.5)
    print("Vous remplacer le AK-47 par cette nouvelle arme.")
    print("")
    survivor.armes = {"arme 1" : {"nom": "Dracarys", "leger" : 30, "moyen" : 60},"arme 2" : {"nom": "Railgun", "leger" : 35, "moyen" : 70}}
    print("Vous avez parcouru de nombreux kilomètres et vous arrivez à Daintree. Une forêt luxuriante de prime abord mais qui peut s’avérer dangereuse dès que le vent tourne. En effet, des pluies d’acides s'abattent de temps à autre pouvant faire fondre la carrosserie d’un véhicule même avec de bonnes plaques de blindage. Trikru, une faction à la tête de ce territoire, interdit aux étrangers de le traverser sous peine de mort. Ne vous faites pas prendre",player_name)    
  if biome_number == 6 : 
    fin()
  sleep(1.5)
  action()

# Inventaire

def inventory():
  for keys, values in inventaire.items():
    print(keys,values)
  print("Voulez-vous utiliser un objet ? ")
  choice = input()
  A = "oui"
  B = "Oui"
  C = "non"
  D = "Non"
  while choice != A and choice != B and choice != C and choice != D:
    print("Erreur")
    print("Voulez-vous voir et utiliser un objet ? ")
    choice = input()
  if choice == A or choice == B :
    print("Que voulez-vous utiliser ?")
    print("(1) Rations d'eau, (2) Rations de nourriture, (3) Bidons d'essence")
    choice = int(input())
    while choice < 1 or choice > 3 :
      print("Erreur")
      print("Que voulez-vous utiliser ?")
      print("(1) Rations d'eau, (2) Rations de nourriture, (3) Bidons d'essence")
      choice = int(input())
    if choice == 1 : 
      personnage.soin()
      action()
    elif choice == 2 : 
      personnage.endurance()
      action()
    else :
      personnage.essence()
      action()
  if choice == C or choice == D : 
    action()

# Stats

global deplacement
deplacement = 0

def stats():
  print("Vous avez ",survivor.vie,"hp")
  sleep(1.5)
  print("Vous avez ",survivor.stamina,"points d'endurance")
  sleep(1.5)
  action()

def essence() : 
  global deplacement
  A = inventaire["Bidons d'essence"]
  if A > 0 : 
    inventaire["Bidons d'essence"] -= 1
    deplacement += 1
    print("Vous avez désormais",deplacement,"litres d'essences")
    sleep(1.5)
    print("Il vous reste ",inventaire["Bidons d'essence"],"bidons d'essences")
    sleep(1.5)
    inventory()
  else : 
    print("Vous n'avez plus de bidons d'essences")
    sleep(1.5)
    inventory()

# Event dans le biome

def event():
  print("Dans ce coffre, tu trouveras le nécessaire pour survivre durant quelques heures, il y a de l'eau, de l'essence et de la nourriture")
  sleep(1)
  print("")
  coffre  = {"Rations d'eau" : 2, "Rations de nourriture" : 3, "Bidons d'essence" : 1}
  sleep(1)
  print("")
  for keys, values in coffre.items():
    print(keys,values)
  sleep(1)
  choice = input("Veux-tu ajouter le contenu du coffre dans ton inventaire ? (o/n)")
  while choice != "o" and choice != "n" :
    print("Je n'ai pas bien compris ta réponse")
    sleep(1)
    choice = input("Veux-tu ajouter le contenu du coffre dans ton inventaire ? (o/n)")
    print("")
  if choice == "o":
    inventaire["Rations d'eau"] += 2
    inventaire["Rations de nourriture"] += 3 
    inventaire["Bidons d'essence"] += 1
    print("")
    print("Grâce au coffre, tu as désormais",inventaire["Rations d'eau"],"rations d'eau,", inventaire["Rations de nourriture"],"rations de nourriture","et",inventaire["Bidons d'essence"],"bidons d'essence. Tu peux continuer ton chemin !")
    print("")
    action()
  if choice == "n":
    print("Tu peux continuer ton chemin si tu estimes pouvoir te passer du coffre")
    print("")
    action()


# Menu du jeu

def Menu():
  print("Bienvenue dans le menu du jeu")
  print("Lancer le jeu (1)")
  print("Voir les crédits (2)")
  print("Règles du jeu (3)")
  print("Quitter le jeu (4)")
  choice = int(input())
  while choice < 1 or choice > 3 :
    print ("Erreur")
    choice = int(input())
  if choice == 1 :
    start_game()
  elif choice == 2 : 
    credits()
  elif choice == 3 :
    rules()
  else : 
    exit()


def start_game():
  global player_name
  player_name = ask_name()
  print("Dans un futur proche, en l’an 2077, alors que le monde que nous connaissons est révolu, que les ressources en eau et en hydrocarbures sont presque intégralement épuisées, que la sécheresse a annihilé toute forme de biodiversité, seule une cité a survécu.\nNew Babylon est la dernière et la seule cité autonome de notre monde.\nElle produit son propre carburant, sa propre eau et ses habitants ont même réussi a cultiver fruits et légumes grâce à de nouvelles techniques de serriculture. Évidemment, ce paradis terrestre est envié de tous mais tout le monde ne peut y accéder.\nRescapé de ce monde post-apocalyptique, vous vous êtes réfugié(e) dans une grotte mais poussé à partir par manque de nourriture votre objectif sera de rejoindre la cité pour retrouver la civilisation, mais prenez garde la route est périlleuse !\nDe nombreuses factions se sont développées et veulent elles aussi rejoindre et prendre d’assaut New Babylon.\nPour réussir votre objectif vous ne possédez que votre buggy et 1 réserve d’essence, 3 rations d’eau, et 1 ration de nourriture. Un conseil n'oubliez pas de prendre votre knout et votre gun avant de partir.\nBonne chance", player_name)
  sleep(10)
  print("")
  print(player_name,"vous voici maintenant dans le monde de Wāha, vous disposez actuellement de :")
  print("")
  for keys, values in inventaire.items():
    print(values, keys)
  sleep(5)
  print("")
  print("Après plusieurs heures de voyage dans votre buggy, vous vous raprochez de New Babylone et entrez dans une zone inconnue...")
  sleep(2)
  print("")
  print("Vous voici au sein de Neo Polis, ruine d’une ancienne mégalopole recouvrant l’intégralité de la zone, de nombreux véhicules désossés, des magasins vides et des animaux sauvages y sont présents. Les désosseurs, la faction contrôlant la zone est constamment à la recherche de nouvelles ressources pour ces véhicules blindés ou pour ses armes. Attention à vous !")
  sleep(2)
  print("")
  biome()

def ask_name():
  print("Entrer votre nom :")
  choice = input()
  return choice

global player_name
player_name = None

def load_game():
  # charger des datas en mémoire
  start_game()

def credits():
  # print afficher des infos sur la teams 
  print("Wāha")
  sleep(1.5)
  print("Un jeu développé par Cin'Hetic Games")
  sleep(1.5)
  print("Développeurs : Marie René, Lucas Rimbault, Adam Maaloul, Marie-Gwenaëlle Fahem")
  sleep(1.5)
  print("Scénario : Marie René")
  sleep(1.5)
  print("Biomes : Lucas Rimbault, Adam Maaloul, Marie-Gwenaëlle Fahem")
  sleep(1.5)
  print("Évènements dans les biomes : Marie René")
  sleep(1.5)
  print("Déplacement : Lucas Rimbault, Adam Maaloul")
  sleep(1.5)
  print("Inventaire : Marie René, Adam Maaloul")
  sleep(1.5)
  Menu()

def exit():
  return
  # quitter le jeu

def rules():
  print("Dans Waha, les combats fonctionnent à l'aide d'un système de choix d'armes et de choix d'intensité d'attaques.")
  sleep(1)
  print("Ces choix influencent l'endurance, ainsi que les points de vie. Choissisez bien vos attaques, l'endurance ne se régènerent pas seul !")
  sleep(1)
  print("L'essence sera également très importante, elle vous permettera de vous déplacer, sans essence votre aventure s'arrete !")
  sleep(1)
  print("Dans votre inventaire, les rations d'eau correspondent à vos points de vie, les rations de nourriture à votre endurance et les bidons d'essence à votre capacité de déplacement.")
  sleep(1)
  print("Au long de votre aventure vous rencontrerez des coffres dispérsés dans les biomes, ils vous seront utiles pour collecter de nouvelles ressources.")
  sleep(1)
  print("Attention votre destination se trouve vers le Nord, ne soyez pas trop hésitants...")
  sleep(5)
  Menu()