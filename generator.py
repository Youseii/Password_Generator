# Password Generator codes
import random
import string

class Password:
    def __init__(self):
        self.length = 0
        self.letters = False
        self.special = False
        self.pwd = []

    def size_password(self):
        self.length = int(input("Enter the lenght: "))

        # Add number from 0 to 9 in a list with the length of what the user decided
        for i in range(self.length):
            i = random.randint(0, 9)
            self.pwd.append(i)

    def ask_letters(self):
        self.ans = str(input("Do we add letters ? (y/n) ")).lower()

        # If the user want to add letter, we add 1 or mutiple letters (randomise) in random positions
        if self.ans == 'y':
            self.letters = True
            # add multiple letter in the list
            rand_let = random.randint(1, self.length-2)

            for i in range(rand_let):
                rand_coord = random.randrange(self.length)
                letter = random.choice(string.ascii_uppercase)
                self.pwd[rand_coord] = letter


    def special_car(self):
        self.ans = str(input("Do we add special caracters ? (y/n) ")).lower()

        # If the user want to add speical characters , we add mutiple one or multiple characters (randomise) in random positions
        if self.ans == 'y':
            self.special = True
            rand_spe = random.randint(1, 5)

            # add multiple special in the list
            for i in range(rand_spe):
                rand_coord = random.randrange(self.length)
                special = random.choice(string.punctuation)
                self.pwd[rand_coord] = special

    # Convert the list into a str
    def convert(self):
        listToStr = ''.join([str(elem) for elem in self.pwd])
        print(f"Your generated password: {listToStr}")

    # Methods to call every others methods in the class
    def start(self):
        self.size_password()
        self.ask_letters()
        self.special_car()
        self.convert()


if __name__ == "__main__":
    obj = Password()
    obj.start()
