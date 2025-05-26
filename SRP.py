class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        print(f"Salvando usuário {user.name} no banco de dados")

# Uso
user = User("João", "joao@email.com")
repo = UserRepository()
repo.save(user)