#Prend en entrée plusieurs noms et prénoms et affiche seulement 
#le premier et le dernier nom en utilisant la destructuration

noms = input("Entrez vos prénoms et votre nom : ")
liste_noms = noms.split(" ")

prénom,*_,nom = liste_noms

print("Bienvenue",prénom,nom)