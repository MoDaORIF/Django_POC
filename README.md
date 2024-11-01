# Comparatif SpringBoot et Django REST Framework (DRF)

## Dépendances et librairies

| Caractéristique               | SpringBoot                                                        | Django REST Framework (DRF)                                                                                       |
|-------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| **Gestion des dépendances**   | Fichier `pom.xml`                                                 | Fichier `requirements.txt` et gestion via `pip`                                                                   |

| Caractéristique               | SpringBoot                                                        | Django REST Framework (DRF)                                                                                       |
|-------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| **Avantages**                 | - Le SpringBoot initializer génère automatiquement le `pom.xml`   | - `requirements.txt` très intuitif et facile d'utilisation                                                        |
|                               |                                                                   | - `pip` est très simple à utiliser                                                                                |
|                               |                                                                   | - Peu de dépendances nécessaires (DB, utilisateurs, authentification, tests unitaires, etc. inclus par défaut)    |
| **Inconvénients**             | - Format XML difficile à lire, modifier et maintenir              | - Les environnements virtuels peuvent ne pas être intuitifs                                                       |
|                               | - Nombre élevé de dépendances                                     | - Nécessite l'appel manuel de `pip freeze` pour verrouiller les dépendances (`pip freeze > requirements.txt`)     |
|                               | - Pas d'outil CLI pour ajouter des dépendances facilement         | - Des dépendances supplémentaires sont nécessaires pour le LSP (ex: `Pyright`)                                    |


## Structure de fichier
Au premier abord, SpringBoot a l'air plus compliqué à lire. Mais dans les faits,
SpringBoot est nettement plus organisé et après s'être habitué au projet,
savoir où se trouve le code dont on a besoin est très rapide et intuitif.

Les deux frameworks peuvent être structurés par `modules`. Cependant, DRF gère
lui-même `user` et `auth`, ce qui nous force à être créatifs et persévérants
pour correctement séparer ces modules.

DRF a tendance à beaucoup se répéter. La majorité des tutoriels utilisent des
`urls.py` pour définir les routages/paths dans chaque module. On se retrouve
avec  `n = m(modules) -> n(urls.py)`, ce qui rend la structure difficile à
comprendre. On pourrait renommer ces fichiers mais cela va à l'encontre des
"bonnes" pratiques du framework.

Il est à noter que les paths de SpringBoot sont déclarés via des annotations
directement au-dessus des méthodes de nos APIs. Cela rend très clair le lien
entre le lien et la méthode, éliminant ainsi les fichiers redondants.

### Nomenclature

Les dossiers Controller, services, etc. dans SpringBoot sont appelés des
`Composants`.
SpringBoot est organisé par `composants`.

Les dossiers de DRF, eux, sont des `apps`.
DRF est organisé par `apps`.
DRF est moins intuitif sur cet aspect.


| Caractéristique               | SpringBoot                                                                            | Django REST Framework (DRF)                                                                                                   |
|-------------------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Organisation générale**     | Très organisé, rapide et intuitif après adaptation                                    | Tendance à la répétition, plus difficile à structurer de façon intuitive                                                      |
| **Modularité**                | Peut être structuré par modules                                                       | Peut être structuré par modules, mais `user` et `auth` sont gérés par défaut, nécessitant plus de créativité pour les séparer |
| **Définition des routes**     | Routes définies par des annotations directement au-dessus des méthodes dans les APIs  | Les `urls.py` se multiplient dans chaque `app`, rendant la structure parfois lourde à comprendre                       |

| Caractéristique               | SpringBoot                                                                            | Django REST Framework (DRF)                                                                                                   |
|-------------------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Avantages**                 | - Structure organisée et claire une fois prise en main                                | - DRF gère directement `user`, `auth` et d'autres aspects courants, ce qui simplifie certains aspects                         |
|                               | - Pas de fichiers redondants pour les paths (déclarés dans les annotations)           |                                                                                                                               |
| **Inconvénients**             | - Peut sembler complexe au premier abord                                              | - Répétition des fichiers `urls.py` dans chaque module                                                                        |
|                               |                                                                                       | - Difficile à maintenir si la structure devient trop complexe                                                                 |
|                               |                                                                                       | - L'organisation par `apps` est moins intuitive que par `composants`.                                                         |


## Facilité d'implémentation de fonctionnalités
Django nous paraît très dur. Alors que SpringBoot nous encourage à créer un
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

On voit que Django nous demande moins de lignes à écrire, mais le Repository
n'est pas clairement identifiable et la customisation des méthodes du CRUD
devient plus complexe et moins lisible pour les débutants.

## Différences en détails des Composants

### Controller
Gestion des requêtes HTTP.

#### SpringBoot
- Module `Controller`.
- Annotation juste au-dessus de la méthode.
- Beaucoup d'annotations à apprendre.
- Annotation `@Controller`, `@RequestMapping`, etc.

#### DRF
- Fichier `urls.py` dupliqué dans chaque "app".
- Les `paths` font référence aux méthodes qu'elles appellent mais ne sont pas
    définies au même endroit (similaire à CodeIgniter 4).
- Méthodes `APIView` ou `ViewSet`.

### Model
Lien entre les classes et les tables dans la database.
Automatisation des migrations de tables dans la database.

Peu de différences notables.

#### SpringBoot
- Getters et setters très simples.
- Paramétrage automatique des tables migrées.
- `@Entity`: JPA pour l'ORM

#### DRF
- Getters et setters non obligatoires mais difficiles.
- Paramétrage manuel des tables migrées.
- Classe `Meta` pour les métadonnées obligatoire. E.g: sort by name.
- `models.Model`: ORM de Django

### Repository
Logique ORM.

#### SpringBoot
- Explicitement géré par une interface.
- Facilement maintenable.
- On se retrouve dans le code super facilement car le repo est très bien organisé.
    E.g: Le controller reçoit une requête HTTP et renvoie à la bonne méthode
    du `Repository`.
    Snippet exemple dans un controller:
    ```
    @PostMapping(path = "/add")
    public @ResponseBody String addNewArticle(@RequestParam String title, @RequestParam String body) {

        // Insérer logique métier ici si besoin.

        // Appel de la méthode save du Repository de notre classe Article.
        articleService.addNewArticle(title, body); 
        return "Article added";
    }
    ```
    Le repo est ultra lisible et non ambigu. Voici l'entièreté du code pour 
    démontrer sa simplicité.
    ```
    package orif.poc.repository;

    import org.springframework.data.repository.CrudRepository;
    import orif.poc.model.Article;
    
    // This will be AUTO IMPLEMENTED by Spring into a Bean called userRepository
    // CRUD refers Create, Read, Update, Delete
    
    public interface ArticleRepository extends CrudRepository<Article, Integer> {}
    ```


#### DRF
- Logique dispersée partout dans le programme. Aucune manière simple de retrouver.
- Les méthodes sont très peu modifiables car entièrement cachées par l'ORM.
- IoC (inverse of control) trop stricte.

### Service
Notre propre logique métier

#### SpringBoot
- Notre propre logique.
- Organisée par Composants.
- Java classique sans spécificité technique propre à SpringBoot.
- Annotations simples contrairement au model.

#### DRF
Les exacts mêmes problèmes que pour le Repository.

- Logique dispersée partout dans le programme. Aucune manière simple de retrouver.
- Les méthodes sont très peu modifiables car entièrement cachées par l'ORM.
- IoC (inverse of control) trop stricte.

En bref, les logiques ORM et métier sont complètement dispersées dans le code
et sont très difficiles à visualiser.


### Tests unitaires

Aucune différence notable, que ce soit avec ou sans mocking.

Cependant, SpringBoot sépare clairement l'application elle-même et les tests
unitaires alors que DRF les organise par app.

Les deux organisent leurs tests de manière claire.


## Permissions

## DataBase

## UserManager reminder

