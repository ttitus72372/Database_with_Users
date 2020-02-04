import sqlite3

conn = sqlite3.connect('country.db')
c = conn.cursor()
'''
c.execute("DROP VIEW user_inputs")
c.execute("""CREATE VIEW  IF NOT EXISTS user_inputs AS
            SELECT country.id, country.name, country.uid
            FROM country
            LEFT JOIN users ON users.uid = country.uid;""")

conn.commit()



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
  for character in new_user:
    if character == ' ':
      print("There is a space in your passowrd, try again.")
      sign_up()
  new_password = input("\n Make a password between 3 and 20 characters and no spaces:\t")
  if len(new_password) < 3 or len(new_password) > 20:
    print("Your passowrd is less than 3 characters or longer than 20 characters, try again.")
    sign_up()
  for character in new_password:
    if character == ' ':
      print("There is a space in your passowrd, try again.")
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
    print("\n\t...Redirecting to login....\t")
    print("------------------------------")
    login()

def sign_in():
  choice = int(input("\nChoose an option:\nEnter 1 if you have used this database before.\nEnter 2 if you're new.\nYour option:\t "))
  if choice == 1:
    login()
  if choice == 2:
    sign_up()

def login():
  current_user = []
  username = input("Your Username:\t")
  for character in username:
    if character == ' ':
      print("There is a space in your username, try again.")
      login()
  password = input("Your password:\t")
  for character in password:
    if character == ' ':
      print("There is a space in your passowrd, try again.")
      login()
  pass_hash = hash(password)
  try:
    c.execute("SELECT name FROM users WHERE name=?", (username,))
    user = c.fetchall[0]
    c.execute("SELECT uid FROM users WHERE name=?", (username,))
    user_id = c.fetchall()[0]
    c.execute("SELECT password FROM users WHERE password=?", (pass_hash,))
    admin_check = c.fetchall()[0]
    current_user.append(user_id)
    current_user.append(admin_check)
    print("Welcome ", user, "\n")
    keepgoing(current_user)
    
  except:
    print("You have mistyped your Username or Password, try again.")
    login()

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

def keepgoing(user_check):
  choice = 0
  user_checks = user_check
  while choice != 5:
    choice = int(input("\nChoose an option." + "\n" + "1 to add a country" + "\n" + "2 to search for a specific country" + "\n" + "3 show all countries in the database" + "\n" + "4 to delete a country" + "\n" "5 to exit and logout.\n" + "\nYour option:\t"))
    if choice == 1:
      option1(choice, user_checks)
    elif choice == 2:
      option2(choice, user_checks)
    elif choice == 3:
      option3()
    elif choice == 4:
      option4(choice, user_checks)
    elif choice == 5:
      option5()
  

def option1(choice, user_check):
  user_option = choice
  current_option = option1
  user_checks = user_check
  uid = user_checks[0]
  add_country = input("\nType in the name of a country you wish to add:\n")
  
  #cleaning up user input
  newstring = cleanup(add_country, user_option)
  c.execute("SELECT * FROM country WHERE name=?", (newstring,))
  try:
    countries = c.fetchone()[1]
    print(countries, "is already in the database, try again.")
    current_option(user_option)
  except:
    c.execute("INSERT INTO country(name, uid) VALUES(?,?)", (newstring, uid,))
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
      
  
def option4(choice,user_check):
  user_option = choice
  user_checks = user_check
  c.execute("Select passowrd FROM users where uid = 1;")
  admin = c.fetchone()[0]
  if user_checks[1] != admin:
    print("You're not the admin, you can not delete records from the database!")
    keepgoing(user_checks)
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

