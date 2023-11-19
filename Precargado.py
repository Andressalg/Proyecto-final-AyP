import requests
import pickle
from Profile import Profile

def manageapi(api):
    jsontousers = []
    for i in api:
        if i["type"] == "professor":
            user = Profile(i["firstName"],
                            i["lastName"], 
                            i["email"], 
                            i["username"],
                            i["type"],
                            i["department"])
            user.id = i["id"]
            jsontousers.append(user)
        else:
            user = Profile(i["firstName"], i["lastName"], i["email"], i["username"], i["type"], i["department"])
            user.id = i["id"]
            jsontousers.append(user)


def APItousers():  
    request_users = requests("GET", "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/08d4d2ce028692d71e9f8c32ea8c29ae24efe5b1/users.json")
    apiusers = request_users.json()
    userdatabase = manageapi(apiusers)
    request_post = requests("GET", "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/posts.json")
    postdatabase = request_post.json()
    return userdatabase, postdatabase

def loadusers(usuarios):
    binarywrite=open("c:\Users\Buste\Documents\UNIMET\Algoritmos y Programacion\Proyecto Final\Archivos del Proyecto","wb")
    pickle.dump(usuarios,binarywrite)

    binarywrite.close()

def readusers(usuarios):

    binaryread= open("c:\Users\Buste\Documents\UNIMET\Algoritmos y Programacion\Proyecto Final\Archivos del Proyecto","rb")
    users=pickle.load(binaryread)
    binaryread.close()
    return users

def loadposts(posts):
    binarywrite=open("c:\Users\Buste\Documents\UNIMET\Algoritmos y Programacion\Proyecto Final\Archivos del Proyecto","wb")
    pickle.dump(posts,binarywrite)

    binarywrite.close()

def readposts(posts):

    binaryread= open("c:\Users\Buste\Documents\UNIMET\Algoritmos y Programacion\Proyecto Final\Archivos del Proyecto","rb")
    posts=pickle.load(binaryread)
    binaryread.close()
    return posts

def register_user(users):
  users.append({
                 "id": "3270ad46-759f-4f76-ac94-2d69b8d776b5",
                 "firstName": "Andres",
                 "lastName": "Salgueiro",
                 "email": "AHSAL@unimet.edu.ve",
                 "username": "Salgueiro_",
                 "type": "student",
                 "department": "Derecho",
                 "following": []
               })

  with open('users.json', 'w') as f:
    f.write(users)