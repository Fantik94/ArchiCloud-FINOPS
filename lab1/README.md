# Lab 1: Creating and Managing Azure Virtual Machines

```bash
az vm create \
    --resource-group <nom_du_groupe> \
    --name <nom_vm> \
    --image UbuntuLTS \
    --admin-username <votre_nom_d_utilisateur> \
    --authentication-type ssh \
    --ssh-key-value <clé_publique_ssh> \
    --size Standard_B1s
```

Capture d'écran: (1.PNG)

Capture d'écran: (2.PNG)