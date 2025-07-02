# 📚 Hackathon-Scripting-Python – ESGI 3 AL/IW/SRC

## 🎯 Objectif

Ce projet a pour but de mettre en œuvre les compétences DevOps à travers une solution permettant d’automatiser 
la gestion des étudiants et l'organisation des cours en fonction de la météo. Il combine :

- 📦 Automatisation de tâches
- 🏗️ Structuration logicielle modulaire
- ☁️ Appels à une API météo (OpenWeatherMap)
- 📁 Manipulation de formats de fichiers variés (CSV, JSON, .env, logs)

---

## 🧩 Fonctionnalités

1. **Gestion des étudiants**
   - Chargement et filtrage des étudiants à partir d’un fichier CSV
   - Tri par âge croissant
   - Sauvegarde des résultats en JSON

2. **Décision automatique du mode de cours**
   - Appel API météo pour chaque ville
   - Présentiel si météo : ☀️ *Clear* ou ☁️ *Clouds*
   - Visioconférence si météo : 🌧️ *Rain*, ❄️ *Snow*, ⚡ *Thunderstorm*, 🌦️ *Drizzle*
   - Fichier `decisions_<date>.json` récapitulatif

3. **Logs**
   - Suivi des événements, erreurs et décisions météo dans un fichier `logs/app_<date>.log`

4. **Interface en ligne de commande (CLI)**
   - Filtrage par ville
   - Lancement complet avec l’option `--full`

5. **Rapport global**
   - Génération de `report_<date>.txt` contenant :
     - Nombre de villes traitées
     - Étudiants en présentiel / visioconférence

---

## 🗂️ Arborescence du projet

```
Hackathon-Scripting-Python/
│
├── .env 
├── etudiants.csv 
├── main.py 
├── gestion.py 
├── meteo.py 
├── utils
│  └── logger.py
├── exports
├── logs
└── decisions
   └──decisions_<date>.json 
```


## ⚙️ Installation

### 1. Cloner le dépôt

```bash
git clone <url-du-projet>
cd Hackathon-Scripting-Python
```

### 2. Créer le fichier .env
```
API_KEY=votre_cle_api_openweathermap
CSV_PATH=etudiants.csv
```