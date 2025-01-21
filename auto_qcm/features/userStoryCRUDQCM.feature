Feature: Agrégation automatique de questions pour générer des QCM

## En tant qu'enseignant, je souhaite créer des QCM à partir de une ou plusieurs questions.
  Scenario: Génération automatique de QCM
    Given je suis connecté en tant qu'enseignant
    When je crée un nouveau QCM
    Then le QCM est crée
## En tant qu'enseignant, je souhaite modifier un QCM.
  Scenario: Modification de QCM
    Given je suis connecté en tant qu'enseignant 
    And j'ai créé un QCM
    When je modifie un QCM
    Then le QCM est mis à jour

## En tant qu'enseignant, je souhaite supprimer un QCM.
  Scenario: Suppression de QCM
    Given je suis connecté en tant qu'enseignant
    And j'ai créé un QCM
    When je supprime un QCM
    Then le QCM est supprimé

## En tant qu'enseignant, je souhaite consulter un QCM.
  Scenario: Consultation de QCM
    Given je suis connecté en tant qu'enseignant
    And j'ai créé un QCM
    When je consulte un QCM
    Then le QCM est affiché