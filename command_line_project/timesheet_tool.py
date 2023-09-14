workdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def add():
  date_to_add = ""
  add_more_time = ""
  entries_to_append = []
  
  while date_to_add.title() not in workdays:
    date_to_add = input("\tEnter the day you want to add time for: ")
    if date_to_add.title() in workdays:
      x_code = input("\tEnter the timesheet code to add time to: ")
      x_hours = input("\tEnter time worked in hours (X.XX) for " + x_code.title() + ": ")
      x_entry = x_hours + " hrs - " + x_code.title() 
      add_item1 = "Days/"+date_to_add+".txt"
      f = open(add_item1, "w")
      f.write("\t"+x_entry+"\n")
      f.close
    else:
      print("\tSorry, I didn't get that properly. ")
    while add_more_time.upper() != "N":
      add_more_time = input("\tDo you want to add more time to this day? ")
      if add_more_time.upper() == "Y":
        x_code = input("\tEnter the timesheet code to add time to: ")
        x_hours = input("\tEnter time worked in hours (X.XX) for " + x_code.title() + ": ")
        x_entry = x_hours + " hrs - " + x_code.title()
        entries_to_append.append(x_entry)
      elif add_more_time.upper() != "N":
        print("\tSorry, I didn't get that properly. ")
    for item in entries_to_append:
      add_item = "Days/"+date_to_add+".txt"
      f = open(add_item, "a")
      f.write("\t"+item+"\n")
      f.close
    entries_to_append.clear()
  
def view():
  print("\t---------------------------------\n\n\tYour weekly timesheet notes:\n")
  for x in workdays:
      file_x = "Days/"+str(x)+".txt"
      f = open(file_x, "r")
      print("\t"+x+":")
      print(f.read())
      f.close
  print("\t---------------------------------")

def clear_all():
  print("\t---------------------------------\n")
  for x in workdays:
      file_x = "Days/"+str(x)+".txt"
      f = open(file_x, "w")
      f.write("\tNo time entered yet for this day.\n")
      f.close
  print("\tAll timesheet entries have been cleared.\n\n\t---------------------------------")

def time_tool():
  
  print("\n\tWelcome to the timesheet notes tool! ")

  chosen_option = ""
  while chosen_option.upper() != "D":
    chosen_option = input("\n\tPlease select an option: \n\t(A)\tAdd time to your timesheet notes \n\t(B)\tView your current timesheet notes \n\t(C)\tClear all timesheet note entries \n\t(D)\tExit the timesheet notes tool\n")
    add_choice2 = ""
    if chosen_option.upper() == "A":
      add()
      while add_choice2.upper() != "N":
        add_choice2 = input("\tWould you like to add time for a different day? (Y/N) ")
        if add_choice2.upper() == "Y":
          add()
        elif add_choice2.upper() != "N":
          print("\tSorry, I didn't get that properly. ")
    elif chosen_option.upper() == "B":
      view()
    elif chosen_option.upper() == "C":
      clear_all()
    elif chosen_option.upper() == "D":
      print("\tThanks for using the timesheet notes tool!\n")
    else:
      print("\tSorry, I didn't get that properly.")

time_tool()