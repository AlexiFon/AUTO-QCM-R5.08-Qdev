Feature: Génération automatique de questions à partir des supports de cours

## En tant qu'enseignant, je souhaite envoyer mes supports de cours pour générer des questions automatiquement.
  Scenario: Envoi de supports de cours pour génération
    Given je suis connecté en tant qu'enseignant
    And j'ai un support de cours (texte ou PDF)
    When j'envoie le support de cours pour analyse
    Then des questions sont générées automatiquement
