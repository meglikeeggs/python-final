from movies import Movies

movies = Movies('./movies.txt')

def list_all():  
    for i in range (len(movies._movies)):
        print(movies._movies[i]['name'])
    print()


def list_name():
    

def list_cast():



  
choice = ' '

while choice.lower() != 'q':
    print("q: quit")
    print("sn: search by name")
    print("sc: search by cast")
    print("list: print all the movie names")
    choice = input("").lower()

    if(choice == "list"):
        list_all()

    if (choice == "sn"):
        list_name()

    if (choice == "sc"):
        list_cast()
