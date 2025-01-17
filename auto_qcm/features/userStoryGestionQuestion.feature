Feature: Gestion des questions dans un espace dédié

## En tant qu'enseignant, je veux pouvoir accéder à un espace de gestion des questions.
  Scenario: Modification, suppression ou ajout de questions
    Given je suis connecté en tant qu'enseignant
    When j'accède à l'espace de gestion des questions
    Then je peux modifier une question existante
    And je peux supprimer une question
    And je peux ajouter une nouvelle question