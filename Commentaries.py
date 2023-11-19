import datetime

class Commentaries():
    def __init__(self, users, body):
        self.users = users
        self.body = body
        self.date = datetime.now()

    def show(self):
        print(f"{self.users}, {self.date} \n {self.body}")