# Comparatif SpringBoot et Django REST Framework (DRF)

## Dépendances et libraires

|-------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Caractéristique               | SpringBoot                                                        | Django REST Framework (DRF)                                                                                       |
|-------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| **Gestion des dépendances**   | Fichier `pom.xml`                                                 | Fichier `requirements.txt` et gestion via `pip`                                                                   |
|-------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
|                               | - Le SpringBoot initializer génère automatiquement le `pom.xml`   | - `requirements.txt` très intuitif et facile d'utilisation                                                        |
| **Avantages**                 |                                                                   | - `pip` est très simple à utiliser                                                                                |
|                               |                                                                   | - Peu de dépendances nécessaires (DB, utilisateurs, authentification, tests unitaires, etc. inclus par défaut)    |
|-------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
|                               | - Format XML difficile à lire, modifier et maintenir              | - Les environnements virtuels peuvent ne pas être intuitifs                                                       |
| **Inconvénients**             | - Nombre élevé de dépendances                                     | - Nécessite l'appel manuel de `pip freeze` pour verrouiller les dépendances (`pip freeze > requirements.txt`)     |
|                               | - Pas d'outil CLI pour ajouter des dépendances facilement         | - Des dépendances supplémentaires sont nécessaires pour le LSP (ex: `Pyright`)                                    |
|-------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|


## Structure de fichier
Au premier abord, SpringBoot à l'air plus compliqué à lire. Mais dans les faits,
SpringBoot est nettement plus organisé et après s'être habitué au projet,
savoir où se trouve le code dont on a besoin est très rapide et intuitif.

Les deux frameworks peuvent être structurés par `modules`. Cependant, DRF gère
lui-même `user` et `auth`, ce qui nous force à être créatif et pérséverent
pour correctement séparer ces modules.

DRF à tendance à beaucoup se répéter. La majorité des tutoriels utilisent des
`urls.py` pour définir les routages/paths dans chaques modules. On se retrouve
avec  `n = m(modules) -> n(urls.py)`, ce qui rend la structure difficle à
comprendre. On pourrait renommer ces fichiers mais cela va à l'encontre des
"bonnes" pratiques du framework.

Il est à noter que les paths de SpringBoot sont déclarés via des annotations
directement au dessus des méthodes de nos APIs. Cela rend très clair le lien
entre le lien et la méthode, éliminant ainsi les fichiers redondants.

|-------------------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Caractéristique               | SpringBoot                                                                            | Django REST Framework (DRF)                                                                                                   |
|-------------------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Organisation générale**     | Très organisé, rapide et intuitif après adaptation                                    | Tendance à la répétition, plus difficile à structurer de façon intuitive                                                      |
|-------------------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Modularité**                | Peut être structuré par modules                                                       | Peut être structuré par modules, mais `user` et `auth` sont gérés par défaut, nécessitant plus de créativité pour les séparer |
|-------------------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Définition des routes**     | Routes définies par des annotations directement au-dessus des méthodes dans les APIs  | Les `urls.py` se multiplient dans chaque module, rendant la structure parfois lourde à comprendre                             |
|-------------------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Avantages**                 | - Structure organisée et claire une fois prise en main                                | - DRF gère directement `user`, `auth` et d'autres aspects courants, ce qui simplifie certains aspects                         |
|                               | - Pas de fichiers redondants pour les paths (déclarés dans les annotations)           |                                                                                                                               |
|-------------------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Inconvénients**             | - Peut sembler complexe au premier abord                                              | - Répétition des fichiers `urls.py` dans chaque module                                                                        |
|                               |                                                                                       | - Difficile à maintenir si la structure devient trop complexe                                                                 |
|-------------------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|


## Facilité d'implémentation de fonctionnalités
Django nous parrait très dur. Alors que SpringBoot nous encourage a créer un
dossier `Services` qui gère la "réception des requêtes API" et redirige
vers la logique métier dans une interface clairement définie, DRF opte pour une
syntaxe opaque.

### E.g:

#### SpringBoot

```
public void addNewArticle(String title, String body) {

  Article n = new Article();
  n.setTitle(title);
  n.setBody(body);
  articleRepository.save(n);
}
```

#### DRF
```
def save(self, *args, **kwargs):
    super(Article, self).save(*args, **kwargs)
```

On voit que Django nous demande moins de ligne à écrire, mais le Repository
n'est pas clairement indentifiable et la customisation des méthodes du CRUD
deviennent plus complexes et moins lisibles pour les débutants.


