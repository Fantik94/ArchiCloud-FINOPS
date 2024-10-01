
# Lab 7: Implementing Azure Functions

## Objectif
Dans ce lab, nous allons créer une Azure Function App, développer une fonction serverless déclenchée par une requête HTTP, l'intégrer avec Azure Storage ou Azure Queue, et surveiller ses performances et ses logs.

## Étape 1 : Créer une Azure Function App

1. Créez une **Function App** dans le portail Azure :
   - *App Name* : `FunctionAppLab7`
   - *Runtime Stack* : Node.js ou Python
   - *Region* : Sélectionner une région appropriée
   - *Operating System* : Linux ou Windows

**Capture d’écran** : ![1.png](screenshots/1.png)

### Commande équivalente (Azure CLI)
```bash
az functionapp create \
  --resource-group <nom_du_groupe> \
  --consumption-plan-location <region> \
  --runtime node \
  --name FunctionAppLab7 \
  --storage-account <nom_du_compte_stockage>
```

---

## Étape 2 : Développer une fonction serverless (HTTP Trigger)

1. Développez une fonction déclenchée par une requête HTTP dans l'**Azure Function App**.

**Capture d’écran** : ![2.png](screenshots/2.png)

---

## Étape 3 : Intégrer la fonction avec Azure Storage ou Azure Queue

1. Intégrez la fonction avec **Azure Queue** ou **Azure Storage** via des bindings.

**Capture d’écran** : ![3.png](screenshots/3.png)

---

## Étape 4 : Surveiller les performances et les logs

1. Surveillez les performances et les logs de la fonction via le portail Azure.

**Capture d’écran** : ![4.png](screenshots/4.png)

---

## Conclusion
Ce lab nous a permis de créer une Azure Function App, de développer une fonction serverless, de l'intégrer avec Azure Storage ou Azure Queue, et de surveiller ses performances et ses logs pour assurer son bon fonctionnement.

