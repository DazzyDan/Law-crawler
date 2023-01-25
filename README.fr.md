# Crawler d'affaires juridiques | Crawler d'affaires juridiques

-   [Chinois simplifié](README.zh-CN.md)

Law case crawler est un projet qui permet d'explorer, de gratter et de visualiser des cas de droit à partir de trois moteurs de recherche (Baidu, Sogou et Wechat) et de deux sites Web de recherche de cas de droit (wusong et bashou). Il s'exécute avec le docker de grille Selenium, Flask et gunicorn. Ceci est la première version. Dans la prochaine version, il mettra en œuvre des processus parallèles et stockera les données acquises dans la base de données pour accélérer le traitement et minimiser la mise en cache.

## La structure

<img width="981" alt="image" src="https://user-images.githubusercontent.com/73490814/214577434-349674c2-eac8-4f93-9e51-dd609273c757.png">

## Captures d'écran

### Page d'accueil

1.  Moteurs de recherche<img width="1356" alt="image" src="https://user-images.githubusercontent.com/73490814/214578514-23a388bb-84a2-4b76-ad9b-c2a80eb5f800.png">

Trois moteurs de recherche peuvent être choisis.![0 0 0 0_5000\_ (3)](https://user-images.githubusercontent.com/73490814/214579469-29272eee-4b23-4e2b-b7d0-456f35757164.png)

2.  Toiles de cas![0 0 0 0_5000\_ (1)](https://user-images.githubusercontent.com/73490814/214578873-102ca7dc-d1eb-4b63-80ae-44840b914c9b.png)

Il est capable de sélectionner différents types de cas.![0 0 0 0_5000\_ (2)](https://user-images.githubusercontent.com/73490814/214579157-7df4cf7b-7c25-47e2-90c1-e22a1e336a05.png)

### Result page

gridjs est utilisé pour réaliser la table. Grid.js est un plugin de tableau JavaScript gratuit et open-source. Il peut mettre en œuvre ces fonctions : recherche de mots clés, tri.

1.  Les résultats des moteurs de recherche![0 0 0 0_5000_search-web](https://user-images.githubusercontent.com/73490814/214580092-96316127-042a-481b-8517-1923099f7ade.png)
2.  Résultats des toiles de cas<img width="1354" alt="image" src="https://user-images.githubusercontent.com/73490814/214585512-d7f1d19e-8f06-4fbd-b746-4aab39af825e.png">

![0 0 0 0_5000_search-case](https://user-images.githubusercontent.com/73490814/214585639-69165daf-0900-4cec-9c06-d93fd0e29eb5.png)

Cliquez sur "Afficher plus":<img width="1361" alt="image" src="https://user-images.githubusercontent.com/73490814/214585922-06f21a67-8195-453c-8f75-a4c33381f439.png">

Plus de détails sur ce cas seront affichés.

## Comment installer et exécuter le projet

Tout d'abord, vous pouvez extraire cette image du hub Docker.

```bash
docker pull dazzydan/law_crawler:1.0
```

Ensuite, exécutez cette image

```bash
docker-compose up -d
```

## Comment utiliser le projet

Portail :<http://0.0.0.0:5000/>

Page de traitement de la grille de sélénium :<http://127.0.0.1:4444/>

Si vous souhaitez découvrir ce qui se passe pendant l'exploration, la connexion à la visionneuse VNC est disponible :<http://127.0.0.1:6900/>

## Amélioration future

1.  Cortège parallèle
2.  Base de données
