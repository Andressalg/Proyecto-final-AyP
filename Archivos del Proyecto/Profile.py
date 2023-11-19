import requests
from Multimedia import Multimedia
 
class Profile:

    def __init__(self, firstName, lastName, email, username, type, department):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.username = username
        self.type = type
        self.department = department
        self.following = []
        self.posts = []

    #Registrar Usuario
    def register_user(self):
        userslist = []
        while True:
                temp_firstname = input("Ingrese sus nombres >> ")
                temp_lastname = input("Ingrese sus apellidos >> ")
                temp_email = input("Ingrese su correo electronico >> ")
                temp_username = input("Ingrese sus nombre de usuario preferido >> ")
                temp_type = input("Ingrese si es profesor or estudiante >> ")
                temp_department = input("Ingrese su carrera >> ")
                
                User = Profile(temp_firstname, temp_lastname, temp_email, temp_username, temp_type, temp_department)
                userslist.append = [User]
                return userslist, User


    #Buscar perfiles en base a usuario #Queda buscarlo por la lista metida en el JSON
    def search_by_username (self):
        users = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/08d4d2ce028692d71e9f8c32ea8c29ae24efe5b1/users.json"
        datos = requests.get(users).json()
        x = str(input("ingrese un usuario al cual buscar"))
        for x in datos:
            if x in datos(users):
                return(f"existe un usuario llamado {x}!")
            else:
                return "Este usuario no existe o ha sido borrado"

    #Buscar en base a carrera #Buscar por el JSON y la lista
    def search_by_career(self, perfil):
        if isinstance(perfil, Profile) == False:
            return "Error"
        else:
            for i in self.users:
                pass

                
    #cambiar informacion #falta
    def change_information (self, perfil):
        perfil.firstName = input("Ingrese sus nombres >> ")
        perfil.lastName = input("Ingrese sus apellidos >> ")
        perfil.email = input("Ingrese su correo electronico >> ")
        perfil.username = input("Ingrese sus nombre de usuario preferido >> ")
        perfil.type = input("Ingrese si es profesor or estudiante >> ")
        perfil.department = input("Ingrese su carrera >> ")
        return perfil


    #borrar cuenta #borrar desde el JSON()
    def delete (self, account):
        print("estas seguro que quieres borrar tu cuenta? \n [Y/N]")
        answer = str(input(">>>   "))
        if answer == "y":
            temp = []
            if isinstance(account, Profile) == True:
                del account
                return "¡Te extrañaremos!"
        elif answer == "n":
            return "Agradecemos su estancia"
        else:
            return "Respuesta Invalida"

    #mostrar cuenta #falta desde el json
    def show_profile(self, user):
        if isinstance(user, Profile())== True:
            x = print (f"firstName: {self.firstName}, lastName: {self.lastName}, email:{self.email}, {self.username}, type: {self.type}, department: {self.department}, follwing: {self.following}")
            return x

