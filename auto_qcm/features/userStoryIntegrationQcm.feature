Feature: Intégration QCM avec Moodle/AMC

## En tant qu'enseignant, je souhaite établir un lien efficace entre le système de QCM et Moodle/AMC.
  Scenario: Intégration automatique des QCM
    Given je suis connecté en tant qu'enseignant
    And j'ai un QCM prêt à être intégré
    When je synchronise le QCM avec Moodle ou AMC
    Then le QCM devrait apparaître automatiquement sur la plateforme