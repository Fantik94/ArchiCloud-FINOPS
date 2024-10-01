
# Lab 9: Implementing Azure Load Balancer and Traffic Manager



## Étape 1 : Déployer Azure Load Balancer

1. Créez un **Load Balancer** dans le portail Azure :
   - *Name* : `LoadBalancerLab9`
   - *Region* : Sélectionner une région appropriée
   - *Frontend IP Configuration* : Associer une IP publique

**Capture d’écran** : ![1.png](1.png)

### Commande équivalente (Azure CLI)
```bash
az network lb create \
  --resource-group <nom_du_groupe> \
  --name LoadBalancerLab9 \
  --frontend-ip-name FrontendConfig \
  --public-ip-address <nom_ip_publique>
```

---

## Étape 2 : Configurer les sondes de santé et les règles de Load Balancing

1. Configurez une **Health Probe** et une **Load Balancing Rule** dans le Load Balancer.

**Capture d’écran** : ![2.png](2.png)

### Commande équivalente (Azure CLI)
```bash
az network lb probe create \
  --resource-group <nom_du_groupe> \
  --lb-name LoadBalancerLab9 \
  --name HealthProbeLab9 \
  --protocol Http \
  --port 80 \
  --path /

az network lb rule create \
  --resource-group <nom_du_groupe> \
  --lb-name LoadBalancerLab9 \
  --name LbRuleLab9 \
  --frontend-ip-name FrontendConfig \
  --backend-pool-name BackendPoolLab9 \
  --probe-name HealthProbeLab9 \
  --protocol Tcp \
  --frontend-port 80 \
  --backend-port 80
```

---

## Étape 3 : Configurer Azure Traffic Manager

1. Créez un **Traffic Manager profile** et associez des endpoints (par exemple, des instances Azure Load Balancer ou d'autres services).

**Capture d’écran** : ![3.png](3.png)

### Commande équivalente (Azure CLI)
```bash
az network traffic-manager profile create \
  --resource-group <nom_du_groupe> \
  --name TrafficManagerLab9 \
  --routing-method Performance \
  --unique-dns-name <nom_unique_dns>

az network traffic-manager endpoint create \
  --resource-group <nom_du_groupe> \
  --profile-name TrafficManagerLab9 \
  --type azureEndpoints \
  --name EndpointLab9 \
  --target-resource-id <id_du_load_balancer>
```

---

## Étape 4 : Tester les scénarios de basculement (failover)

1. Simulez une panne et testez le basculement en arrêtant une des VMs ou en déconnectant un endpoint.

**Capture d’écran** : ![4.png](4.png)

---
