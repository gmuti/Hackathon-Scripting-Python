from dotenv import load_dotenv
from gestion import exportStudentByCity, exportAllStudentByCity
import argparse
from meteo import traiter_etudiants
import os

load_dotenv() 

csv_path = os.getenv("CSV_PATH")
API_KEY = os.getenv("API_KEY")


def parser_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ville", type=str, help="Nom de la ville à traiter")
    parser.add_argument("--full", action="store_true", help="Traiter toutes les villes")
    return parser.parse_args()



if __name__ == "__main__":
    if csv_path is None:
        print("Erreur: La variable CSV_PATH n'est pas définie dans le fichier .env")
        print("Veuillez créer un fichier .env avec: CSV_PATH=chemin/vers/votre/fichier.csv")
        exit(1)
    
    args = parser_arguments()
    if args.ville:
        exportStudentByCity(csv_path, args.ville)
    elif args.full:
        exportAllStudentByCity(csv_path)
    else:
        exportStudentByCity(csv_path, None)
    traiter_etudiants(API_KEY)
    