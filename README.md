#  Challenge CTF – Dans les pas d’une Analyste Cybersécurité

Bienvenue dans un mini-CTF (Capture The Flag) immersif !  
Tu vas marcher dans les pas de **Sadio**, analyste cybersécurité chez **Junior**, à travers une série d’étapes interactives inspirées de son quotidien.

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

challenge_cybersec/
│
├── logs/
│ └── intrusion_alert_01.log ← Fichier d’alerte IDS (Snort/Suricata)
│
├── scripts/
│ └── alert_parser.py ← Script Python à compléter
│
├── hashes/
│ └── clue1.hash ← Indice encodé en base64
│
├── cv/
│ └── CV_Sadio_Analyste.pdf ← Récompense finale (CV complet)
│
├── flag.txt ← Message final
├── README.md ← Ce fichier
└── start.sh ← (Optionnel) Script de lancement

yaml
Copier
Modifier

---

## 🔍 Étapes du Challenge

### 🧭 Étape 1 – Reconnaissance
Fouille dans les fichiers pour trouver un indice de départ.

> Astuce : fouille les logs ou les encodages.

---

### 🔎 Étape 2 – Analyse d'incident
Lis le fichier `logs/intrusion_alert_01.log`.

> Que s’est-il passé ?  
> Quelle est l’adresse IP à l’origine de l’alerte ?  
> Que faisait-elle ? (Indice : port scan)

Corrèle cette information à l’entreprise **TicketEasy** pour avancer.

---

### 🧮 Étape 3 – Décryptage
Tu as trouvé un hash dans `hashes/clue1.hash` ?

U2FkaW8=

bash
Copier
Modifier

Utilise :

```bash
echo U2FkaW8= | base64 -d
🐍 Étape 4 – Script Python à compléter
Fichier : scripts/alert_parser.py
Complète les 2 lignes manquantes dans ce parser :

python
Copier
Modifier
# Ligne manquante 1
alert_type = line.split("]")[2].strip()

# Ligne manquante 2
alerts.append(alert_type)
Puis exécute le script :

bash
Copier
Modifier
python scripts/alert_parser.py
🏁 Étape 5 – Révélation finale
Le fichier flag.txt s’affiche :

bash
Copier
Modifier
Tu viens de marcher dans les pas de Sadio. Voici qui elle est.
CV : ./cv/CV_Sadio_Analyste.pdf
🎉 Félicitations ! Tu as complété le challenge.

💡 À propos
Ce challenge a été conçu comme un CV interactif pour mettre en valeur les compétences techniques et l’esprit d’analyse de Sadio, analyste cybersécurité spécialisée en IA.

📫 Contact : LinkedIn de Sadio
🔐 GitHub : https://github.com/sadioguindo/challenge-CTF

✅ Technologies utilisées
Python 3

Snort / IDS Logs (format simplifié)

base64, hash

GitHub Pages / README interactif

✨ Licence
Ce projet est libre pour usage personnel, professionnel ou pédagogique.
Fais-en bon usage… ou inspire-toi pour créer ton propre CV-challenge !
