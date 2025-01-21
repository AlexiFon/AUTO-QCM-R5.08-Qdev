Feature: Tableau de bord des résultats des étudiants

## En tant qu'enseignant, je veux consulter un tableau de bord des résultats des étudiants.
  Scenario: Consultation des statistiques des résultats
    Given je suis connecté en tant qu'enseignant
    When j'accède au tableau de bord
    Then je vois les statistiques anonymisées ou personnalisées
    And je vois l'historique des résultats des étudiants