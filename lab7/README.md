
# Lab 7: Implementing Azure Functions


## Étape 1 : Créer une Azure Function App

1. Créez une **Function App** dans le portail Azure :
   - *App Name* : `FunctionAppLab7`
   - *Runtime Stack* : Node.js ou Python
   - *Region* : Sélectionner une région appropriée
   - *Operating System* : Linux ou Windows

**Capture d’écran** : ![1.png](1.png)

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

**Capture d’écran** : ![2.png](2.png)

---

## Étape 3 : Intégrer la fonction avec Azure Storage ou Azure Queue

1. Intégrez la fonction avec **Azure Queue** ou **Azure Storage** via des bindings.

**Capture d’écran** : ![3.png](3.png)

---

## Étape 4 : Surveiller les performances et les logs

1. Surveillez les performances et les logs de la fonction via le portail Azure.

**Capture d’écran** : ![4.png](4.png)

---

