from typing import Any


class InitialInformation:

    def __init__(self, Especie, Cultura, TipoPlantio, phSolo=None, IndiceSMP=None, Bases=None, Ca=None, Mg=None, AlSat=None, CTC=None, n=None, p=None, k=None, Inoculacao=None, Estacao=None, MateriaOrganica=None):
        self.Especie = Especie
        self.Cultura = Cultura
        self.TipoPlantio = TipoPlantio

        if phSolo is not None:
            # Se os parâmetros relacionados ao solo forem fornecidos
            self.phSolo = phSolo
            self.IndiceSMP = IndiceSMP
            self.Bases = Bases
            self.Ca = Ca
            self.Mg = Mg
            self.AlSat = AlSat
            self.CTC = CTC
        elif p is not None:
            # Se os parâmetros relacionados aos nutrientes forem fornecidos
            self.n = n
            self.p = p
            self.k = k
            self.Inoculacao = Inoculacao
            self.Estacao = Estacao
            self.MateriaOrganica = MateriaOrganica
        else:
            raise ValueError("Você deve fornecer parâmetros relacionados ao solo ou aos nutrientes.")

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def __str__(self) -> str:
        return super().__str__()