# Intro Prefect — pipeline « random-check »

Ce mini-projet démontre **Prefect 3** en mode « orchestration-as-code ».  
Toutes les **10 secondes**, un *flow* tire un nombre aléatoire ; si le résultat est **< 0 .5** il écrit **retrain** et lève une exception (2 retries automatiques), sinon il écrit **ok**.  
Vous verrez ainsi :

* la syntaxe _task/flow_ de Prefect,  
* les retries intégrés,  
* la capture des logs,  
* et deux façons de déployer : **local pur** (virtual-env) ou **Docker Compose**.

## architecture
```
intro-prefect/
│
├── flow.py             
├── requirements.txt    
├── Dockerfile
└── docker-compose.yml
```
---

## 1. Exécution locale (sans Docker)

### 1.1 Créer et activer un environnement virtuel

```powershell
# Windows / PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1

# Linux / macOS / WSL
python -m venv .venv
source .venv/bin/activate
```
### 1.2 Installer les dépendances
`pip install -U -r requirements.txt`


#### lancer le serveur prefect
`prefect server start`

#### lancer le code
`python flow.py`

### 2. virtuelLancer avec docker compose
#### build + run en arrière-plan
`docker compose up -d`

#### logs en temps réel si mode détaché
`docker compose logs -f random-check`

#### arrêter et supprimer les conteneurs
`docker compose down`


### 3. Explorer Prefect par vous-même !
* UI Prefect : Flows → Deployments → Runs, pour rejouer un run, voir les retries, filtrer les logs.
* Work Pools & Workers : créez un work pool (prefect work-pool create …) puis lancez prefect worker start … et déployez votre flow avec flow.deploy() ou prefect deploy.
* Schedules avancées : passez de interval=10 à un cron="*/5 * * * *" pour tester les crons.
* Blocks : stockez des credentials AWS, des webhooks Slack, des templates Docker.
* Notifications : configurez un bloc Slack et ajoutez @on_failure_notify(slack_block) pour recevoir une alerte quand un run échoue.
* Transactions (v3) : groupez plusieurs tasks critiques et bénéficiez d’un rollback automatique.
* Cloud : prefect cloud login donne accès à l’UI SaaS gratuite (2 Go).
* Workers Docker/Kubernetes : chaque run dans son propre conteneur, ou orchestration sur K8s via le worker Helm.

Parcourez la doc officielle : https://docs.prefect.io
Explorez les exemples : https://github.com/PrefectHQ/prefect/tree/main/examples

Bonne orchestration !
