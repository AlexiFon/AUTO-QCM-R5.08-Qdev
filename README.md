# Compte-rendu projet de Qualité de développement

*Auteurs :* **Alexi Fontanilles, Nathan Pagnucco**

## Introduction

Lien vers notre dépôt : [Depot Github](https://github.com/AlexiFon/AUTO-QCM-R5.08-Qdev)

Ce document présente le compte-rendu du projet de Qualité de développement. Il s'agit d'un projet de développement d'une application de QCM en ligne, réalisé en binôme. Le projet est découpé en plusieurs User Stories, chacune représentant une fonctionnalité de l'application. Chaque User Story est associée à une ou plusieurs Features, qui décrivent plus en détail les exigences fonctionnelles. Enfin, chaque Feature est associée à des tests d'acceptation qui permettent de valider son bon fonctionnement.

## Installation

Pour pouvoir commencer à relier des features Cucumber à des tests en python nous avons d'abord choisi de voir si on pouvez utiliser Behave comme nous l'avions fait dans le TP3 mais le packet behave n'était pas du tout prévu pour être utilisé avec django, nous avons alors vu des conflits de version et des packages que nous ne pouvions pas utiliser en même temps. Nous avons donc commencé à regarder une version de behave destiné à django et nous avons trouvé [django-behave](https://github.com/django-behave/django-behave) mais nous avons eu le même problème, il était prévu pour une version antérieure de django et n'a pas eu de mise à jour depuis 3 ans. Finalement nous avons trouvé [behave-django](https://github.com/behave/behave-django) le port officiel de behave pour fonctionner avec django, nous avons pu le rajouter à notre requirements.txt dans la version dev.


## Traçabilité US -> Features -> Tests

### User Story 1 : En tant qu'étudiant, je veux avoir accès à toutes les pages qui me sont destinées.

**Feature : Accès aux pages étudiants**

**Tests :**

- Test que l'étudiant peut accéder à une page autorisée.
- Test que l'étudiant est bloqué lorsqu'il accède à une page non autorisée.

### User Story 2 : En tant qu'enseignant, je veux avoir accès à toutes les pages qui me sont destinées.

**Feature : Accès aux pages enseignants**

**Tests :**

- Test que l'enseignant peut accéder aux pages d'administration.
- Test que l'enseignant est redirigé s'il tente d'accéder aux pages étudiantes.

### User Story 3 : En tant qu'enseignant, je souhaite établir un lien efficace entre le système de QCM et Moodle/AMC.

**Feature : Intégration QCM avec Moodle/AMC**

**Tests :**

Pour les tests nous avons choisi de tester l'export et l'import avec les trois formats compatibles XML pour Moodle, LaTeX pour AMC, et AMC.txt pour AMC également.

- Test que l'export des qcm sous différent formats est conforme
- Test que l'import de questions depuis différents formats est conforme

### User Story 4 : En tant qu'enseignant, je veux pouvoir accéder à un espace de gestion des questions.

**Feature : Gestion des questions**

**Tests :**

Pour les tests nous avons choisi de faire des tests sur le crud en faisant des requetes pour tester vraiment le même fonctionnement qu'un utilisateur et non pas juste en créant en base de données.

- Test de modification d'une question existante.
- Test d'ajout d'une nouvelle question.
- Test de suppression d'une question.

### User Story 5 : En tant qu'enseignant, je veux consulter un tableau de bord des résultats des étudiants.

**Feature : Tableau de bord des résultats**

**Tests :**

- Test que les statistiques anonymisées sont visibles.
- Test de l'accès à l'historique des résultats d'un étudiant.

### User Story 6 : En tant qu'étudiant, je veux pouvoir réaliser des qcm à tout moment pour réviser

**Feature : Répondre à un qcm**

**Tests :**

- Test que l'étudiant peut démarrer un QCM.
- Test que les réponses sont enregistrées correctement.

### User Story 7 : En tant qu'enseignant, je souhaite envoyer mes supports de cours pour générer des questions automatiquement.

Pour cette user story nous n'avons pas réalisé de tests, car cela nous demanderai de mettre des clés OpenAI, et d'utiliser des tokens pour le tester à chaque fois.

### User Story 8 : En tant qu'enseignant, je souhaite agréger automatiquement des questions pour générer des QCM de contrôle.

**Feature : Agrégation de questions**

**Tests :**

- Test que les questions sont sélectionnées automatiquement à partir de la banque de questions.
- Test que le QCM généré contient un mélange de questions nouvelles et existantes.

### User Story 9 : En tant qu'étudiant, je veux pouvoir accéder à un tableau de bord interactif me montrant mes progrès.

**Feature : Tableau de bord étudiant**

**Tests :**

- ???


### User Story 10 : En tant qu'enseignant, je souhaite pouvoir créer des QCM de révision hebdomadaire.

**Feature : Création de QCM de révision**

**Tests :**

- Test que l'enseignant peut créer un QCM en saisissant des questions.
- Test que l'enseignant peut modifier des qcms.
- Test que l'enseignant peut supprimer des qcms.

## Conclusion

Chaque User Story est tracée vers une ou plusieurs Features, et chaque Feature est associée à des tests d'acceptation concrets. Cela garantit une couverture complète des exigences fonctionnelles et facilite la validation du projet.
