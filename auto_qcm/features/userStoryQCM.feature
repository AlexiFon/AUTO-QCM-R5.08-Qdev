Feature: Réalisation des QCM par les étudiants

## En tant qu'étudiant, je veux pouvoir réaliser les QCM à tout moment.
  Scenario: Accès flexible aux QCM
    Given je suis connecté en tant qu'étudiant
    When je démarre un QCM
    Then je peux répondre aux questions à mon rythme
