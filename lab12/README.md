
# Lab 12: Using Azure Resource Manager (ARM) Templates


## Étape 1 : Écrire un template ARM

1. Écrivez un template **`azuredeploy.json`** pour déployer une application multi-tier dans Azure (par exemple, un front-end Web App et un back-end SQL).


---

## Étape 2 : Paramétrer le template pour la réutilisation

1. Utilisez la section **parameters** du template ARM pour rendre les noms et configurations des ressources paramétrables.


---

## Étape 3 : Déployer les ressources via Azure CLI

1. Déployez les ressources définies dans le template ARM à l'aide de la commande Azure CLI :

```bash
az deployment group create \
  --resource-group <nom_du_groupe> \
  --template-file azuredeploy.json \
  --parameters azuredeploy.parameters.json
```


---

## Étape 4 : Valider et dépanner les problèmes de déploiement

1. Validez le déploiement avec l'option **`--what-if`** et dépannez les problèmes en consultant les logs de déploiement.

```bash
az deployment group create \
  --resource-group <nom_du_groupe> \
  --template-file azuredeploy.json \
  --parameters azuredeploy.parameters.json \
  --what-if
```


---
