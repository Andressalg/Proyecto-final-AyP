from Moderation import Moderation
#import mathplotlib

class Indicators(Moderation):

    def showmostposts ():
        for i in postdatabase:
            i.postsshow
            pass

    def mostpostscareer (self, career):
        for i in self.userlist:
            if career == career["department"]:
                return i
   
    def mostinteractionspost (self):
        pass

    def mostinteractionsuser (self):
        pass

    def mostdeleted (self):
        pass

    def careerbadcomments (self):
        pass

    def deletedusers(self):
        pass

