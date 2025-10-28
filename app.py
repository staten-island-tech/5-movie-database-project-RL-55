import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)

def yearafter():
    z=0
    y=int(input("Select year "))
    for h in data:
        x=data[z]["year"]
        if x>y:
            print(data[z]["title"],data[z]["year"])
        z+=1
def yearbefore():
    z=0
    y=int(input("Select year "))
    w=int(input("Select year "))
    for h in data:
        x=data[z]["year"]
        if x>y>w:
            print(data[z]["title"],data[z]["year"])
        z+=1
def yearduring():
    z=0
    y=int(input("Select year "))
    for h in data:
        x=data[z]["year"]
        if x==y:
            print(data[z]["title"],data[z]["year"])
        z+=1
def moviesearch():
    y=input("Search a movie ")
    z=0
    for h in data:
        x=data[z]["title"]
        if x==y:
            print(data[z])
    z+=1
def genresearch():
    z=0
    y=input("Search a genre ")
    for h in data:
        x=data[z]["genres"]
        for i in x:
            if i==y:
                print(data[z]["title"],data[z]["genres"])
        z+=1
