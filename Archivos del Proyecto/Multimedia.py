import datetime
from Like import Like
from Commentaries import Commentaries

class Multimedia:

    
    def __init__(self, user, type, description, hashtag):
        self.user = user
        self.type = type
        self.description = description
        self.hashtag = hashtag
        self.date = datetime.now
        self.comments = []
        self.likes = []

    #datos del post y commentarios
    def showpost (self):
        x =  print (f"multimeda: {self.user} \n,
                        descrption: {self.description} \n,
                        hashtag:{self.hashtag} \n,
                        date: {self.date} \n, 
                        likes: {sum(self.likes)} \n,
                        comments: {self.comments}")
        return x

    #like
    def like(self, liker):
        userfound = True
        for like in self.likes:
                if like.liker == liker:
                    self.likes.remove(like)
                    userfound = False
                    break
            
        if not userfound:
            like = Like(liker, self)
            self.likes.append(like)

    #Comentar:
    def commment (self, commenter):
        Comments = input("escriba su commentario, recuerde ser civil >>  ")
        Comments = Commentaries(commenter, self, Comments)
        self.Comments.append(Comments)
        return "su comentario ha sido publicado"

    #buscar en base a hashtag
    def searchhashtag (self):
        x = input("escriba el nombre del hashtag el cual quiera buscar")
        similars = []
        for i in self.posts["department"]:
            for j in self.hashtag:
                if self.hashtag == x:
                    similars.append(j)
                    return print(similars)
        