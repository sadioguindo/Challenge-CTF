# Challenge CTF – Dans les pas d’une Analyste Cybersécurité

Bienvenue dans ce mini-CTF immersif !  
Tu vas marcher dans les pas de **Sadio**, développeuse IA chez **TicketEasy**, à travers une série d’étapes inspirées de son quotidien en cybersécurité.

---

##  Objectif

Mets-toi dans la peau d’un analyste SOC 👩🏽‍💻  
Ton objectif est de :
1. Identifier une activité malveillante à partir de logs réels.
2. Corréler les événements à un profil professionnel.
3. Décrypter des indices.
4. Compléter un script d’analyse.
5. Découvrir le CV complet de Sadio.

---

## 🗂️ Arborescence du projet

```text
challenge_cybersec/
├── logs/
│   └── intrusion_alert_01.log        # Log d’alerte (Snort-like)
├── scripts/
│   └── alert_parser.py               # Script Python à compléter
├── hashes/
│   └── clue1.hash                    # Indice encodé (Base64)
├── cv/
│   └── CV_Sadio_Analyste.pdf         # Récompense finale
├── flag.txt                          # Message final
├── start.sh                          # Script Bash de lancement 
└── README.md                         # Ce fichier
```

---

## Étapes du Challenge

### Étape 1 – Reconnaissance

Fouille dans les fichiers pour trouver un indice de départ.

> Astuce : fouille les logs ou les encodages.

###  Étape 2 – Analyse d'incident

Lis le fichier `logs/intrusion_alert_01.log`.

> Que s’est-il passé ?  
> Quelle est l’adresse IP à l’origine de l’alerte ?  
> Que faisait-elle ? (Indice : port scan)

Corrèle cette information à l’entreprise **TicketEasy** pour avancer.

Repère les mots-clés comme `ALERT`, `Port Scan`, `IP` etc.


---

###  Étape 2 – Décryptage

Tu as trouvé un hash dans `hashes/clue1.hash` ?

Contenu :

```text
U2FkaW8gcmVjaGVyY2hlIHVuZSBhbHRlcm5hbmNlIGVuIGFuYWx5c3RlIHNvYw==
```

Décode-le avec la commande suivante :

```bash
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("U2FkaW8gcmVjaGVyY2hlIHVuZSBhbHRlcm5hbmNlIGVuIGFuYWx5c3RlIHNvYw=="))
```



---

### Étape 3 – Script Python

Complète les deux lignes suivantes :

```python
# Script d’analyse simple de logs SOC

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
```

Puis exécute :

```bash
python scripts/alert_parser.py
```

---

###  Étape 4 – Révélation finale

```text
Tu viens de marcher dans les pas de Sadio. Voici qui elle est.
"Complète le formulaire final.html pour découvrir la suite de l’aventure…

```

---

## 🧠 Technologies utilisées

- Python 3
- Fichier log (type IDS)
- Encodage Base64
- Bash

---

## 👩🏽‍💻 À propos de Sadio

**Sadio Guindo** est développeuse IA chez **TicketEasy**  
Elle combine **cybersécurité**, **automatisation** et **analyse de logs** dans un environnement SOC.

---

##  Licence

Ce projet est libre pour usage personnel, professionnel ou pédagogique.
Fais-en bon usage… ou inspire-toi pour créer ton propre CV-challenge !

---

## 📫 Contact

**Sadio Guindo**  
📧 sadioguindo560@gmail.com  
🌐 [LinkedIn](https://www.linkedin.com/in/sadioguindo) 
