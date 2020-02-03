import sqlite3

conn = sqlite3.connect('country.db')
c = conn.cursor()

'''
c.execute("""CREATE TABLE IF NOT EXISTS users(
  uid integer PRIMARY KEY,
  name text,
  password text,
  UNIQUE(name)
)""")


c.execute(""" CREATE TABLE IF NOT EXISTS country (
  id integer PRIMARY KEY,
  name text NOT NULL,
  uid INTEGER REFERENCES users(uid), 
  UNIQUE(name)
)""")

admin = "admin"
password = "S3CR3T"
admin_pass = hash(password)
'''
def sign_up():
  new_user = input("\nCreate a username:\t")
  new_password = input("\n Make a password:\t")
  if len(new_password) < 3 or len(new_password) > 20:
    print("Your passowrd is less than 3 characters or longer than 20 characters, try again.")
    sign_up()
  new_pass_hash = hash(new_password)
  try:
    c.execute("SELECT * FROM users WHERE name=?", (new_user,))
    user = c.fetchone()[1]
    print(user, " is taken, try again.")
    sign_up()
  except:
    c.execute("INSERT INTO user(name, password) VALUES(?)", (new_user, new_pass_hash,))
    check_addition = new_user
    c.execute("SELECT * FROM country WHERE name=?", (check_addition,))
    check = c.fetchone()[1]
    print("You are in the database, ", check)
    conn.commit()

def sign_in():
  choice = int(input("\nChoose an option:\nEnter 1 if you have used this database before.\nEnter 2 if you're new.\nYour option:\t "))
  if choice == 1:
    login()
  if choice == 2:
    sign_up()

def login():
  username = input("Your Username:\t")
  password = input("Your password:\t")
  pass_hash = hash(password)
  try:
    c.execute("SELECT name FROM users WHERE name=?", (username,))
    user = c.fetchall[1]
    c.execute("SELECT password FROM users WHERE password=?", (pass_hash,))
    
    print("Welcome ", username)
'''
def cleanup(userInput, userChoice):
  if userChoice == 1:
    current_option = option1
  if userChoice == 2:
    current_option = option2
  if userChoice == 4:
    current_option = option4

  #inital cleanup of the user's input
  newstring = ''
  position = 1
  for a in userInput:
    if (a.isnumeric()) == False:
      if a != ' ':
        if (a.isalpha()) == True:
          if (a.isupper()) == True and position == 1:
            newstring += a
            position += 1
          elif (a.isupper()) == True and position != 1:
            newstring += (a.lower())
            position += 1
          elif (a.islower()) == True and position == 1:
            newstring += (a.upper())
            position +=1
          elif (a.islower()) == True and position != 1:
            newstring += a
            position += 1
        elif (a.isalpha()) == False:
          return print("You have entered an invalid cahracter, tray again."), current_option(userChoice)
      elif a == ' ' and position == 1:
        return print("\nThe first character of your entry was a space, try again."), current_option(userChoice)
      elif a == ' ':
        newstring += a
        position += 1
    elif (a.isnumeric()) == True:
      return print("\nThat is an invalid input, try again."), current_option(userChoice)
  

#further cleanup before returning for database use
  current_position = 0
  
  final_string = ''
  for character in newstring:
    if (character.isalpha()) == True and newstring[current_position - 1] == ' ':
      final_string += (character.upper())
      current_position += 1
    elif character == ' ' and newstring[-1] == ' ':
      return print("The entry ends with a space, try again."), current_option(userChoice)
    elif character == ' ' and newstring[current_position - 1] == ' ':
      return print("\nYou have to many spaces, try again."), current_option(userChoice)
    elif character == " ":
      final_string += character
      current_position += 1
    elif (character.isalpha()) == True:
      final_string += character
      current_position += 1
  
  return final_string

def keepgoing():
  choice = 0
  while choice != 5:
    choice = int(input("\nChoose an option." + "\n" + "1 to add a country" + "\n" + "2 to search for a specific country" + "\n" + "3 show all data in the database" + "\n" + "4 to delete a country" + "\n" "5 to exit.\n" + "\nYour option:\t"))
    if choice == 1:
      option1(choice)
    elif choice == 2:
      option2(choice)
    elif choice == 3:
      option3()
    elif choice == 4:
      option4(choice)
    elif choice == 5:
      option5()
  

def option1(choice):
  user_option = choice
  current_option = option1
  add_country = input("\nType in the name of a country you wish to add:\n")
  
  #cleaning up user input
  newstring = cleanup(add_country, user_option)
  c.execute("SELECT * FROM country WHERE name=?", (newstring,))
  try:
    countries = c.fetchone()[1]
    print(countries, "is already in the database, try again.")
    current_option(user_option)
  except:
    c.execute("INSERT INTO country(name) VALUES(?)", (newstring,))
    check_addition = newstring
    c.execute("SELECT * FROM country WHERE name=?", (check_addition,))
    check = c.fetchone()[1]
    print(check, "was added to the database.\n")
    conn.commit()
  
  

def option2(choice):
  user_option = choice
  search_country = input("\nType in the country you wish to search for:\n")
  #cleaning up user input
  newstring = cleanup(search_country, user_option)
  c.execute("SELECT * FROM country WHERE name=?", (newstring,))
  try:
    countries = c.fetchone()[1]
    print(countries, "was found.")
  except:
    print("That country is not in the database.")
def option3():
  c.execute("SELECT name FROM country")
  print("\nThe countries currently in the database are:")
  print("-------------------")
  for row in c.fetchall():
    for item in row:
      item = row[0]
      print(item)
  print('\n')
      
  
def option4(choice):
  user_option = choice
  remove_country = input("\nType in the name of a country you wish to delete:\n")
  #cleaning up user input
  newstring = cleanup(remove_country, user_option)
  #double checking to make sure the contry submitted is in the database
  c.execute("SELECT * FROM country WHERE name=?", (newstring,))
  try:
    country = c.fetchone()[1]
    if country is not None:
      c.execute("DELETE FROM country WHERE name=?", (newstring,))
      conn.commit()
      print(newstring, "was deleted.\n")
  except:
    print("That country is not in the database.")
  
def option5():
  conn.commit()
  conn.close()
  quit("Done")
keepgoing()
'''
