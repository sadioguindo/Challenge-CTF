# Script d’analyse simple de logs SOC
# À compléter (2 lignes manquantes)

def parse_log(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    
    alerts = []
    for line in lines:
        if "ALERT" in line:
            # Ligne manquante 1 : extraire la description de l’alerte
            alert_type = line.split("]")[2].strip()
            # Ligne manquante 2 : ajouter cette alerte à la liste
            alerts.append(alert_type)

    return alerts

if __name__ == "__main__":
    results = parse_log("logs/intrusion_alert_01.log")
    for r in results:
        print("🔍 Alerte détectée :", r)
