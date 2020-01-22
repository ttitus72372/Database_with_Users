import sqlite3

conn = sqlite3.connect('country.db')
c = conn.cursor()
'''
c.execute(""" CREATE TABLE IF NOT EXISTS country (
  id integer PRIMARY KEY,
  name text NOT NULL, 
  UNIQUE(name)
);""")
'''

def keepgoing():
  choice = 0
  while choice != 5:
    choice = choice = int(input("Choose an option." + "\n" + "1 to add a country" + "\n" + "2 to search for a specific country" + "\n" + "3 show all data in the database" + "\n" + "4 to delete a country" + "\n" "5 to exit." + "\n"))
    if choice == 1:
      option1()
    elif choice == 2:
      option2()
    elif choice == 3:
      option3()
    elif choice == 4:
      option4()
    elif choice == 5:
      option5()

def option1():
  add_country = input("\nType in the name of a country you wish to add:\n")
  #cleaning up user input
  newstring = ''
  position = 1
  if (add_country.isalpha()) == True:
    for a in add_country:
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
    c.execute("INSERT INTO country(name) VALUES(?)", (newstring,))
    check_addition = newstring
    c.execute("SELECT * FROM country WHERE name=?", (check_addition,))
    check = c.fetchone()[1]
    print(check, "was added to the database.\n")
    conn.commit()
  else:
    print("\nYou included an invalid character, try again.")
    option1()

def option2():
  search_country = input("\nType in the country you wish to search for:\n")
  #cleaning up user input
  newstring = ''
  position = 1
  if (search_country.isalpha()) == True: 
    for a in search_country:
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
    c.execute("SELECT * FROM country WHERE name=?", (newstring,))
    try:
      countries = c.fetchone()[1]
      print(countries, "was found.")
    except:
      print("That country is not in the database.")
  else:
    print("\nYou included an invalid character, try again.")
    option2()
def option3():
  c.execute("SELECT name FROM country")
  print("\nThe countries currently in the database are:")
  print("-------------------")
  for row in c.fetchall():
    for item in row:
      item = row[0]
      print(item)
  print('\n')
      
  
def option4():
  remove_country = input("\nType in the name of a country you wish to delete:\n")
  #cleaning up user input
  newstring = ''
  position = 1
  if (remove_country.isalpha()) == True:
    for a in remove_country:
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
  else:
    print("\nYou included an invalid character, try again.")
    option4()
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
option1()
option2()
option3()
option4()
option5()
