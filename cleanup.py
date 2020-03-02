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