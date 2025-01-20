Feature: Intégration QCM avec Moodle/AMC

## En tant qu'enseignant, je souhaite tester l'export des qcm vers Moodle/AMC
  Scenario: Export de QCM vers Moodle Xml
    Given je suis connecté en tant qu'enseignant
    And j'ai un QCM à exporter
    When j'exporte le qcm au format moodle xml
    Then j'ai un qcm prêt à être importé dans Moodle

  Scenario: Export de question vers Moodle Xml
    Given je suis connecté en tant qu'enseignant
    And j'ai une question à exporter
    When j'exporte la question au format moodle xml
    Then j'ai une question prête à être importé dans Moodle

  Scenario: Export de QCM vers AMC
    Given je suis connecté en tant qu'enseignant
    And j'ai un QCM à exporter
    When j'exporte le qcm au format amc
    Then j'ai un qcm au format AMC
  
  Scenario: Export de QCM vers AMC.txt
    Given je suis connecté en tant qu'enseignant
    And j'ai un QCM à exporter
    When j'exporte le qcm au format amc.txt
    Then j'ai un qcm au format AMC.txt

## En tant qu'enseignant, je souhaite tester l'import des qcm depuis Moodle/AMC

  Scenario: Import de questions vers Moodle Xml
    Given je suis connecté en tant qu'enseignant
    And j'ai des questions Moodle XML à importer
    When j'importe les questions au format moodle xml
    Then j'ai des questions prêtes à être utilisées dans un QCM
  
  Scenario: Import de questions vers AMC
    Given je suis connecté en tant qu'enseignant
    And j'ai des questions AMC à importer
    When j'importe les questions au format amc
    Then j'ai des questions prêtes à être utilisées dans un QCM
  
  Scenario: Import de questions vers AMC.txt
    Given je suis connecté en tant qu'enseignant
    And j'ai des questions AMC.txt à importer
    When j'importe les questions au format amc.txt
    Then j'ai des questions prêtes à être utilisées dans un QCM
    