Feature: Accès aux pages pour les étudiants et enseignants

## En tant qu'étudiant, je veux avoir accès à toutes les pages qui me sont destinées.
  Scenario: Accès à une page pour les étudiants
    Given je suis connecté en tant qu'étudiant
    When je tente d'accéder à une page destinée aux étudiants
    Then je devrais voir le contenu de la page

## En tant qu'enseignant, je veux avoir accès à toutes les pages qui me sont destinées.
  Scenario: Accès à une page pour les enseignants
    Given je suis connecté en tant qu'enseignant
    When je tente d'accéder à une page destinée aux enseignants
    Then je devrais voir le contenu de la page












