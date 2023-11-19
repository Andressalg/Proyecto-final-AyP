from Profile import Profile

class Moderation(Profile):

    def __init__(self, username, multimedia, description, hashtag, date):
        super().__init__(username, multimedia, description, hashtag, date)
        self.moderator = True

    #Eliminar un post que considera ofensivo
    def offensivepost(self, post):
        x = input("razon por la cual la publicacion sera borrada")
        del post
        return f"la publicacion fue borrada por un moderador debido a la siguiente razon: {x}"

    #Eliminar un comentario ofensivo
    def offensivecomment(self, commentario):
        x = input("razon por la cual este comentario sera borrado")
        del commentario
        return f"el comentario fue borrado por un moderador debido a la siguiente razon: {x}"

    #Eliminar un usuario que infringido múltiples veces las reglas
    def offensiveuser(self, user):
        x = input("razon por la cual este usuario sera borrado")
        del user
        return f"este perfil fue borrado por un moderador debido a la siguiente razon: {x}"

    