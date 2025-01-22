Feature: Réalisation des QCM par les étudiants

## En tant qu'étudiant, je veux pouvoir réaliser les QCM à tout moment.
  Scenario: Réalisation d'un QCM
    Given je suis connecté en tant qu'étudiant
    And j'ai un QCM à réaliser
    When je démarre un QCM
    Then je peux répondre aux questions à mon rythme
