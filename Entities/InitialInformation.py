from typing import Any


class InitialInformation:

    def __init__(self,Especie, Cultura, TipoPlantio, phSolo, IndiceSMP, Bases, Ca, Mg, AlSat, CTC):
        self.Especie = Especie
        self.Cultura = Cultura
        self.TipoPlantio = TipoPlantio
        self.phSolo = phSolo
        self.IndiceSMP = IndiceSMP
        self.Bases = Bases
        self.AlSat = AlSat
        self.Ca = Ca
        self.Mg = Mg
        self.CTC = CTC

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def __str__(self) -> str:
        return super().__str__()