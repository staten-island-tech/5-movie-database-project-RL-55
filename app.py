import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)

def yearafter():
    z=0
    No=False
    y=int(input("Select year "))
    for h in data:
        x=data[z]["year"]
        if x>y:
            print(data[z]["title"],data[z]["year"])
            No=True
        z+=1
    if No==False:
        print("No Results")
def yearbetween():
    z=0
    No=False
    y=int(input("Select year start "))
    w=int(input("Select year end "))
    for h in data:
        x=data[z]["year"]
        if w>x>y:
            print(data[z]["title"],data[z]["year"])
            No=True
        z+=1
    if No==False:
        print("No Results")
def yearduring():
    z=0
    y=int(input("Select year "))
    No=False
    for h in data:
        x=data[z]["year"]
        if x==y:
            print(data[z]["title"],data[z]["year"])
            No=True
        z+=1
    if No==False:
        print("No Results")
def moviesearch():
    y=input("Search a movie ")
    z=0
    No=False
    for h in data:
        x=data[z]["title"]
        if x.lower()==y.lower():
            print(data[z])
            No=True
        z+=1
    if No==False:
        print('No Result')
def genresearch():
    z=0
    No=False
    y=input("Search a genre ")
    for h in data:
        x=data[z]["genres"]
        for i in x:
            if i.lower()==y.lower():
                print(data[z]["title"],data[z]["genres"])
        z+=1
    if No==False:
        print("No Result")
genresearch()
