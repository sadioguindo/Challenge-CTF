# Script d’analyse simple de logs SOC
# À compléter (2 lignes manquantes)

def parse_log(filename):
    with open(filename, "r", encoding="latin-1", errors="ignore") as f:
        lines = f.readlines()
    
    alerts = []
    for line in lines:
        if "ALERT" in line:
            # Ligne manquante 1 : extraire la description de l’alerte
            # Ligne manquante 2 : ajouter cette alerte à la liste

    return alerts

if __name__ == "__main__":
    alerts, note = parse_log("../logs/intrusion_alert_01.log")
    for r in results:
        print(" Alerte détectée :", r)
