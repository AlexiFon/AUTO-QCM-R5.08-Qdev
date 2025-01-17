# Compte-rendu projet de Qualité de développement

*Auteur :* **Alexi Fontanilles, Nathan Pagnucco**

## Introduction

Ce document présente le compte-rendu du projet de Qualité de développement. Il s'agit d'un projet de développement d'une application de QCM en ligne, réalisé en binôme. Le projet est découpé en plusieurs User Stories, chacune représentant une fonctionnalité de l'application. Chaque User Story est associée à une ou plusieurs Features, qui décrivent plus en détail les exigences fonctionnelles. Enfin, chaque Feature est associée à des tests d'acceptation qui permettent de valider son bon fonctionnement.

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

- Test que le QCM est synchronisé avec Moodle avec succès.
- Test que les erreurs de synchronisation sont signalées correctement.

### User Story 4 : En tant qu'enseignant, je veux pouvoir accéder à un espace de gestion des questions.

**Feature : Gestion des questions**

**Tests :**

- Test de modification d'une question existante.
- Test d'ajout d'une nouvelle question.
- Test de suppression d'une question.

### User Story 5 : En tant qu'enseignant, je veux consulter un tableau de bord des résultats des étudiants.

**Feature : Tableau de bord des résultats**

**Tests :**

- Test que les statistiques anonymisées sont visibles.
- Test de l'accès à l'historique des résultats d'un étudiant.

### User Story 6 : En tant qu'étudiant, je veux pouvoir réaliser les QCM à tout moment.

**Feature : Réalisation des QCM**

**Tests :**

- Test que l'étudiant peut démarrer un QCM.
- Test que les réponses sont enregistrées correctement.

### User Story 7 : En tant qu'enseignant, je souhaite envoyer mes supports de cours pour générer des questions automatiquement.

**Feature : Génération automatique de questions**

**Tests :**

- Test que des questions pertinentes sont générées pour un document texte.
- Test que des questions pertinentes sont générées pour un fichier PDF.

### User Story 8 : En tant qu'enseignant, je souhaite agréger automatiquement des questions pour générer des QCM de contrôle.

**Feature : Agrégation de questions**

**Tests :**

- Test que les questions sont sélectionnées automatiquement à partir de la banque de questions.
- Test que le QCM généré contient un mélange de questions nouvelles et existantes.

### User Story 9 : En tant qu'enseignant, je souhaite pouvoir créer des QCM de révision hebdomadaire.

**Feature : Création de QCM de révision**

**Tests :**

- Test que l'enseignant peut créer un QCM en saisissant des questions.
- Test que l'enseignant peut créer un QCM en important un fichier.

## Conclusion

Chaque User Story est tracée vers une ou plusieurs Features, et chaque Feature est associée à des tests d'acceptation concrets. Cela garantit une couverture complète des exigences fonctionnelles et facilite la validation du projet.
