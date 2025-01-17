Feature: Agrégation automatique de questions pour générer des QCM

## En tant qu'enseignant, je souhaite agréger automatiquement des questions pour générer des QCM de contrôle.
  Scenario: Génération automatique de QCM
    Given je suis connecté en tant qu'enseignant
    When je sélectionne une banque de questions
    Then un QCM de contrôle est généré automatiquement