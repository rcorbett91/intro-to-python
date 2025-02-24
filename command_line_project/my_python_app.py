days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def add():
  
  add_choice1 = ""
  add_date = ""
  add_list = []

  while add_date.title() not in days:
    add_date = input("\tEnter the day you want to add time for: ")
    if add_date.title() in days:
      x_code = input("\tEnter the timesheet code to add time to: ")
      x_hours = input("\tEnter time worked in hours (X.XX) for " + x_code.title() + ": ")
      x_entry = x_hours + " hrs - " + x_code.title()
      add_item1 = "Days/"+add_date+".txt"
      f = open(add_item1, "w")
      f.write("\t"+x_entry+"\n")
      f.close
    else:
      print("\tSorry, I didn't get that properly. ")
    while add_choice1.upper() != "N":
      add_choice1 = input("\tDo you want to add more time to this day? ")
      if add_choice1.upper() == "Y":
        x_code = input("\tEnter the timesheet code to add time to: ")
        x_hours = input("\tEnter time worked in hours (X.XX) for " + x_code.title() + ": ")
        x_entry = x_hours + " hrs - " + x_code.title()
        add_list.append(x_entry)
      elif add_choice1.upper() != "N":
        print("\tSorry, I didn't get that properly. ")
      for item in add_list:
        add_item = "Days/"+add_date+".txt"
        f = open(add_item, "a")
        f.write("\t"+item+"\n")
        f.close
      add_list.clear()
  
def view():
  print("\t---------------------------------\n\n\tYour weekly timesheet notes:\n")
  for x in days:
      file_x = "Days/"+str(x)+".txt"
      f = open(file_x, "r")
      print("\t"+x+":")
      print(f.read())
      f.close
  print("\t---------------------------------")

def clear_all():
  print("\t---------------------------------\n")
  for x in days:
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