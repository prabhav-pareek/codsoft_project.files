import random
import string

class PasswordGenerator:
    def __init__(self, length):
        self.length = length
        self.characters = string.ascii_letters  

    def generate(self):
            return ''.join(random.choice(self.characters) for _ in range(self.length))

print("\t**Welcome to Password Generator**\n")
length = int(input("Enter the Length of your desired Password: "))
generator = PasswordGenerator(length)
password = generator.generate()
print("Generated password:", password)