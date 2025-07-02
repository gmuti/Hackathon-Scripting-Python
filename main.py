from dotenv import load_dotenv
from gestion import exportStudentByCity
from meteo import traiter_etudiants
import os


load_dotenv() 

csv_path = os.getenv("CSV_PATH")
API_KEY = os.getenv("API_KEY")


if __name__ == "__main__":
    traiter_etudiants(API_KEY)
    exportStudentByCity(csv_path)
    