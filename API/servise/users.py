from scheme.users import User,Creds,Creds2
import uuid


class UserService:
    def get_users(self) -> list[User]:
        file = open("Base_Data.txt","r")
        base = file.readlines()
        items = []
        for item in base:
            item = item.split()
            if len(item) != 0:
                items.append(
                    User(
                        id=item[0],
                        username=item[1],
                    )
                )
        return items

    def register(self, paylods: Creds,data:Creds2) -> User | str:
        user = {
            "id": uuid.uuid4(),
            "username": paylods.username,
            "password": paylods.password
        }
        user1 = {
            "password1": data.password1,
        }
        if user["password"] == user1["password1"]:
            file = open('Base_Data.txt', 'a+')
            for key, value in user.items():
                file.write(f'{value } ')
            file.write(f'\n')
            file.close()
            return User(
                id=user["id"],
                username=user["username"]
            )
        return f'failure'

user_service: UserService = UserService()
