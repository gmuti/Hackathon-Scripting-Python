from dotenv import load_dotenv
from gestion import exportStudentByCity
import os


load_dotenv() 

csv_path = os.getenv("CSV_PATH")


if __name__ == "__main__":
    exportStudentByCity(csv_path)