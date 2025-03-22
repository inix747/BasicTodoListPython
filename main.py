import os

print("MY TODO LIST!! by Adam Stewart")
print(r"""                   __..._   _...__
              _..-"      `Y`      "-._
              \           |           /
              \\   TODO   |          //
              \\\         |         ///
               \\\ _..---.|.---.._ ///
                \\`_..---.Y.---.._`//
                 '`               `'""")

print("\n")

while True:
    currentToDo = open("ToDo.txt","r")
    content = currentToDo.readlines()
    currentToDo.close()
    check = ""

    if (content == []):
        print("There is nothing in your toDO list.")
    else:
        print("\nHere is a list of all the items on your toDo list: ")
        print("\n")
        for i in range(0,len(content)):
            print("     " + str(i+1) + ")" + " " + content[i] + "\n")
        print("\n")
    
    print("\nDo you wish to modify your toDo list?")
    check = input("(y/n):: ")

    if (check=="y"):
        print("\nRemove, Add or Nuke (remove everything): ")
        check = input("(add/remove/nuke):: ")
        currentToDo = open("ToDo.txt","w")
        if(check.lower()=="add"):
            print("\nWhat is it you wish to add? ")
            toDoItem = input("type:: ")
            for i in range(0,len(content)):
                currentToDo.write(content[i])
            if (content==[]):
                currentToDo.write(toDoItem)
            else:
                currentToDo.write("\n"+toDoItem)
            currentToDo.close()
            print("\nIs that everything for now? ")
            check = input("(y/n):: ")
            if (check.lower()=="y"):
                break
        elif (check=="nuke"):
            print("\nAre you sure you want to nuke your ToDo list (this will delete everything in it.)??")
            check = input("(y/n):: ")
            if (check=="y"):
                currentToDo.write("")
                currentToDo.close()
                print("Your ToDo list has been nuked :)")
                print(r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⠀⠉⠢⢀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡁⠀⠀⠀⠀⠀⠑⠠⡀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠑⢄⡀⠀⠀⠀⠀⠈⠑⢄⡀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⣀⣰⢉⣦⣄⠀⠀⠀⠀⠀⠈⢢
                ⠀⠀⠀⠀⠀⠀⠀⠀⡠⠐⠊⠁⠀⢩⣿⣯⡶⠃⠢⡀⠀⠀⡠⠊
                ⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⢠⡟⠁⢹⠀⡀⠄⠚⠑⠒⠁⠀
                ⠀⠀⠀⢀⠎⠉⠂⢄⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⡰⠁⠀⠀⠀⠀⠁⠢⢀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⣘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⡀⡘⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠰⠁⠁⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⡇⠀⠀⠀⠀⠑⠄⡀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⢣⠀⠀⠀⠀⠀⠀⠈⠐⠄⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠈⠆⡀⠀⠀⠀⠀⢀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠉⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
            else:
                print("Okay be careful :))")
                for i in range(0,len(content)):
                    currentToDo.write(content[i])
        
        elif (check=="remove"):
            print("\nWhich line do you wish to remove? ")
            check = int(input("(1,2,3...):: "))
            print("Deleting line " + str(check) + " -> " + "(" + (content[check-1])[:4] + "..."  + ")")
            for i in range(0,len(content)):
                if (i != check-1):
                    currentToDo.write(content[i])
            currentToDo.close()
            print("\n Is that everything for now? ")
            check = input("(y/n):: ")
            if (check=="y"):
                break
        else:
            print("EEK invalid option sorry >w<")
            for i in range(0,len(content)):
                currentToDo.write(content[i])
        
    elif(check == "n"):
        break
    else:
        print("Woops Invalid option :(")
print("\n Okay Bye for now. :) :) :) :)")
print(r"""
          /      /,
         /      //
        /______//
       (______(/""")
input("Press enter to exit.")