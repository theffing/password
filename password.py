# Takes in input, how many characters the password is
# Password must include, at least, one special character
# one uppercase character, one lowercase character, and one number
# Must then save the password in a specified folder and take in input to name it
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
special = "!@#$%^&*()_+"
characters = [lower, upper, num, special]

def main():
    print("Input Desired Password Length:         *Must be 4 or more*")
    length = int(input())
    if length < 4:
        main()
    password = generator(length)
    print(password)

    print("Input Pre-existing password file or Name for New File:")
    filename = input()
    print("Input username Associated with Password:")
    username = input()
    print("Input website Associated with username and password:")
    website = input()

    try:
        with open(f"{filename}.txt", "a") as file:
            file.write(f"\n\n{website}\nUser: {username}\nPassword: {password}")
    except:
        print("File Error, Try Again")
        main()

def generator(length):
    password = ""
    visited = [False, False, False, False]
    while len(password) < length:
        index = random.randrange(4)
        if visited[index] == False:
            char = random.choice(characters[index])
            visited[index] = True
            password += char
        else:
            if visited[0] and visited[1] and visited[2] and visited[3]:
                visited[0] = False
                visited[1] = False 
                visited[2] = False 
                visited[3] = False
            pass
    return password

if __name__ == '__main__':
    main()