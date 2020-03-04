def username(name):
  error = 0
  clean_name = name.capitalize()
  for x in clean_name:
    if x == " ":
      error = 1
      return error
  if clean_name.isalnum() == False:
    error = 2
    return error
  elif clean_name.isalnum() == True:
    return clean_name

def country(userInput):
  error = 1
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
          error = 1
          return error
      elif a == ' ' and position == 1:
        error = 2
        return error
      elif a == ' ':
        newstring += a
        position += 1
    elif (a.isnumeric()) == True:
      error = 3
      return error
  
  current_position = 0
  
  final_string = ''
  for character in newstring:
    if (character.isalpha()) == True and newstring[current_position - 1] == ' ':
      final_string += (character.upper())
      current_position += 1
    elif character == ' ' and newstring[-1] == ' ':
      error = 4
      return error
    elif character == ' ' and newstring[current_position - 1] == ' ':
      error = 5
      return error
    elif character == " ":
      final_string += character
      current_position += 1
    elif (character.isalpha()) == True:
      final_string += character
      current_position += 1
  
  return final_string