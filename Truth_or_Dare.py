#-*-coding:latin-1-*
import os 

print("\t\t--------------------- BIENVENU DANS ACTION OU VɉRITɉ ---------------------")

print("L'actions compte 15 pts et la v�rit� 5 pts\n")

genre = game_type()

print(genre.upper())

nbr_utilisateur = rec_user_number()

utilisateurs = rec_user_name(nbr_utilisateur)

action,verite = recovery_quiz(genre)

nbr_tour = nbr_utilisateur * 3

partie_en_cour = {}

i = 0
while i < nbr_utilisateur :
    user,so = utilisateurs[i]
    partie_en_cour[user] = so
    i += 1

continuer_partie = True

while continuer_partie:
    inc = 1
    player = 0
    while inc != nbr_tour:
        nom,score,player= pick(utilisateurs,player,nbr_utilisateur)
        if inc == 0:
            print("\n--------------------- ON COMMENCE AVEC :",nom.upper(),"---------------------")
        else:
            print("\n---------------------",nom.upper()," C'EST VOTRE TOUR---------------------")
        option,pts = play_quiz(action,verite)
        print(option.upper())
        verif = validation()
        if verif:
            partie_en_cour[nom] += pts
        print(nom.upper(),"Vous avez : ",partie_en_cour[nom]," pts")
        if   inc % nbr_utilisateur  == 0 and inc != 0:
            print("\n**************RECAPITULATIF**************")
            for name,values in partie_en_cour.items():
                print(name," : ",values)
        inc += 1
        player += 1
    oui = False
    while not oui:
        leave = input("Voulez-vous continuer (O/N) : ")
        if not leave.isalpha() or len(leave) > 1:
            print("Vous n'avez pas saisi une lettre")
            oui = False
            continue
        elif leave.lower() != 'o' and leave.lower() != 'n':
            print("Veuillez saisi une lettre valide")
            oui = False
            continue
        elif leave.lower() == 'o':
            oui = True
            continuer_partie = True
        elif leave.lower() == 'n':
            oui = True
            continuer_partie = True
pause()
