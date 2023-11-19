from Multimedia import Multimedia
from Profile import Profile

class Interaction(Multimedia, Profile):

    #seguir un usuario
    def follow (self, userfollowing):
        self.following.append(userfollowing)

    #comentario guardando user, post, comentario, fecha
    def comment(self):
        return super().comment()
    
    #eliminar comentario
    def deletecomment(self, comment):
        for comment in self.comments:
            print("deseas borrar este comentario?")
            x = (input("Y/N"))
            if x == "Y" or x == "y":
                del comment
            elif x == "N" or x == "n":
                continue
            else:
                return "error"


    #acceder desde listado de like
    def accesslike(self, post):
        for i in self.peopleliked(post):
            return i

    #acceder desde listado de comentarios
    def accesscomment(self, post):
         for i in self.peoplecommented(post):
            return i


