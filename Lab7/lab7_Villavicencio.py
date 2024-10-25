"""
Michael Villavicencio
Sep 23, Python Files
"""

fileusers = open("users.txt", "r")

print("\n --------------- Example 2: Python Limit to Read Files -------------")
print(fileusers.read(10))

print("\n --------------- Example 1: Python Files -------------")

# Reset file pointer to the beginning
fileusers.seek(0)
print(fileusers.read())

fileusers.close()

print("\n --------------- Example 3: Python read files with 'with' and 'r' -------------")
with open("users.txt", "r") as fileusers:
    eachline = fileusers.readlines()
    print(eachline[2])

print("\n --------------- Example 4: Python read files with 'split()' -------------")
with open("users.txt", "r") as fileusers:
    eachline = fileusers.readlines()
    for line in eachline:
        word = line.split()
        if len(word) > 2:
            print(word[2])

print("\n --------------- Example 5: Python read file and check for a specific item -------------")
# Loop through the 'users.txt' file and check how many users are named 'Bruce'
with open("users.txt", "r") as fileusers:
    eachline = fileusers.readlines()
    usercounter = 0
    for line in eachline:
        word = line.split()
        for eachword in word:
            if eachword == "Bruce":  # Compare individual words to "Bruce"
                usercounter += 1
    print(f"There are {usercounter} users with the name 'Bruce'")

print("\n --------------- Example 5.2 -------------")
print("\n--------- Example 5: Python read file and check for a specific item ---------")

def finduser(textfile, username):
    with open(textfile, "r") as fileusers:
        eachlines = fileusers.readlines()
        usercounter = 0
        for line in eachlines:
            word = line.split()
            for eachword in word:
                if eachword == username:
                    usercounter += 1
        return usercounter

user = "Tony"
usercount = finduser("users.txt", user)
print(f"There is {usercount} with the name '{user}'")

print("\n --------------- Example 6: Python with file -------------")
def userreport(totalcount, username):
    with open("writeresult.txt", "w") as writeuserresult:
        writeuserresult.write(f"There is {totalcount} with name '{username}")

userreport(usercount, user)

print("\n --------------- Example 7: Python appending data into a file -------------")
def appenduser(newuser, city, age, userfilename):
    try:
        with open(userfilename, "a") as fileusers:
            fileusers.write(f"\n{newuser} from {city} is {age} years")
    except IOError:
        print("Error: unable to open file named {userfilename}")

appenduser("John", "New York", 30, "users.txt")