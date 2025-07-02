import csv, json
from dotenv import load_dotenv
import os

load_dotenv() 

csv_path = os.getenv("CSV_PATH")


def arrangeVille(ville):
    return (ville[0].upper() + ville[1:].lower()).strip()
    

def demanderVille(data):
    ville = None
    while True:
        ville = input("Saisir le nom d'une ville : ")
        ville = arrangeVille(ville)
        if ville in data:
            return ville
        else:
            print("Il n'y a pas de campus dans cette ville.")


def getAllVille(data):
    responseData = []
    for element in data :
        if element["ville"] not in responseData:
            responseData.append(element["ville"])
    return responseData
        

def readFile(file, data):
    with open(file, newline='',encoding="UTF-8") as csvFile:
        reader = csv.DictReader(csvFile)
        data.extend(list(reader))
    return data

def filterStudent(data, ville):
    responseData = []
    for element in data:
        if element["ville"] == ville:
            responseData.append(element)
    return responseData

def getAge(item):
    return item["age"]

def sortedAge(data):
    return sorted(data,key=getAge)


def exportJson(data, file):
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        

def exportStudentByCity(csv_path) :
    
    data = readFile(csv_path,[])
    allCity = getAllVille(data)    
    ville = demanderVille(allCity)
    filterStudentData = filterStudent(data,ville)
    sortedByAge = sortedAge(filterStudentData)    
    exportFile = "export/"+ville+".json"
    
    exportJson(sortedByAge,exportFile)
    
