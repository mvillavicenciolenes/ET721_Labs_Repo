"""
Michael Villavicencio
ET 721
"""

print("\n--------------- Example 1: Dictionary ---------------------")
car = {
    "Brand": "Tesla",
    "Model": "S",
    "Year": 2023,
    "Color": "Red",
    "Price": 79999,
    "Electric": True
}

print(f"Best car of 2022 = {car['Brand']}, model = {car['Model']}")

print("\n-------- Example 2: Loop through each key in a dictionary -----------")
for k in car:
    print(f"{k} has a value of {car[k]}")  # print each key

print("\n--------------- Example 3: Amount of key-pair in a dictionary --------------")
print(f"Dictionary has {len(car)} key-value pairs")

print("\n--------------- Example 4: Remove a key-value pair from a dictionary --------------")
car.pop("Year")
print(f"Dictionary after removing the 'Year' key: {car}")
for k in car:
    print(f"{k}, {car[k]}")

print("\n--------------- Example 5: Get the value of a key --------------")
look_key = "last_visit"
print(f"The value of key {look_key} is {car.get(look_key)}")

print("\n--------------- Example 6: Store data in a dictionary --------------")
phrase = "to be or not to be"
phrase = phrase.split()
print(f"Phrase after the split method {phrase}")
word_count_dict = {}  # empty dictionary 

# for loop to count how many times a word is in the dictionary 
for word in phrase:
    if word not in word_count_dict:
        word_count_dict[word] = 1
    else:
        word_count_dict[word] += 1

print(word_count_dict)

print("\n ---------- Exercise ----------------")

# Given the following user list, find the number of users that use 'gmail', 'hotmail', 'yahoo', and 'swamp'
user = """
    peter = ppan@gmail.com
    diana = d@gmail.com
    Kent = ckent@hotmail.com
    Bruce = bwayne@hotmail.com
    tony = tstark@gmail.com
    shrek = shrek@swamp.com
    harry = harry.potter@swamp.com
    tony_stark = tony.stark@hotmail.com
    bruce_wayne = bruce.wayne@gmail.com
    neo = neo@gmail.com
    joker = joker@hotmail.com
    frodo = frodo.baggins@swamp.com
    vader = darth.vader@hotmail.com
    yoda = yoda@swamp.com
    terminator = terminator@gmail.com
    gandalf = gandalf.thegrey@swamp.com
    buzz = buzz.lightyear@gmail.com
    agent_smith = agent.smith@hotmail.com
"""

# Split user string into entries by line
user_list = user.strip().split('\n')

# Initialize dictionary for domain counts
domain_count_dict = {'gmail': 0, 'hotmail': 0, 'yahoo': 0, 'swamp': 0}

# Loop through each email entry
for entry in user_list:
    if '=' in entry:  # Check if '=' is in the entry
        # Clean up the entry and extract the email
        email = entry.split('=')[1].strip()
        if '@' in email:  
            domain = email.split('@')[1].split('.')[0] 
            if domain in domain_count_dict:
                domain_count_dict[domain] += 1

# Print domain counts
print(domain_count_dict)
