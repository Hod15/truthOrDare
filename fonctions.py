from tr_da.dare import *
from tr_da.truth import *
from random import *
import os

def rec_user_number():#enregistrement du nombre de joueur
	ok_user = False #variable de verif de la boucle
	nb_user = 0
	while not ok_user:
		nb_user = input("\nA combien voulez-vous jouer: ")
		try:
			nb_user = int(nb_user)
		except ValueError:#on demande à l'utilisateur de réentrer son choix s'il n'est pas un int
			print("!!!! INVALIDE !!!!\nVous n'avez pas saisi un nombre")
			ok_user = False
			continue
		if nb_user <= 0:
			print("Le nombre saisi est négatif ou nul")
			ok_user = False
			continue
		elif nb_user == 1:#empêche un utilisateur de jouer s'il est seul
			print("Vous devez être au minimum deux")
			ok_user = False
			continue
		else:
			ok_user = True
	return nb_user #renvoie le nombre de joueur

def rec_user_name(nb_user):#enregistrement du nom des joueurs
	users = {}
	reg = 0
	while reg < nb_user:
		ok_reg = False
		while not ok_reg:
			user_name = input("Entre un nom ou pseudo: ")
			user_name = user_name.capitalize()
			if not user_name.isalnum or len(user_name) < 3:#verifie si le nom n'est pas un chiffre ou si le nombre de carateres est au moins = 4
				print("!!!! Ce nom ou pseudo n'est pas valide !!!!")
				ok_reg = False
				continue
			elif (user_name,0) in users.values():
                                                print("Ce nom a déjà été saisi. Veuillez le changer\n")
                                                ok_reg = False
                                                continue
			else:
				ok_reg = True

		users[reg] = (user_name,0) #stockage des noms et des scores initiaux 
		reg += 1
		if reg == nb_user:
			reg += nb_user
	return users

def game_type():
	ok_user = False
	while not ok_user:
                choi = input("Etes vous 1 --> JUNIOR ou 2 --> ADOS :")#enregistre pour savoir s'il est mature
                try:
                        choi = int(choi)
                except ValueError:
                        print("Vous n'avez pas saisi un entier")
                        ok_user = False
                        continue
                if choi < 1 or choi >2:
                        print("le chiffre saisi n'st pas dans l'intervalle")
                        ok_user = False
                        continue
                if choi == 1:
                        choi = "junior"
                        ok_user = True
                elif choi == 2:
                        choi = "ados"
                        ok_user = True
                return choi
	
def recovery_quiz(choix):
	if choix == "junior":
		dare = dare_jun
		truth = truth_jun
		return dare,truth
	else:
		dare = dare_ado
		truth = truth_ado
		return dare,truth

def pick(users,joueur,nb_user):
	if joueur >= nb_user:
                joueur = 0
	name,score = users[joueur]
	return name,score,joueur

def play_quiz(dare,truth):
	ok = False
	while not ok:
		choisir = input("\nACTION (a) OU VÉRITÉ (v) : ")
		if not choisir.isalpha() or len(choisir) > 1:
			print("Vous n'avez pas saisi une lettre")
			ok = False
			continue
		elif choisir.lower() == "a" :
			quiz = choice(dare)
			pts = dare_pts
			ok = True
		elif choisir.lower() == "v":
			quiz = choice(truth)
			pts = truth_pts
			ok = True
		elif choisir.lower() != "a"  and choisir.lower() != "v":
			print("Veuillez saisi une lettre valide")
			ok = False
			continue
	return quiz,pts

def validation():
	ok = False
	while not ok:
		verif = input("Est ce valider OUI (o) / NON (n) : ")
		if not verif.isalpha or len(verif) > 1:
			print("Vous n'avez pas saisi une lettre")
			ok = False
			continue
		elif verif.lower() != 'o' and verif.lower() != 'n':
		    print("Veuillez saisi une lettre valide")
		    ok = False
		    continue 
		else:
			ok = True
	if verif.lower() == 'o':
		return True
	else:
		return False
def pause():
        os.system("pause")