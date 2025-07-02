import os
import requests
import json
from datetime import datetime
from utils.logger import logger

def get_meteo(ville, apiKey):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": ville,
        "appid": apiKey,
        "units": "metric",
        "lang": "fr"
    }
    try:
        logger.info(f"Requête météo pour la ville : {ville}")
        reponse = requests.get(url, params=params)
        reponse.raise_for_status()
        donnees = reponse.json()
        logger.debug(f"Réponse météo reçue : {donnees}")
        return donnees["weather"][0]["main"], donnees["weather"][0]["description"]
    except Exception as erreur:
        logger.error(f"Erreur lors de la récupération météo pour {ville} : {erreur}")
        return None, f"Erreur API : {str(erreur)}"

def determiner_mode_cours(condition_meteo):
    meteo_visio = ["Rain", "Snow", "Thunderstorm", "Drizzle"]
    logger.debug(f"Détermination du mode de cours pour la météo : {condition_meteo}")
    if condition_meteo in meteo_visio:
        return "visioconférence"
    return "présentiel"

def lister_fichiers_json(dossier_exports):
    logger.info(f"Liste des fichiers JSON dans le dossier : {dossier_exports}")
    fichiers = []
    for nom_fichier in os.listdir(dossier_exports):
        if nom_fichier.endswith('.json'):
            fichiers.append(nom_fichier)
    logger.debug(f"Fichiers trouvés : {fichiers}")
    return fichiers

def charger_etudiants(chemin_fichier):
    logger.info(f"Chargement des étudiants depuis : {chemin_fichier}")
    with open(chemin_fichier, 'r', encoding='utf-8') as f:
        data = json.load(f)
    logger.debug(f"Nombre d'étudiants chargés : {len(data)}")
    return data

def traiter_etudiant(etudiant, ville, apiKey):
    logger.debug(f"Traitement de l'étudiant : {etudiant['nom']} ({etudiant['ville']})")
    condition_meteo, description_meteo = get_meteo(ville, apiKey)
    mode_cours = determiner_mode_cours(condition_meteo)
    decision = {
        "nom": etudiant['nom'],
        "ville": etudiant['ville'],
        "mode_cours": mode_cours,
        "description_meteo": description_meteo
    }
    if mode_cours == "visioconférence":
        print(f"Cours en visio pour {etudiant['nom']} ({etudiant['ville']}) – Météo : {description_meteo.lower()}")
        logger.info(f"Cours en visio pour {etudiant['nom']} ({etudiant['ville']}) – Météo : {description_meteo.lower()}")
    else:
        print(f"Cours en présentiel pour {etudiant['nom']} ({etudiant['ville']}) – Météo : {description_meteo.lower()}")
        logger.info(f"Cours en présentiel pour {etudiant['nom']} ({etudiant['ville']}) – Météo : {description_meteo.lower()}")
    return decision

def traiter_etudiants(apiKey):
    dossier_exports = "exports"
    decisions = []
    
    if not os.path.exists(dossier_exports):
        logger.error(f"Le dossier {dossier_exports} n'existe pas.")
        return
    
    for fichier in lister_fichiers_json(dossier_exports):
        chemin_fichier = os.path.join(dossier_exports, fichier)
        ville = fichier.replace('.json', '')
        try:
            liste_etudiants = charger_etudiants(chemin_fichier)
            for etudiant in liste_etudiants:
                decision = traiter_etudiant(etudiant, ville, apiKey)
                decisions.append(decision)
        except FileNotFoundError:
            logger.error(f"Fichier {chemin_fichier} introuvable.")
        except json.JSONDecodeError:
            logger.error(f"Erreur lors de la lecture du fichier JSON {chemin_fichier}.")
        except Exception as e:
            logger.error(f"Erreur lors du traitement de {fichier}: {str(e)}")
                
    sauvegarder_decisions_json(decisions)

def sauvegarder_decisions_json(decisions: list[dict]):
    os.makedirs("decision_meteo", exist_ok=True)
    date_du_jour = datetime.now().strftime("%Y-%m-%d")
    chemin_fichier = f"decision_meteo/decisions_{date_du_jour}.json"
    logger.info(f"Sauvegarde des décisions dans : {chemin_fichier}")
    with open(chemin_fichier, "w", encoding="utf-8") as f:
        json.dump(decisions, f, ensure_ascii=False, indent=2)
    logger.info("Sauvegarde des décisions terminée")