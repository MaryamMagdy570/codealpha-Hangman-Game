import random
import os

os.system('cls')

def Display_state(trials):
  print("  __________")
  print("  |        |")
  if(trials == 0):
    print("  |")
    print("  |")
    print("  |") 
  elif(trials == 1):
    print("  |        O")
    print("  |")
    print("  |") 
  elif(trials == 2):
    print("  |        O")
    print("  |        |")
    print("  |") 
  elif(trials == 3):
    print("  |        O")
    print("  |        |\\")
    print("  |") 
  elif(trials == 4):
    print("  |        O")
    print("  |       /|\\")
    print("  |") 
  elif(trials == 5):
    print("  |        O")
    print("  |       /|\\")
    print("  |         \\")
  elif(trials == 6):
    print("  |        O")
    print("  |       /|\\")
    print("  |       / \\")
  
  print("  |")
  print("__|__",end="\t\t")

movies = [
    "Harry Potter and the Sorcerer's Stone",
    "Harry Potter and the Chamber of Secrets",
    "Harry Potter and the Prisoner of Azkaban",
    "Harry Potter and the Goblet of Fire",
    "Harry Potter and the Order of the Phoenix",
    "Harry Potter and the Half-Blood Prince",
    "Harry Potter and the Deathly Hallows: Part 1",
    "Harry Potter and the Deathly Hallows: Part 2",
    "Memento",
    "Insomnia",
    "Batman Begins",
    "The Prestige",
    "The Dark Knight",
    "Inception",
    "The Dark Knight Rises",
    "Interstellar",
    "The Shawshank Redemption",
    "12 Angry Men",
    "Schindler's List",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Lord of the Rings: The Fellowship of the Ring",
    "Fight Club",
    "Forrest Gump",
    "Star Wars: Episode V - The Empire Strikes Back",
    "The Lord of the Rings: The Two Towers",
    "The Matrix",
    "Goodfellas",
    "One Flew Over the Cuckoo's Nest",
    "Seven Samurai",
    "The Silence of the Lambs",
    "It's a Wonderful Life",
    "Life Is Beautiful",
    "The Usual Suspects",
    "Saving Private Ryan",
    "Spirited Away",
    "The Green Mile",
    "The Departed",
    "The Pianist",
    "Gladiator",
    "The Lion King",
    "The Intouchables",
    "Back to the Future",
    "Whiplash",
    "The Lives of Others",
    "The Shining",
    "Django Unchained",
    "Alien",
    "Cinema Paradiso",
    "Apocalypse Now",
    "The Great Dictator",
    "The Sting",
    "The Godfather",
    "Reservoir Dogs",
    "Braveheart",
    "Requiem for a Dream",
    "Toy Story",
    "To Kill a Mockingbird",
    "The Truman Show",
    "A Clockwork Orange",
    "Monty Python and the Holy Grail",
    "The Wizard of Oz",
    "The Apartment",
    "Snatch",
    "The Princess Bride",
    "The Elephant Man",
    "Raiders of the Lost Ark",
    "The Terminator",
    "The Big Lebowski",
    "No Country for Old Men",
    "Heat",
    "Gone with the Wind",
    "Casino",
    "The Sixth Sense",
    "The Graduate",
    "Gran Torino",
    "The Maltese Falcon",
    "Finding Nemo",
    "Trainspotting",
    "Fargo",
    "Jurassic Park",
    "Stand by Me",
    "The Thing",
    "V for Vendetta",
    "Twelve Monkeys",
    "Butch Cassidy and the Sundance Kid",
    "Mary and Max",
    "The Night of the Hunter",
    "The Exorcist",
    "Lock, Stock and Two Smoking Barrels",
    "Blade Runner",
    "The Grand Budapest Hotel",
    "Donnie Darko",
    "The Social Network",
    "Raging Bull",
    "The King's Speech",
    "Groundhog Day",
    "The Deer Hunter",
    "Gone Girl",
    "The Best Years of Our Lives",
    "How to Train Your Dragon",
    "12 Years a Slave",
    "The 400 Blows",
    "Million Dollar Baby",
    "Network",
    "Gandhi",
    "A Beautiful Mind",
    "The Bourne Ultimatum",
    "Donnie Brasco",
    "Jaws",
    "The Princess Diaries",
    "Slumdog Millionaire",
    "Mystic River",
    "The Passion of the Christ",
    "The Sound of Music",
    "The Girl with the Dragon Tattoo",
    "Hotel Rwanda",
    "Casablanca",
    "The Avengers",
    "The Exorcist",
    "The Big Lebowski",
    "The Shawshank Redemption",
    "City Lights",
    "To Kill a Mockingbird",
    "Chinatown",
    "It's a Wonderful Life",
    "Shakespeare in Love",
    "Apocalypse Now",
    "Gravity",
    "The Hurt Locker",
    "The Hunger Games",
    "Little Women"
]

random_item = random.choice(movies)

space_count = random_item.count(' ')
sub_words = random_item.split(" ")

trials = 0
gussed=""
for i in range(0,space_count+1):
  gussed=gussed+("_" * len(sub_words[i]))+' '
Display_state(trials)
print(gussed)
print("===========================================================================\n")

previous_chars=[]
loser = 0;
while "_" in gussed:
  
  if previous_chars and (not repeated):
    print("Entered characters: ",previous_chars)
  
  char = input("Enter your guess: ")
  char = char.casefold();

  if char == ' ':
    continue

  if char in previous_chars:
    print("\nyou have entered this character before,\n please, enter another character.\n")
    repeated = 1
    continue
  else:
    repeated = 0
    previous_chars.extend(list(char))
  
  found = 0;
  for i,c in enumerate(random_item):
    if (c.casefold() == char):
      gussed = gussed[:i]+random_item[i]+gussed[i+1:]
      found = 1;
  
  if (not found):
    trials=trials+1

  os.system('cls')
  Display_state(trials)
  print(gussed)
  print("===========================================================================")

  if trials==6:
    loser = 1
    break;  
  
if (loser):
  print("\nGame Over, the movie is: ",random_item,"\n")
else:
  print("\nCongratuations, you won\n")




