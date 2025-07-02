from dotenv import load_dotenv
import os
import requests
import json
from datetime import datetime

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_meteo(ville):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
    "q": ville,
    "appid": API_KEY,
    "units": "metric",
    "lang": "fr"
    }
    try:
        reponse = requests.get(url, params=params)
        reponse.raise_for_status()
        donnees = reponse.json()
        return donnees["weather"][0]["main"], donnees["weather"][0]["description"]
    except Exception as erreur:
        return None, f"Erreur API : {str(erreur)}"


def determiner_mode_cours(condition_meteo):
    meteo_visio = ["Rain", "Snow", "Thunderstorm", "Drizzle"]
    if condition_meteo in meteo_visio:
        return "visioconférence"
    return "présentiel"


def traiter_etudiants():
    dossier_exports = "exports"
    decisions = []
    
    if not os.path.exists(dossier_exports):
        print(f"Le dossier {dossier_exports} n'existe pas.")
        return
    
    for fichier in os.listdir(dossier_exports):
        if fichier.endswith('.json'):
            chemin_fichier = os.path.join(dossier_exports, fichier)
            ville = fichier.replace('.json', '')
                        
            try:
                with open(chemin_fichier, 'r', encoding='utf-8') as f:
                    liste_etudiants = json.load(f)
                
                condition_meteo, description_meteo = get_meteo(ville)
                
                mode_cours = determiner_mode_cours(condition_meteo)
                
                for etudiant in liste_etudiants:
                    #creer une liste decision
                    nom = etudiant['nom']
                    ville_etudiant = etudiant['ville']
                    
                    decision = {
                        "nom": nom,
                        "ville": ville_etudiant,
                        "mode_cours": mode_cours,
                        "description_meteo": description_meteo
                    }
                    decisions.append(decision)
                    
                    if mode_cours == "visioconférence":
                        print(f"Cours en visio pour {nom} ({ville_etudiant}) – Météo : {description_meteo.lower()}")
                    else:
                        print(f"Cours en présentiel pour {nom} ({ville_etudiant}) – Météo : {description_meteo.lower()}")
                        
            except FileNotFoundError:
                print(f"Fichier {chemin_fichier} introuvable.")
            except json.JSONDecodeError:
                print(f"Erreur lors de la lecture du fichier JSON {chemin_fichier}.")
            except Exception as e:
                print(f"Erreur lors du traitement de {fichier}: {str(e)}")
                
    sauvegarder_decisions_json(decisions)

def sauvegarder_decisions_json(decisions: list[dict]):
    os.makedirs("decision_meteo", exist_ok=True)
    date_du_jour = datetime.now().strftime("%Y-%m-%d")
    chemin_fichier = f"decision_meteo/decisions_{date_du_jour}.json"

    with open(chemin_fichier, "w", encoding="utf-8") as f:
        json.dump(decisions, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    traiter_etudiants()


