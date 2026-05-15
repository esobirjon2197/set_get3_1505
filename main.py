
# 5-m
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.__ram = ram

    def get_ram(self):
        return self.__ram

    def set_ram(self, new_ram):
        if new_ram in [4, 8, 16, 32]:
            self.__ram = new_ram
            print("RAM yangilandi")
        else:
            print("RAM noto'g'ri")


l1 = Laptop("HP", 8)
print(l1.brand)
print(l1.get_ram())

l1.set_ram(16)
print(l1.get_ram())

l1.set_ram(12)
print(l1.get_ram())




# 6-m
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        if len(str(new_password)) >= 5:
            self.__password = new_password
            print("Parol yangilandi")
        else:
            print("Parol juda qisqa")


u1 = User("admin", 12345)
print(u1.username)
print(u1.get_password())

u1.set_password(98765)
print(u1.get_password())

u1.set_password(123)
print(u1.get_password())
