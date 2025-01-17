Feature: Création de QCM de révision hebdomadaire

## En tant qu'enseignant, je souhaite pouvoir créer des QCM de révision hebdomadaire.
  Scenario: Création simple de QCM
    Given je suis connecté en tant qu'enseignant
    When je saisis ou envoie des questions pour un QCM
    Then un QCM de révision hebdomadaire est créé
