"""Si M < 1 ou M > 12 Alors
  Ecrire "Date Invalide"
SinonSi M = 2 Alors
  Si A dp 400 Alors
    Si J < 1 ou J > 29 Alors
      Ecrire "Date Invalide"
    Sinon
      Ecrire "Date Valide"
    FinSi
  SinonSi A dp 100 Alors
    Si J < 1 ou J > 28 Alors
      Ecrire "Date Invalide"
    Sinon
      Ecrire "Date Valide"
    FinSi
  SinonSi A dp 4 Alors
    Si J < 1 ou J > 29Alors
      Ecrire "Date Invalide"
    Sinon
      Ecrire "Date Valide"
    FinSi
  Sinon
    Si J < 1 ou J > 28 Alors
      Ecrire "Date Invalide"
    Sinon
      Ecrire "Date Valide"
    FinSi
  FinSi
SinonSi M = 4 ou M = 6 ou M = 9 ou M = 11 Alors
  Si J < 1 ou J > 30 Alors
    Ecrire "Date Invalide"
  Sinon
    Ecrire "Date Valide"
  FinSi
Sinon
  Si J < 1 ou J > 31 Alors
    Ecrire "Date Invalide"
  Sinon
    Ecrire "Date Valide"
  FinSi
FinSi"""