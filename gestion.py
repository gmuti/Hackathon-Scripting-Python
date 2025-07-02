import csv, json
import os
from utils.logger import logger


def arrangeVille(ville):
    logger.debug(f"arrangeVille appelee avec : {ville}")
    return (ville[0].upper() + ville[1:].lower()).strip()
    

def demanderVille(data):
    ville = None
    while True:
        ville = input("Saisir le nom d'une ville : ")
        logger.info(f"Ville saisie par l'utilisateur : {ville}")
        ville = arrangeVille(ville)
        if ville in data:
            logger.info(f"Ville trouvee dans la liste : {ville}")
            return ville
        else:
            print("Il n'y a pas de campus dans cette ville.")
            logger.warning(f"Aucun campus pour la ville saisie : {ville}")


def getAllVille(data):
    logger.debug("getAllVille appelee")
    responseData = []
    for element in data :
        if element["ville"] not in responseData:
            responseData.append(element["ville"])
    logger.info(f"Liste des villes extraites : {responseData}")
    return responseData
        

def readFile(file, data):
    logger.info(f"Lecture du fichier CSV : {file}")
    with open(file, newline='',encoding="UTF-8") as csvFile:
        reader = csv.DictReader(csvFile)
        data.extend(list(reader))
    logger.info(f"Nombre d'elements lus : {len(data)}")
    return data

def filterStudent(data, ville):
    logger.debug(f"Filtrage des etudiants pour la ville : {ville}")
    responseData = []
    for element in data:
        if element["ville"] == ville:
            responseData.append(element)
    logger.info(f"Nombre d'etudiants trouves pour {ville} : {len(responseData)}")
    return responseData

def getAge(item):
    return item["age"]

def sortedAge(data):
    logger.debug("Tri des etudiants par age")
    return sorted(data,key=getAge)


def exportJson(data, file):
    logger.info(f"Export des donnees vers le fichier JSON : {file}")
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    logger.info("Export JSON termine")
        

def exportStudentByCity(csv_path) :
    logger.info("Lancement de la fonction exportStudentByCity")
    data = readFile(csv_path,[])
    allCity = getAllVille(data)    
    ville = demanderVille(allCity)
    filterStudentData = filterStudent(data,ville)
    sortedByAge = sortedAge(filterStudentData)    
    exportFile = "exports/"+ville+".json"
    exportJson(sortedByAge,exportFile)
    logger.info(f"Export termine pour la ville : {ville}")