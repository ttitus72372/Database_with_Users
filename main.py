import sqlite3
import hashlib
import os
import cleanup

conn = sqlite3.connect('country.db')
c = conn.cursor()

def sign_in():
  print("Welcome to the Simple Countries Database!")
  choice = int(input("\nChoose an option:\nEnter 1 if you have used this database before.\nEnter 2 if you're new.\nYour option:\t "))
  if choice == 1:
    login()
  if choice == 2:
    sign_up()

def sign_up():
  print("\nWelcome new user, please create a username and password for yourself.")
  new_user = input("\nCreate a username:\t")
  cleaned_user = cleanup.username(new_user)
  if cleaned_user == 1:
    print("There is a space in the username.")
    sign_up()
  elif cleaned_user == 2:
    print("There is a special character in your username.")
    sign_up()
  new_password = input("\n Make a password between 3 and 20 characters and no spaces:\t")
  if len(new_password) < 3 or len(new_password) > 20:
    print("Your passowrd is less than 3 characters or longer than 20 characters, try again.")
    sign_up()
  for character in new_password:
    if character == ' ':
      print("There is a space in your passowrd, try again.")
      sign_up()
    else:
      c.execute("SELECT * FROM users WHERE name=?", (cleaned_user,))
      try:
        user = c.fetchone[1]
        print(user, "as a username is already taken.")
        sign_up()
      except:
        salt = os.urandom(32)
        new_pass_hash = hashlib.pbkdf2_hmac('sha256', new_password.encode('utf-8'), salt, 100000)
        c.execute("INSERT INTO users(name, password, usn) VALUES(?,?,?)", (cleaned_user, new_pass_hash, salt,))
        conn.commit()
        print("\n\t...Redirecting to login....\t")
        print("------------------------------")
        login()

def login():
  current_user = []
  print("\n....Login....\n")
  username = input("Your Username:\t")
  cleaned_username = cleanup.username(username)
  if cleaned_username == 1:
    print("There is a space in the username.")
    login()
  elif cleaned_username == 2:
    print("There is a special character in your username.")
    login()
  c.execute("SELECT usn FROM users WHERE name=?", (cleaned_username,))
  salt = c.fetchone()[0]
  #print("Checking the salt:", salt)
  password = input("Your password:\t")
  for character in password:
    if character == ' ':
      print("There is a space in your passowrd, try again.")
      login()
  pass_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
  c.execute("SELECT password FROM users WHERE name=?", (cleaned_username,))
  stored_password = c.fetchone()[0]
  if pass_hash == stored_password:
    c.execute("SELECT uid FROM users WHERE name=?", (cleaned_username,))
    user_id = c.fetchone()[0]
    current_user.append(user_id)
    current_user.append(stored_password)
    print("Welcome", cleaned_username, "\n")
    print("Loading main menu.......")
    keepgoing(current_user)
  if pass_hash != stored_password:
    print("Your password is incorrect.")
    login()

def keepgoing(user_check):
  choice = 0
  user_checks = user_check
  while choice != 10:
    choice = int(input("\nChoose an option." + "\n 1. To add a country" + "\n 2. To search for a specific country" + "\n 3. To show all countries in the database" + "\n 4. To delete a country" + "\n 5. To show all users" +"\n 6. To show which country was added by which user."+"\n 7. To search for a specific user."+"\n 8. To delete a user."+"\n 9. To logout and switch users."+"\n 10. To logout and close the database connection."+"\nYour option:\t"))
    if choice == 1:
      option1(user_checks)
    elif choice == 2:
      option2()
    elif choice == 3:
      option3()
    elif choice == 4:
      option4(user_checks)
    elif choice == 5:
      option5()
    elif choice == 6:
      option6()
    elif choice == 7:
      option7()
    elif choice == 8:
      option8(user_checks)
    elif choice == 9:
      option9(user_checks)
    elif choice == 10:
      option10()
  
def option1(user_check):
  uid = user_check[0]
  add_country = input("\nType in the name of a country you wish to add:\n")
  
  #cleaning up user input
  newstring = cleanup.country(add_country)
  if newstring == 1:
    print("You have entered an invalid cahracter, tray again.")
    option1(uid)
  elif newstring == 2:
    print("\nThe first character of your entry was a space, try again.")
    option1(uid)
  elif newstring == 3:
    print("\nThat is an invalid input, try again.")
    option1(uid)
  elif newstring == 4:
    print("The entry ends with a space, try again.")
    option1(uid)
  elif newstring == 5:
    print("\nYou have to many spaces, try again.")
    option1(uid)
  
  c.execute("SELECT * FROM country WHERE name=?", (newstring,))
  try:
    countries = c.fetchone()[1]
    print(countries, "is already in the database, try again.")
    option1(uid)
  except:
    c.execute("INSERT INTO country(name, uid) VALUES(?,?)", (newstring, uid,))
    check_addition = newstring
    c.execute("SELECT * FROM country WHERE name=?", (check_addition,))
    check = c.fetchone()[1]
    print(check, "was added to the database.\n")
    conn.commit()
  
def option2():
  search_country = input("\nType in the country you wish to search for:\n")
  #cleaning up user input
  newstring = cleanup.country(search_country)
  if newstring == 1:
    print("You have entered an invalid cahracter, tray again.")
    option2()
  elif newstring == 2:
    print("\nThe first character of your entry was a space, try again.")
    option2()
  elif newstring == 3:
    print("\nThat is an invalid input, try again.")
    option2()
  elif newstring == 4:
    print("The entry ends with a space, try again.")
    option2()
  elif newstring == 5:
    print("\nYou have to many spaces, try again.")
    option2()

  c.execute("SELECT * FROM country WHERE name=?", (newstring,))
  try:
    countries = c.fetchone()[1]
    print(countries, "is in the database.")
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
      
def option4(user_check):
  user_pass = user_check[1]
  c.execute("Select password FROM users WHERE uid =1")
  admin = c.fetchone()[0]
  if user_pass != admin:
    print("You're not the admin, you can not delete records from the database!")
    print("Redirecting to main menu.......\n")
    keepgoing(user_check)
  remove_country = input("\nType in the name of a country you wish to delete:\n")
  #cleaning up user input
  newstring = cleanup.country(remove_country)
  if newstring == 1:
    print("You have entered an invalid cahracter, tray again.")
    option3(user_check)
  elif newstring == 2:
    print("\nThe first character of your entry was a space, try again.")
    option3(user_check)
  elif newstring == 3:
    print("\nThat is an invalid input, try again.")
    option3(user_check)
  elif newstring == 4:
    print("The entry ends with a space, try again.")
    option3(user_check)
  elif newstring == 5:
    print("\nYou have to many spaces, try again.")
    option3(user_check)
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
  c.execute("SELECT name FROM users")
  print("\nAll users in the database:")
  print("-------------------")
  for row in c.fetchall():
    for item in row:
      item = row[0]
      print(item)
  print('\n')

def option6():
  c.execute("SELECT country, user FROM user_inputs")
  print("\nCounty\t\t\tAdded by")
  print("------------------------")
  for row in c.fetchall():
    for item in row:
      country = row[0]
      user = row[1]
    print(country,"\t\t\t",user)
    print("------------------------")

def option7():
  search_user = input("\nType in the username you wish to search for:\n")
  #cleaning up user input
  cleaned_username = cleanup.username(search_user)
  if cleaned_username == 1:
    print("There is a space in the username.")
    option7()
  elif cleaned_username == 2:
    print("There is a special character in the username.")
    option7()
  c.execute("SELECT * FROM users WHERE name=?", (cleaned_username,))
  try:
    user = c.fetchone()[1]
    print(user, "is in the database.")
  except:
    print("That user is not in the database.")

def option8(user_check):
  user_pass = user_check[1]
  c.execute("Select password FROM users WHERE uid =1")
  admin = c.fetchone()[0]
  if user_pass != admin:
    print("You're not the admin, you can not delete records from the database!")
    print("Redirecting to main menu.......\n")
    keepgoing(user_check)
  remove_user = input("\nType in the name of a user you wish to delete:\n")
  #cleaning up user input
  user_clean = cleanup.username(remove_user)
  if user_clean == 1:
    print("There is a space in the username.")
    option7()
  elif user_clean == 2:
    print("There is a special character in the username.")
    option7()
  #double checking to make sure the user submitted is in the database
  
  c.execute("SELECT uid FROM users WHERE name=?", (user_clean,))
  uid = c.fetchone()[0]

  if uid == user_check[0]:
    print("The Admin can not be deleted!")
    print("Booting to main menu.....")
    keepgoing(user_check)
  c.execute("SELECT * FROM users WHERE name=?", (user_clean,))
  try:
    user = c.fetchone()[1]
    if user is not None:
      c.execute("DELETE FROM users WHERE name=?", (user_clean,))
      conn.commit()
      print(user_clean, "was deleted.\n")
  except:
    print("That user is not in the database.")

def option9(user_check):
  uid = user_check[0]
  c.execute("SELECT name FROM users WHERE uid=?",(uid,))
  user = c.fetchone()[0]
  print("Logging out....")
  print("Goodbye,", user)
  print()
  sign_in()

def option10():
  conn.commit()
  conn.close()
  quit("Done")

sign_in()

'''
def name_formating(name, choice):
  if choice == 1:
    menu_option = login
  if choice == 2:
    menu_option = sign_up
  if choice == 7:
    menu_option = option7
  if choice == 8:
    menu_option = option8
    
  
  clean_name = name.capitalize()
  for x in clean_name:
    if x == " ":
      return print("There was a space in the username."), menu_option(choice)
  if clean_name.isalnum() == False:
    return print("There is a special character in the username. You typed", name), menu_option(choice)
  elif clean_name.isalnum() == True:
    return clean_name

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
'''