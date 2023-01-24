class Bibliotheque:
    def __init__ (self,liste,nom):
        self.listDesLivres = liste
        self.nom = nom
        self.lendDict = {}
 
    def DisplayBooks(self):
        #méthode chargée de retourner les livres disponibles
        for book in self.listDesLivres:
            print(book)
    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Vous pouvez prendre le livre !")
        else:
            print(f"le livre n'est pas disponible, il est actuellement emprunté par : {self.lendDict[book]}")

    def addBook(self,book):
        self.listDesLivres.append(book)
    def returnBook(self,book):
        if book in self.lendDict:
            user_confirm = input(f"Etes-vous sûr de vouloir retourner le livre {book} emprunté par {self.lendDict[book]}? Entrez 'y' pour continuer ou 'n' pour annuler:")
            if user_confirm == 'y':
                self.lendDict.pop(book, None)
                print("Merci d'avoir retourné le livre !")
            else:
                print("Retour de livre annulé.")
        else:
            print(f"Le livre {book} n'est pas actuellement emprunté.")
biblioCegep = Bibliotheque(["One Hundred Years of Solitude","To Kill a Mockingbird","The Grapes of Wrath","Pride and Prejudice","The Adventures of Sherlock Holmes"],"Bibliothèque de cegep")
while(True):
    print(f"Bienvenue à la {biblioCegep.nom}. Entrez votre choix pour continuer")
    print("1. Afficher les livres")
    print("2. Emprunter un livre")
    print("3. Ajouter un livre")
    print("4. Retourner un livre")
    user_choice = input()
    if user_choice not in ['1','2','3','4']:
        print("SVP Entrez une option valide")
    else:
        user_choice = int(user_choice)
        if user_choice == 1:
            biblioCegep.DisplayBooks()
        elif user_choice == 2:
            book = input("Entrez le titre du livre que vous voulez emprunter:")
            user = input("Entrez votre nom")
            biblioCegep.lendBook(user,book)
        elif user_choice == 3:
            book = input("Entrez le titre du livre que vous voulez ajouter:")
            biblioCegep.addBook(book)
        elif user_choice == 4:
            book = input("Entrez le titre du livre que vous voulez retourner:")
biblioCegep.returnBook(book)
