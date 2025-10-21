import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

def yearafter():
    z=-1
    y=int(input("Select year "))
    for h in data:
        z+=1
        x=data[z]["year"]
        if x>=y:
            print(data[z]["title"],data[z]["year"])
def yearbefore():
    z=-1
    y=int(input("Select year "))
    for h in data:
        z+=1
        x=data[z]["year"]
        if x>=y:
            print(data[z]["title"],data[z]["year"])
    z=-1
    y=int(input("Select year "))
    for h in data:
        z+=1
        x=data[z]["year"]
        if x<=y:
            print(data[z]["title"],data[z]["year"])
def yearduring():
    z=-1
    y=int(input("Select year "))
    for h in data:
        z+=1
        x=data[z]["year"]
        if x==y:
            print(data[z]["title"],data[z]["year"])
def moviesearch():
    y=input("Search a movie ")
    z=-1
    for h in data:
        z+=1
        x=data[z]["title"]
        if x==y:
            print(data[z])
def genresearch():
    y=input("Search a genre ")
    z=-1
    w=0
    for h in data:
        z+=1
        x=data[z]["genres"][0]
        if x==y:
            print(data[z]["title"],data[z]["genres"])
genresearch()