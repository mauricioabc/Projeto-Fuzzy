from typing import Any


class InformationDicts:

    def __init__(self, entrada):
        self.entrada = entrada
        self.NitrogenioDict = None
        self.processa_nitrogenio()

    def processa_nitrogenio(self):
        if self.entrada.Cultura == 'Gramíneas':
            if self.entrada.Estacao == 'Fria':
                self.NitrogenioDict = {
                    'muito_baixo': {
                        'faixa': (0, 1.6),
                        'kg_n_ha': (160, 180)
                    },
                    'baixo': {
                        'faixa': (1.5, 2.6),
                        'kg_n_ha': (140, 160)
                    },
                    'medio': {
                        'faixa': (2.5, 3.6),
                        'kg_n_ha': (120, 140)
                    },
                    'alto': {
                        'faixa': (3.5, 4.6),
                        'kg_n_ha': (100, 120)
                    },
                    'muito_alto': {
                        'faixa': (4.5, 6),
                        'kg_n_ha': (80, 100)
                    }
                }
            if self.entrada.Estacao == 'Quente':
                self.NitrogenioDict = {
                    'muito_baixo': {
                        'faixa': (0, 1.6),
                        'kg_n_ha': (200, 220)
                    },
                    'baixo': {
                        'faixa': (1.5, 2.6),
                        'kg_n_ha': (180, 200)
                    },
                    'medio': {
                        'faixa': (2.5, 3.6),
                        'kg_n_ha': (160, 180)
                    },
                    'alto': {
                        'faixa': (3.5, 4.6),
                        'kg_n_ha': (140, 160)
                    },
                    'muito_alto': {
                        'faixa': (4.5, 6),
                        'kg_n_ha': (120, 140)
                    }
                }

        if self.entrada.Cultura == 'Milho':
            self.NitrogenioDict = {
                'muito_baixo': {
                    'faixa': (0, 1.6),
                    'kg_n_ha': (160, 170)
                },
                'baixo': {
                    'faixa': (1.5, 2.6),
                    'kg_n_ha': (150, 160)
                },
                'medio': {
                    'faixa': (2.5, 3.6),
                    'kg_n_ha': (140, 150)
                },
                'alto': {
                    'faixa': (3.5, 4.6),
                    'kg_n_ha': (130, 140)
                },
                'muito_alto': {
                    'faixa': (4.5, 6),
                    'kg_n_ha': (120, 130)
                }
            }

        if self.entrada.Cultura == 'Campo natural':
            self.NitrogenioDict = {
                'muito_baixo': {
                    'faixa': (0, 1.6),
                    'kg_n_ha': (120, 130)
                },
                'baixo': {
                    'faixa': (1.5, 2.6),
                    'kg_n_ha': (110, 120)
                },
                'medio': {
                    'faixa': (2.5, 3.6),
                    'kg_n_ha': (100, 110)
                },
                'alto': {
                    'faixa': (3.5, 4.6),
                    'kg_n_ha': (90, 100)
                },
                'muito_alto': {
                    'faixa': (4.5, 6),
                    'kg_n_ha': (80, 90)
                }
            }

        if self.entrada.Cultura == 'Campo natural misturado':
            self.NitrogenioDict = {
                'muito_baixo': {
                    'faixa': (0, 1.6),
                    'kg_n_ha': (140, 155)
                },
                'baixo': {
                    'faixa': (1.5, 2.6),
                    'kg_n_ha': (125, 140)
                },
                'medio': {
                    'faixa': (2.5, 3.6),
                    'kg_n_ha': (110, 125)
                },
                'alto': {
                    'faixa': (3.5, 4.6),
                    'kg_n_ha': (95, 110)
                },
                'muito_alto': {
                    'faixa': (4.5, 6),
                    'kg_n_ha': (80, 95)
                }
            }


    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def __str__(self) -> str:
        return super().__str__()