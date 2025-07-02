from utils.csv_utils import read_csv
from utils.logger import logger
from utils.json_utils import export_json


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
    data = read_csv(file)
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
    export_json(data,file)
    logger.info("Export JSON termine")
        

def exportCityData(data, ville):
    filterStudentData = filterStudent(data, ville)
    sortedByAge = sortedAge(filterStudentData)
    exportFile = f"exports/{ville}.json"
    exportJson(sortedByAge, exportFile)
    logger.info(f"Export terminé pour la ville : {ville}")

def exportStudentByCity(csv_path, ville_CLI=None):
    logger.info("Lancement de la fonction exportStudentByCity")
    data = readFile(csv_path, [])
    allCity = getAllVille(data)
    if ville_CLI is None:
        ville = demanderVille(allCity)
        logger.info(f"Ville sélectionnée : {ville}")
    else:
        ville = arrangeVille(ville_CLI)
        logger.info(f"Ville fournie par l'utilisateur : {ville}")
        if ville not in allCity:
            logger.error(f"La ville {ville} n'est pas dans la liste des villes disponibles.")
            print(f"La ville {ville} n'est pas dans la liste des villes disponibles.")
            exit(1)
    exportCityData(data, ville)

def exportAllStudentByCity(csv_path):
    logger.info("Lancement de la fonction exportAllStudentByCity")
    data = readFile(csv_path, [])
    allCity = getAllVille(data)
    for ville in allCity:
        exportCityData(data, ville)