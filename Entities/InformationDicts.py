from typing import Any


class InformationDicts:

    def __init__(self, entrada):
        self.entrada = entrada
        self.NitrogenioDict = None
        self.FosforoDict = None
        self.PotassioDict = None
        self.processa_nitrogenio()
        self.processa_fosforo()
        self.processa_potassio()

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

    def processa_fosforo(self):
        general_dict_fosforo = {
            'faixa_1': {
                'muito_baixo': (0, 1.6),
                'baixo': (1.4, 3.0),
                'medio': (2.9, 4.6),
                'alto': (4.5, 9.0),
                'muito_alto': (9.0, 12)
            },
            'faixa_2': {
                'muito_baixo': (0, 2.1),
                'baixo': (2, 4.0),
                'medio': (3.9, 5.9),
                'alto': (6.0, 12.0),
                'muito_alto': (12.0, 15)
            },
            'faixa_3': {
                'muito_baixo': (0, 3.1),
                'baixo': (2.9, 6.0),
                'medio': (5.9, 8.9),
                'alto': (9.0, 18.0),
                'muito_alto': (18.0, 21)
            },
            'faixa_4': {
                'muito_baixo': (0, 4.9),
                'baixo': (4.9, 10.0),
                'medio': (9.9, 14.9),
                'alto': (15, 30.0),
                'muito_alto': (30, 33)
            }
        }

        if self.entrada.Cultura == 'Alfafa':
            if float(self.entrada.TeorArgila) >= 60:
                self.FosforoDict = {
                    'muito_baixo': {
                        'faixa': general_dict_fosforo['faixa_1']['muito_baixo'],
                        'kg_p_ha': (195, 210)
                    },
                    'baixo': {
                        'faixa': general_dict_fosforo['faixa_1']['baixo'],
                        'kg_p_ha': (135, 195)
                    },
                    'medio': {
                        'faixa': general_dict_fosforo['faixa_1']['medio'],
                        'kg_p_ha': (125, 135)
                    },
                    'alto': {
                        'faixa': general_dict_fosforo['faixa_1']['alto'],
                        'kg_p_ha': (85, 125)
                    },
                    'muito_alto': {
                        'faixa': general_dict_fosforo['faixa_1']['muito_alto'],
                        'kg_p_ha': (0, 85)
                    }
                }
            elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                self.FosforoDict = {
                    'muito_baixo': {
                        'faixa': general_dict_fosforo['faixa_2']['muito_baixo'],
                        'kg_p_ha': (195, 210)
                    },
                    'baixo': {
                        'faixa': general_dict_fosforo['faixa_2']['baixo'],
                        'kg_p_ha': (135, 195)
                    },
                    'medio': {
                        'faixa': general_dict_fosforo['faixa_2']['medio'],
                        'kg_p_ha': (125, 135)
                    },
                    'alto': {
                        'faixa': general_dict_fosforo['faixa_2']['alto'],
                        'kg_p_ha': (85, 125)
                    },
                    'muito_alto': {
                        'faixa': general_dict_fosforo['faixa_2']['muito_alto'],
                        'kg_p_ha': (0, 85)
                    }
                }
            elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                self.FosforoDict = {
                    'muito_baixo': {
                        'faixa': general_dict_fosforo['faixa_3']['muito_baixo'],
                        'kg_p_ha': (195, 210)
                    },
                    'baixo': {
                        'faixa': general_dict_fosforo['faixa_3']['baixo'],
                        'kg_p_ha': (135, 195)
                    },
                    'medio': {
                        'faixa': general_dict_fosforo['faixa_3']['medio'],
                        'kg_p_ha': (125, 135)
                    },
                    'alto': {
                        'faixa': general_dict_fosforo['faixa_3']['alto'],
                        'kg_p_ha': (85, 125)
                    },
                    'muito_alto': {
                        'faixa': general_dict_fosforo['faixa_3']['muito_alto'],
                        'kg_p_ha': (0, 85)
                    }
                }
            elif float(self.entrada.TeorArgila) <= 20:
                self.FosforoDict = {
                    'muito_baixo': {
                        'faixa': general_dict_fosforo['faixa_4']['muito_baixo'],
                        'kg_p_ha': (195, 210)
                    },
                    'baixo': {
                        'faixa': general_dict_fosforo['faixa_4']['baixo'],
                        'kg_p_ha': (135, 195)
                    },
                    'medio': {
                        'faixa': general_dict_fosforo['faixa_4']['medio'],
                        'kg_p_ha': (125, 135)
                    },
                    'alto': {
                        'faixa': general_dict_fosforo['faixa_4']['alto'],
                        'kg_p_ha': (85, 125)
                    },
                    'muito_alto': {
                        'faixa': general_dict_fosforo['faixa_4']['muito_alto'],
                        'kg_p_ha': (0, 85)
                    }
                }

        if self.entrada.Cultura == 'Gramíneas':
            if self.entrada.Estacao == 'Fria':
                if float(self.entrada.TeorArgila) >= 60:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_1']['muito_baixo'],
                            'kg_p_ha': (170, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_1']['baixo'],
                            'kg_p_ha': (110, 170)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_1']['medio'],
                            'kg_p_ha': (100, 110)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_1']['alto'],
                            'kg_p_ha': (60, 100)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_1']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_2']['muito_baixo'],
                            'kg_p_ha': (170, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_2']['baixo'],
                            'kg_p_ha': (110, 170)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_2']['medio'],
                            'kg_p_ha': (100, 110)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_2']['alto'],
                            'kg_p_ha': (60, 100)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_2']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_3']['muito_baixo'],
                            'kg_p_ha': (170, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_3']['baixo'],
                            'kg_p_ha': (110, 170)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_3']['medio'],
                            'kg_p_ha': (100, 110)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_3']['alto'],
                            'kg_p_ha': (60, 100)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_3']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) <= 20:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_4']['muito_baixo'],
                            'kg_p_ha': (170, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_4']['baixo'],
                            'kg_p_ha': (110, 170)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_4']['medio'],
                            'kg_p_ha': (100, 110)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_4']['alto'],
                            'kg_p_ha': (60, 100)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_4']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
            if self.entrada.Estacao == 'Quente':
                if float(self.entrada.TeorArgila) >= 60:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_1']['muito_baixo'],
                            'kg_p_ha': (190, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_1']['baixo'],
                            'kg_p_ha': (130, 190)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_1']['medio'],
                            'kg_p_ha': (120, 130)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_1']['alto'],
                            'kg_p_ha': (80, 120)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_1']['muito_alto'],
                            'kg_p_ha': (0, 80)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_2']['muito_baixo'],
                            'kg_p_ha': (190, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_2']['baixo'],
                            'kg_p_ha': (130, 190)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_2']['medio'],
                            'kg_p_ha': (120, 130)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_2']['alto'],
                            'kg_p_ha': (80, 120)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_2']['muito_alto'],
                            'kg_p_ha': (0, 80)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_3']['muito_baixo'],
                            'kg_p_ha': (190, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_3']['baixo'],
                            'kg_p_ha': (130, 190)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_3']['medio'],
                            'kg_p_ha': (120, 130)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_3']['alto'],
                            'kg_p_ha': (80, 120)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_3']['muito_alto'],
                            'kg_p_ha': (0, 80)
                        }
                    }
                elif float(self.entrada.TeorArgila) <= 20:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_4']['muito_baixo'],
                            'kg_p_ha': (190, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_4']['baixo'],
                            'kg_p_ha': (130, 190)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_4']['medio'],
                            'kg_p_ha': (120, 130)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_4']['alto'],
                            'kg_p_ha': (80, 120)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_4']['muito_alto'],
                            'kg_p_ha': (0, 80)
                        }
                    }

        if self.entrada.Cultura == 'Leguminosas':
            if self.entrada.Estacao == 'Fria':
                if float(self.entrada.TeorArgila) >= 60:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_1']['muito_baixo'],
                            'kg_p_ha': (170, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_1']['baixo'],
                            'kg_p_ha': (110, 170)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_1']['medio'],
                            'kg_p_ha': (100, 110)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_1']['alto'],
                            'kg_p_ha': (60, 100)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_1']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_2']['muito_baixo'],
                            'kg_p_ha': (170, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_2']['baixo'],
                            'kg_p_ha': (110, 170)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_2']['medio'],
                            'kg_p_ha': (100, 110)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_2']['alto'],
                            'kg_p_ha': (60, 100)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_2']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_3']['muito_baixo'],
                            'kg_p_ha': (170, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_3']['baixo'],
                            'kg_p_ha': (110, 170)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_3']['medio'],
                            'kg_p_ha': (100, 110)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_3']['alto'],
                            'kg_p_ha': (60, 100)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_3']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) <= 20:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_4']['muito_baixo'],
                            'kg_p_ha': (170, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_4']['baixo'],
                            'kg_p_ha': (110, 170)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_4']['medio'],
                            'kg_p_ha': (100, 110)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_4']['alto'],
                            'kg_p_ha': (60, 100)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_4']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
            if self.entrada.Estacao == 'Quente':
                if float(self.entrada.TeorArgila) >= 60:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_1']['muito_baixo'],
                            'kg_p_ha': (170, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_1']['baixo'],
                            'kg_p_ha': (110, 170)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_1']['medio'],
                            'kg_p_ha': (100, 110)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_1']['alto'],
                            'kg_p_ha': (60, 100)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_1']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_2']['muito_baixo'],
                            'kg_p_ha': (170, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_2']['baixo'],
                            'kg_p_ha': (110, 170)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_2']['medio'],
                            'kg_p_ha': (100, 110)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_2']['alto'],
                            'kg_p_ha': (60, 100)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_2']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_3']['muito_baixo'],
                            'kg_p_ha': (170, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_3']['baixo'],
                            'kg_p_ha': (110, 170)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_3']['medio'],
                            'kg_p_ha': (100, 110)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_3']['alto'],
                            'kg_p_ha': (60, 100)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_3']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) <= 20:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_4']['muito_baixo'],
                            'kg_p_ha': (170, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_4']['baixo'],
                            'kg_p_ha': (110, 170)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_4']['medio'],
                            'kg_p_ha': (100, 110)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_4']['alto'],
                            'kg_p_ha': (60, 100)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_4']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }

        if self.entrada.Cultura == 'Consórcios':
            if self.entrada.Estacao == 'Fria':
                if float(self.entrada.TeorArgila) >= 60:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_1']['muito_baixo'],
                            'kg_p_ha': (170, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_1']['baixo'],
                            'kg_p_ha': (110, 170)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_1']['medio'],
                            'kg_p_ha': (100, 110)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_1']['alto'],
                            'kg_p_ha': (60, 100)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_1']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_2']['muito_baixo'],
                            'kg_p_ha': (170, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_2']['baixo'],
                            'kg_p_ha': (110, 170)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_2']['medio'],
                            'kg_p_ha': (100, 110)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_2']['alto'],
                            'kg_p_ha': (60, 100)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_2']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_3']['muito_baixo'],
                            'kg_p_ha': (170, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_3']['baixo'],
                            'kg_p_ha': (110, 170)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_3']['medio'],
                            'kg_p_ha': (100, 110)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_3']['alto'],
                            'kg_p_ha': (60, 100)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_3']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) <= 20:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_4']['muito_baixo'],
                            'kg_p_ha': (170, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_4']['baixo'],
                            'kg_p_ha': (110, 170)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_4']['medio'],
                            'kg_p_ha': (100, 110)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_4']['alto'],
                            'kg_p_ha': (60, 100)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_4']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
            if self.entrada.Estacao == 'Quente':
                if float(self.entrada.TeorArgila) >= 60:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_1']['muito_baixo'],
                            'kg_p_ha': (190, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_1']['baixo'],
                            'kg_p_ha': (130, 190)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_1']['medio'],
                            'kg_p_ha': (120, 130)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_1']['alto'],
                            'kg_p_ha': (80, 120)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_1']['muito_alto'],
                            'kg_p_ha': (0, 80)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_2']['muito_baixo'],
                            'kg_p_ha': (190, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_2']['baixo'],
                            'kg_p_ha': (130, 190)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_2']['medio'],
                            'kg_p_ha': (120, 130)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_2']['alto'],
                            'kg_p_ha': (80, 120)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_2']['muito_alto'],
                            'kg_p_ha': (0, 80)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_3']['muito_baixo'],
                            'kg_p_ha': (190, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_3']['baixo'],
                            'kg_p_ha': (130, 190)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_3']['medio'],
                            'kg_p_ha': (120, 130)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_3']['alto'],
                            'kg_p_ha': (80, 120)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_3']['muito_alto'],
                            'kg_p_ha': (0, 80)
                        }
                    }
                elif float(self.entrada.TeorArgila) <= 20:
                    self.FosforoDict = {
                        'muito_baixo': {
                            'faixa': general_dict_fosforo['faixa_4']['muito_baixo'],
                            'kg_p_ha': (190, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_fosforo['faixa_4']['baixo'],
                            'kg_p_ha': (130, 190)
                        },
                        'medio': {
                            'faixa': general_dict_fosforo['faixa_4']['medio'],
                            'kg_p_ha': (120, 130)
                        },
                        'alto': {
                            'faixa': general_dict_fosforo['faixa_4']['alto'],
                            'kg_p_ha': (80, 120)
                        },
                        'muito_alto': {
                            'faixa': general_dict_fosforo['faixa_4']['muito_alto'],
                            'kg_p_ha': (0, 80)
                        }
                    }

        if self.entrada.Cultura == 'Milho':
            if float(self.entrada.TeorArgila) >= 60:
                self.FosforoDict = {
                    'muito_baixo': {
                        'faixa': general_dict_fosforo['faixa_1']['muito_baixo'],
                        'kg_p_ha': (220, 240)
                    },
                    'baixo': {
                        'faixa': general_dict_fosforo['faixa_1']['baixo'],
                        'kg_p_ha': (160, 220)
                    },
                    'medio': {
                        'faixa': general_dict_fosforo['faixa_1']['medio'],
                        'kg_p_ha': (150, 160)
                    },
                    'alto': {
                        'faixa': general_dict_fosforo['faixa_1']['alto'],
                        'kg_p_ha': (110, 150)
                    },
                    'muito_alto': {
                        'faixa': general_dict_fosforo['faixa_1']['muito_alto'],
                        'kg_p_ha': (0, 110)
                    }
                }
            elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                self.FosforoDict = {
                    'muito_baixo': {
                        'faixa': general_dict_fosforo['faixa_2']['muito_baixo'],
                        'kg_p_ha': (170, 210)
                    },
                    'baixo': {
                        'faixa': general_dict_fosforo['faixa_2']['baixo'],
                        'kg_p_ha': (110, 170)
                    },
                    'medio': {
                        'faixa': general_dict_fosforo['faixa_2']['medio'],
                        'kg_p_ha': (100, 110)
                    },
                    'alto': {
                        'faixa': general_dict_fosforo['faixa_2']['alto'],
                        'kg_p_ha': (60, 100)
                    },
                    'muito_alto': {
                        'faixa': general_dict_fosforo['faixa_2']['muito_alto'],
                        'kg_p_ha': (0, 60)
                    }
                }
            elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                self.FosforoDict = {
                    'muito_baixo': {
                        'faixa': general_dict_fosforo['faixa_3']['muito_baixo'],
                        'kg_p_ha': (170, 210)
                    },
                    'baixo': {
                        'faixa': general_dict_fosforo['faixa_3']['baixo'],
                        'kg_p_ha': (110, 170)
                    },
                    'medio': {
                        'faixa': general_dict_fosforo['faixa_3']['medio'],
                        'kg_p_ha': (100, 110)
                    },
                    'alto': {
                        'faixa': general_dict_fosforo['faixa_3']['alto'],
                        'kg_p_ha': (60, 100)
                    },
                    'muito_alto': {
                        'faixa': general_dict_fosforo['faixa_3']['muito_alto'],
                        'kg_p_ha': (0, 60)
                    }
                }
            elif float(self.entrada.TeorArgila) <= 20:
                self.FosforoDict = {
                    'muito_baixo': {
                        'faixa': general_dict_fosforo['faixa_4']['muito_baixo'],
                        'kg_p_ha': (170, 210)
                    },
                    'baixo': {
                        'faixa': general_dict_fosforo['faixa_4']['baixo'],
                        'kg_p_ha': (110, 170)
                    },
                    'medio': {
                        'faixa': general_dict_fosforo['faixa_4']['medio'],
                        'kg_p_ha': (100, 110)
                    },
                    'alto': {
                        'faixa': general_dict_fosforo['faixa_4']['alto'],
                        'kg_p_ha': (60, 100)
                    },
                    'muito_alto': {
                        'faixa': general_dict_fosforo['faixa_4']['muito_alto'],
                        'kg_p_ha': (0, 60)
                    }
                }

        if self.entrada.Cultura == 'Campo natural':
            if float(self.entrada.TeorArgila) >= 60:
                self.FosforoDict = {
                    'muito_baixo': {
                        'faixa': general_dict_fosforo['faixa_1']['muito_baixo'],
                        'kg_p_ha': (100, 120)
                    },
                    'baixo': {
                        'faixa': general_dict_fosforo['faixa_1']['baixo'],
                        'kg_p_ha': (75, 100)
                    },
                    'medio': {
                        'faixa': general_dict_fosforo['faixa_1']['medio'],
                        'kg_p_ha': (70, 75)
                    },
                    'alto': {
                        'faixa': general_dict_fosforo['faixa_1']['alto'],
                        'kg_p_ha': (50, 70)
                    },
                    'muito_alto': {
                        'faixa': general_dict_fosforo['faixa_1']['muito_alto'],
                        'kg_p_ha': (0, 50)
                    }
                }
            elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                self.FosforoDict = {
                    'muito_baixo': {
                        'faixa': general_dict_fosforo['faixa_2']['muito_baixo'],
                        'kg_p_ha': (170, 210)
                    },
                    'baixo': {
                        'faixa': general_dict_fosforo['faixa_2']['baixo'],
                        'kg_p_ha': (110, 170)
                    },
                    'medio': {
                        'faixa': general_dict_fosforo['faixa_2']['medio'],
                        'kg_p_ha': (100, 110)
                    },
                    'alto': {
                        'faixa': general_dict_fosforo['faixa_2']['alto'],
                        'kg_p_ha': (60, 100)
                    },
                    'muito_alto': {
                        'faixa': general_dict_fosforo['faixa_2']['muito_alto'],
                        'kg_p_ha': (0, 60)
                    }
                }
            elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                self.FosforoDict = {
                    'muito_baixo': {
                        'faixa': general_dict_fosforo['faixa_3']['muito_baixo'],
                        'kg_p_ha': (170, 210)
                    },
                    'baixo': {
                        'faixa': general_dict_fosforo['faixa_3']['baixo'],
                        'kg_p_ha': (110, 170)
                    },
                    'medio': {
                        'faixa': general_dict_fosforo['faixa_3']['medio'],
                        'kg_p_ha': (100, 110)
                    },
                    'alto': {
                        'faixa': general_dict_fosforo['faixa_3']['alto'],
                        'kg_p_ha': (60, 100)
                    },
                    'muito_alto': {
                        'faixa': general_dict_fosforo['faixa_3']['muito_alto'],
                        'kg_p_ha': (0, 60)
                    }
                }
            elif float(self.entrada.TeorArgila) <= 20:
                self.FosforoDict = {
                    'muito_baixo': {
                        'faixa': general_dict_fosforo['faixa_4']['muito_baixo'],
                        'kg_p_ha': (170, 210)
                    },
                    'baixo': {
                        'faixa': general_dict_fosforo['faixa_4']['baixo'],
                        'kg_p_ha': (110, 170)
                    },
                    'medio': {
                        'faixa': general_dict_fosforo['faixa_4']['medio'],
                        'kg_p_ha': (100, 110)
                    },
                    'alto': {
                        'faixa': general_dict_fosforo['faixa_4']['alto'],
                        'kg_p_ha': (60, 100)
                    },
                    'muito_alto': {
                        'faixa': general_dict_fosforo['faixa_4']['muito_alto'],
                        'kg_p_ha': (0, 60)
                    }
                }

        if self.entrada.Cultura == 'Campo natural misturado':
            if float(self.entrada.TeorArgila) >= 60:
                self.FosforoDict = {
                    'muito_baixo': {
                        'faixa': general_dict_fosforo['faixa_1']['muito_baixo'],
                        'kg_p_ha': (160, 190)
                    },
                    'baixo': {
                        'faixa': general_dict_fosforo['faixa_1']['baixo'],
                        'kg_p_ha': (100, 160)
                    },
                    'medio': {
                        'faixa': general_dict_fosforo['faixa_1']['medio'],
                        'kg_p_ha': (90, 100)
                    },
                    'alto': {
                        'faixa': general_dict_fosforo['faixa_1']['alto'],
                        'kg_p_ha': (50, 90)
                    },
                    'muito_alto': {
                        'faixa': general_dict_fosforo['faixa_1']['muito_alto'],
                        'kg_p_ha': (0, 50)
                    }
                }
            elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                self.FosforoDict = {
                    'muito_baixo': {
                        'faixa': general_dict_fosforo['faixa_2']['muito_baixo'],
                        'kg_p_ha': (170, 210)
                    },
                    'baixo': {
                        'faixa': general_dict_fosforo['faixa_2']['baixo'],
                        'kg_p_ha': (110, 170)
                    },
                    'medio': {
                        'faixa': general_dict_fosforo['faixa_2']['medio'],
                        'kg_p_ha': (100, 110)
                    },
                    'alto': {
                        'faixa': general_dict_fosforo['faixa_2']['alto'],
                        'kg_p_ha': (60, 100)
                    },
                    'muito_alto': {
                        'faixa': general_dict_fosforo['faixa_2']['muito_alto'],
                        'kg_p_ha': (0, 60)
                    }
                }
            elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                self.FosforoDict = {
                    'muito_baixo': {
                        'faixa': general_dict_fosforo['faixa_3']['muito_baixo'],
                        'kg_p_ha': (170, 210)
                    },
                    'baixo': {
                        'faixa': general_dict_fosforo['faixa_3']['baixo'],
                        'kg_p_ha': (110, 170)
                    },
                    'medio': {
                        'faixa': general_dict_fosforo['faixa_3']['medio'],
                        'kg_p_ha': (100, 110)
                    },
                    'alto': {
                        'faixa': general_dict_fosforo['faixa_3']['alto'],
                        'kg_p_ha': (60, 100)
                    },
                    'muito_alto': {
                        'faixa': general_dict_fosforo['faixa_3']['muito_alto'],
                        'kg_p_ha': (0, 60)
                    }
                }
            elif float(self.entrada.TeorArgila) <= 20:
                self.FosforoDict = {
                    'muito_baixo': {
                        'faixa': general_dict_fosforo['faixa_4']['muito_baixo'],
                        'kg_p_ha': (170, 210)
                    },
                    'baixo': {
                        'faixa': general_dict_fosforo['faixa_4']['baixo'],
                        'kg_p_ha': (110, 170)
                    },
                    'medio': {
                        'faixa': general_dict_fosforo['faixa_4']['medio'],
                        'kg_p_ha': (100, 110)
                    },
                    'alto': {
                        'faixa': general_dict_fosforo['faixa_4']['alto'],
                        'kg_p_ha': (60, 100)
                    },
                    'muito_alto': {
                        'faixa': general_dict_fosforo['faixa_4']['muito_alto'],
                        'kg_p_ha': (0, 60)
                    }
                }

    def processa_potassio(self):
        general_dict_potassio = {
            'faixa_1': {
                'muito_baixo': (0, 16),
                'baixo': (15.9, 31),
                'medio': (30.9, 46),
                'alto': (45.9, 91),
                'muito_alto': (90.9, 110)
            },
            'faixa_2': {
                'muito_baixo': (0, 21),
                'baixo': (20.9, 41),
                'medio': (40.9, 61),
                'alto': (60.9, 121),
                'muito_alto': (120.9, 140)
            },
            'faixa_3': {
                'muito_baixo': (0, 31),
                'baixo': (30.9, 61),
                'medio': (60.9, 91),
                'alto': (90.9, 181),
                'muito_alto': (180.9, 200)
            },
            'faixa_4': {
                'muito_baixo': (0, 36),
                'baixo': (36.9, 71),
                'medio': (70.9, 106),
                'alto': (105.9, 211),
                'muito_alto': (210.9, 230)
            }
        }

        if self.entrada.Cultura == 'Alfafa':
            if float(self.entrada.TeorArgila) >= 60:
                self.PotassioDict = {
                    'muito_baixo': {
                        'faixa': general_dict_potassio['faixa_1']['muito_baixo'],
                        'kg_p_ha': (330, 360)
                    },
                    'baixo': {
                        'faixa': general_dict_potassio['faixa_1']['baixo'],
                        'kg_p_ha': (290, 330)
                    },
                    'medio': {
                        'faixa': general_dict_potassio['faixa_1']['medio'],
                        'kg_p_ha': (280, 290)
                    },
                    'alto': {
                        'faixa': general_dict_potassio['faixa_1']['alto'],
                        'kg_p_ha': (250, 280)
                    },
                    'muito_alto': {
                        'faixa': general_dict_potassio['faixa_1']['muito_alto'],
                        'kg_p_ha': (0, 250)
                    }
                }
            elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                self.PotassioDict = {
                    'muito_baixo': {
                        'faixa': general_dict_potassio['faixa_2']['muito_baixo'],
                        'kg_p_ha': (330, 360)
                    },
                    'baixo': {
                        'faixa': general_dict_potassio['faixa_2']['baixo'],
                        'kg_p_ha': (290, 330)
                    },
                    'medio': {
                        'faixa': general_dict_potassio['faixa_2']['medio'],
                        'kg_p_ha': (280, 290)
                    },
                    'alto': {
                        'faixa': general_dict_potassio['faixa_2']['alto'],
                        'kg_p_ha': (250, 280)
                    },
                    'muito_alto': {
                        'faixa': general_dict_potassio['faixa_2']['muito_alto'],
                        'kg_p_ha': (0, 250)
                    }
                }
            elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                self.PotassioDict = {
                    'muito_baixo': {
                        'faixa': general_dict_potassio['faixa_3']['muito_baixo'],
                        'kg_p_ha': (330, 360)
                    },
                    'baixo': {
                        'faixa': general_dict_potassio['faixa_3']['baixo'],
                        'kg_p_ha': (290, 330)
                    },
                    'medio': {
                        'faixa': general_dict_potassio['faixa_3']['medio'],
                        'kg_p_ha': (280, 290)
                    },
                    'alto': {
                        'faixa': general_dict_potassio['faixa_3']['alto'],
                        'kg_p_ha': (250, 280)
                    },
                    'muito_alto': {
                        'faixa': general_dict_potassio['faixa_3']['muito_alto'],
                        'kg_p_ha': (0, 250)
                    }
                }
            elif float(self.entrada.TeorArgila) <= 20:
                self.PotassioDict = {
                    'muito_baixo': {
                        'faixa': general_dict_potassio['faixa_4']['muito_baixo'],
                        'kg_p_ha': (330, 360)
                    },
                    'baixo': {
                        'faixa': general_dict_potassio['faixa_4']['baixo'],
                        'kg_p_ha': (290, 330)
                    },
                    'medio': {
                        'faixa': general_dict_potassio['faixa_4']['medio'],
                        'kg_p_ha': (280, 290)
                    },
                    'alto': {
                        'faixa': general_dict_potassio['faixa_4']['alto'],
                        'kg_p_ha': (250, 280)
                    },
                    'muito_alto': {
                        'faixa': general_dict_potassio['faixa_4']['muito_alto'],
                        'kg_p_ha': (0, 250)
                    }
                }

        if self.entrada.Cultura == 'Gramíneas':
            if self.entrada.Estacao == 'Fria':
                if float(self.entrada.TeorArgila) >= 60:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_1']['muito_baixo'],
                            'kg_p_ha': (140, 170)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_1']['baixo'],
                            'kg_p_ha': (100, 140)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_1']['medio'],
                            'kg_p_ha': (90, 100)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_1']['alto'],
                            'kg_p_ha': (60, 90)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_1']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_2']['muito_baixo'],
                            'kg_p_ha': (140, 170)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_2']['baixo'],
                            'kg_p_ha': (100, 140)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_2']['medio'],
                            'kg_p_ha': (90, 100)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_2']['alto'],
                            'kg_p_ha': (60, 90)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_2']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_3']['muito_baixo'],
                            'kg_p_ha': (140, 170)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_3']['baixo'],
                            'kg_p_ha': (100, 140)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_3']['medio'],
                            'kg_p_ha': (90, 100)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_3']['alto'],
                            'kg_p_ha': (60, 90)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_3']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) <= 20:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_4']['muito_baixo'],
                            'kg_p_ha': (140, 170)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_4']['baixo'],
                            'kg_p_ha': (100, 140)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_4']['medio'],
                            'kg_p_ha': (90, 100)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_4']['alto'],
                            'kg_p_ha': (60, 90)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_4']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
            if self.entrada.Estacao == 'Quente':
                if float(self.entrada.TeorArgila) >= 60:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_1']['muito_baixo'],
                            'kg_p_ha': (180, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_1']['baixo'],
                            'kg_p_ha': (140, 180)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_1']['medio'],
                            'kg_p_ha': (130, 140)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_1']['alto'],
                            'kg_p_ha': (100, 130)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_1']['muito_alto'],
                            'kg_p_ha': (0, 100)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_2']['muito_baixo'],
                            'kg_p_ha': (180, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_2']['baixo'],
                            'kg_p_ha': (140, 180)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_2']['medio'],
                            'kg_p_ha': (130, 140)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_2']['alto'],
                            'kg_p_ha': (100, 130)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_2']['muito_alto'],
                            'kg_p_ha': (0, 100)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_3']['muito_baixo'],
                            'kg_p_ha': (180, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_3']['baixo'],
                            'kg_p_ha': (140, 180)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_3']['medio'],
                            'kg_p_ha': (130, 140)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_3']['alto'],
                            'kg_p_ha': (100, 130)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_3']['muito_alto'],
                            'kg_p_ha': (0, 100)
                        }
                    }
                elif float(self.entrada.TeorArgila) <= 20:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_4']['muito_baixo'],
                            'kg_p_ha': (180, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_4']['baixo'],
                            'kg_p_ha': (140, 180)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_4']['medio'],
                            'kg_p_ha': (130, 140)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_4']['alto'],
                            'kg_p_ha': (100, 130)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_4']['muito_alto'],
                            'kg_p_ha': (0, 100)
                        }
                    }

        if self.entrada.Cultura == 'Leguminosas':
            if self.entrada.Estacao == 'Fria':
                if float(self.entrada.TeorArgila) >= 60:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_1']['muito_baixo'],
                            'kg_p_ha': (140, 170)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_1']['baixo'],
                            'kg_p_ha': (100, 140)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_1']['medio'],
                            'kg_p_ha': (90, 100)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_1']['alto'],
                            'kg_p_ha': (60, 90)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_1']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_2']['muito_baixo'],
                            'kg_p_ha': (140, 170)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_2']['baixo'],
                            'kg_p_ha': (100, 140)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_2']['medio'],
                            'kg_p_ha': (90, 100)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_2']['alto'],
                            'kg_p_ha': (60, 90)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_2']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_3']['muito_baixo'],
                            'kg_p_ha': (140, 170)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_3']['baixo'],
                            'kg_p_ha': (100, 140)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_3']['medio'],
                            'kg_p_ha': (90, 100)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_3']['alto'],
                            'kg_p_ha': (60, 90)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_3']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) <= 20:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_4']['muito_baixo'],
                            'kg_p_ha': (140, 170)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_4']['baixo'],
                            'kg_p_ha': (100, 140)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_4']['medio'],
                            'kg_p_ha': (90, 100)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_4']['alto'],
                            'kg_p_ha': (60, 90)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_4']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
            if self.entrada.Estacao == 'Quente':
                if float(self.entrada.TeorArgila) >= 60:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_1']['muito_baixo'],
                            'kg_p_ha': (140, 170)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_1']['baixo'],
                            'kg_p_ha': (100, 140)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_1']['medio'],
                            'kg_p_ha': (90, 100)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_1']['alto'],
                            'kg_p_ha': (60, 90)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_1']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_2']['muito_baixo'],
                            'kg_p_ha': (140, 170)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_2']['baixo'],
                            'kg_p_ha': (100, 140)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_2']['medio'],
                            'kg_p_ha': (90, 100)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_2']['alto'],
                            'kg_p_ha': (60, 90)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_2']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_3']['muito_baixo'],
                            'kg_p_ha': (140, 170)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_3']['baixo'],
                            'kg_p_ha': (100, 140)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_3']['medio'],
                            'kg_p_ha': (90, 100)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_3']['alto'],
                            'kg_p_ha': (60, 90)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_3']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) <= 20:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_4']['muito_baixo'],
                            'kg_p_ha': (140, 170)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_4']['baixo'],
                            'kg_p_ha': (100, 140)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_4']['medio'],
                            'kg_p_ha': (90, 100)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_4']['alto'],
                            'kg_p_ha': (60, 90)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_4']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }

        if self.entrada.Cultura == 'Consórcios':
            if self.entrada.Estacao == 'Fria':
                if float(self.entrada.TeorArgila) >= 60:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_1']['muito_baixo'],
                            'kg_p_ha': (140, 170)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_1']['baixo'],
                            'kg_p_ha': (100, 140)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_1']['medio'],
                            'kg_p_ha': (90, 100)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_1']['alto'],
                            'kg_p_ha': (60, 90)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_1']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_2']['muito_baixo'],
                            'kg_p_ha': (140, 170)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_2']['baixo'],
                            'kg_p_ha': (100, 140)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_2']['medio'],
                            'kg_p_ha': (90, 100)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_2']['alto'],
                            'kg_p_ha': (60, 90)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_2']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_3']['muito_baixo'],
                            'kg_p_ha': (140, 170)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_3']['baixo'],
                            'kg_p_ha': (100, 140)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_3']['medio'],
                            'kg_p_ha': (90, 100)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_3']['alto'],
                            'kg_p_ha': (60, 90)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_3']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
                elif float(self.entrada.TeorArgila) <= 20:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_4']['muito_baixo'],
                            'kg_p_ha': (140, 170)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_4']['baixo'],
                            'kg_p_ha': (100, 140)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_4']['medio'],
                            'kg_p_ha': (90, 100)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_4']['alto'],
                            'kg_p_ha': (60, 90)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_4']['muito_alto'],
                            'kg_p_ha': (0, 60)
                        }
                    }
            if self.entrada.Estacao == 'Quente':
                if float(self.entrada.TeorArgila) >= 60:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_1']['muito_baixo'],
                            'kg_p_ha': (180, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_1']['baixo'],
                            'kg_p_ha': (140, 180)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_1']['medio'],
                            'kg_p_ha': (130, 140)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_1']['alto'],
                            'kg_p_ha': (100, 130)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_1']['muito_alto'],
                            'kg_p_ha': (0, 100)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_2']['muito_baixo'],
                            'kg_p_ha': (180, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_2']['baixo'],
                            'kg_p_ha': (140, 180)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_2']['medio'],
                            'kg_p_ha': (130, 140)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_2']['alto'],
                            'kg_p_ha': (100, 130)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_2']['muito_alto'],
                            'kg_p_ha': (0, 100)
                        }
                    }
                elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_3']['muito_baixo'],
                            'kg_p_ha': (180, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_3']['baixo'],
                            'kg_p_ha': (140, 180)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_3']['medio'],
                            'kg_p_ha': (130, 140)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_3']['alto'],
                            'kg_p_ha': (100, 130)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_3']['muito_alto'],
                            'kg_p_ha': (0, 100)
                        }
                    }
                elif float(self.entrada.TeorArgila) <= 20:
                    self.PotassioDict = {
                        'muito_baixo': {
                            'faixa': general_dict_potassio['faixa_4']['muito_baixo'],
                            'kg_p_ha': (180, 210)
                        },
                        'baixo': {
                            'faixa': general_dict_potassio['faixa_4']['baixo'],
                            'kg_p_ha': (140, 180)
                        },
                        'medio': {
                            'faixa': general_dict_potassio['faixa_4']['medio'],
                            'kg_p_ha': (130, 140)
                        },
                        'alto': {
                            'faixa': general_dict_potassio['faixa_4']['alto'],
                            'kg_p_ha': (100, 130)
                        },
                        'muito_alto': {
                            'faixa': general_dict_potassio['faixa_4']['muito_alto'],
                            'kg_p_ha': (0, 100)
                        }
                    }

        if self.entrada.Cultura == 'Milho':
            if float(self.entrada.TeorArgila) >= 60:
                self.PotassioDict = {
                    'muito_baixo': {
                        'faixa': general_dict_potassio['faixa_1']['muito_baixo'],
                        'kg_p_ha': (300, 330)
                    },
                    'baixo': {
                        'faixa': general_dict_potassio['faixa_1']['baixo'],
                        'kg_p_ha': (260, 300)
                    },
                    'medio': {
                        'faixa': general_dict_potassio['faixa_1']['medio'],
                        'kg_p_ha': (250, 260)
                    },
                    'alto': {
                        'faixa': general_dict_potassio['faixa_1']['alto'],
                        'kg_p_ha': (220, 250)
                    },
                    'muito_alto': {
                        'faixa': general_dict_potassio['faixa_1']['muito_alto'],
                        'kg_p_ha': (0, 220)
                    }
                }
            elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                self.PotassioDict = {
                    'muito_baixo': {
                        'faixa': general_dict_potassio['faixa_2']['muito_baixo'],
                        'kg_p_ha': (300, 330)
                    },
                    'baixo': {
                        'faixa': general_dict_potassio['faixa_2']['baixo'],
                        'kg_p_ha': (260, 300)
                    },
                    'medio': {
                        'faixa': general_dict_potassio['faixa_2']['medio'],
                        'kg_p_ha': (250, 260)
                    },
                    'alto': {
                        'faixa': general_dict_potassio['faixa_2']['alto'],
                        'kg_p_ha': (220, 250)
                    },
                    'muito_alto': {
                        'faixa': general_dict_potassio['faixa_2']['muito_alto'],
                        'kg_p_ha': (0, 220)
                    }
                }
            elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                self.PotassioDict = {
                    'muito_baixo': {
                        'faixa': general_dict_potassio['faixa_3']['muito_baixo'],
                        'kg_p_ha': (300, 330)
                    },
                    'baixo': {
                        'faixa': general_dict_potassio['faixa_3']['baixo'],
                        'kg_p_ha': (260, 300)
                    },
                    'medio': {
                        'faixa': general_dict_potassio['faixa_3']['medio'],
                        'kg_p_ha': (250, 260)
                    },
                    'alto': {
                        'faixa': general_dict_potassio['faixa_3']['alto'],
                        'kg_p_ha': (220, 250)
                    },
                    'muito_alto': {
                        'faixa': general_dict_potassio['faixa_3']['muito_alto'],
                        'kg_p_ha': (0, 220)
                    }
                }
            elif float(self.entrada.TeorArgila) <= 20:
                self.PotassioDict = {
                    'muito_baixo': {
                        'faixa': general_dict_potassio['faixa_4']['muito_baixo'],
                        'kg_p_ha': (300, 330)
                    },
                    'baixo': {
                        'faixa': general_dict_potassio['faixa_4']['baixo'],
                        'kg_p_ha': (260, 300)
                    },
                    'medio': {
                        'faixa': general_dict_potassio['faixa_4']['medio'],
                        'kg_p_ha': (250, 260)
                    },
                    'alto': {
                        'faixa': general_dict_potassio['faixa_4']['alto'],
                        'kg_p_ha': (220, 250)
                    },
                    'muito_alto': {
                        'faixa': general_dict_potassio['faixa_4']['muito_alto'],
                        'kg_p_ha': (0, 220)
                    }
                }

        if self.entrada.Cultura == 'Campo natural':
            if float(self.entrada.TeorArgila) >= 60:
                self.PotassioDict = {
                    'muito_baixo': {
                        'faixa': general_dict_potassio['faixa_1']['muito_baixo'],
                        'kg_p_ha': (100, 130)
                    },
                    'baixo': {
                        'faixa': general_dict_potassio['faixa_1']['baixo'],
                        'kg_p_ha': (75, 100)
                    },
                    'medio': {
                        'faixa': general_dict_potassio['faixa_1']['medio'],
                        'kg_p_ha': (70, 75)
                    },
                    'alto': {
                        'faixa': general_dict_potassio['faixa_1']['alto'],
                        'kg_p_ha': (50, 70)
                    },
                    'muito_alto': {
                        'faixa': general_dict_potassio['faixa_1']['muito_alto'],
                        'kg_p_ha': (0, 50)
                    }
                }
            elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                self.PotassioDict = {
                    'muito_baixo': {
                        'faixa': general_dict_potassio['faixa_2']['muito_baixo'],
                        'kg_p_ha': (100, 130)
                    },
                    'baixo': {
                        'faixa': general_dict_potassio['faixa_2']['baixo'],
                        'kg_p_ha': (75, 100)
                    },
                    'medio': {
                        'faixa': general_dict_potassio['faixa_2']['medio'],
                        'kg_p_ha': (70, 75)
                    },
                    'alto': {
                        'faixa': general_dict_potassio['faixa_2']['alto'],
                        'kg_p_ha': (50, 70)
                    },
                    'muito_alto': {
                        'faixa': general_dict_potassio['faixa_2']['muito_alto'],
                        'kg_p_ha': (0, 50)
                    }
                }
            elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                self.PotassioDict = {
                    'muito_baixo': {
                        'faixa': general_dict_potassio['faixa_3']['muito_baixo'],
                        'kg_p_ha': (100, 130)
                    },
                    'baixo': {
                        'faixa': general_dict_potassio['faixa_3']['baixo'],
                        'kg_p_ha': (75, 100)
                    },
                    'medio': {
                        'faixa': general_dict_potassio['faixa_3']['medio'],
                        'kg_p_ha': (70, 75)
                    },
                    'alto': {
                        'faixa': general_dict_potassio['faixa_3']['alto'],
                        'kg_p_ha': (50, 70)
                    },
                    'muito_alto': {
                        'faixa': general_dict_potassio['faixa_3']['muito_alto'],
                        'kg_p_ha': (0, 50)
                    }
                }
            elif float(self.entrada.TeorArgila) <= 20:
                self.PotassioDict = {
                    'muito_baixo': {
                        'faixa': general_dict_potassio['faixa_4']['muito_baixo'],
                        'kg_p_ha': (100, 130)
                    },
                    'baixo': {
                        'faixa': general_dict_potassio['faixa_4']['baixo'],
                        'kg_p_ha': (75, 100)
                    },
                    'medio': {
                        'faixa': general_dict_potassio['faixa_4']['medio'],
                        'kg_p_ha': (70, 75)
                    },
                    'alto': {
                        'faixa': general_dict_potassio['faixa_4']['alto'],
                        'kg_p_ha': (50, 70)
                    },
                    'muito_alto': {
                        'faixa': general_dict_potassio['faixa_4']['muito_alto'],
                        'kg_p_ha': (0, 50)
                    }
                }

        if self.entrada.Cultura == 'Campo natural misturado':
            if float(self.entrada.TeorArgila) >= 60:
                self.PotassioDict = {
                    'muito_baixo': {
                        'faixa': general_dict_potassio['faixa_1']['muito_baixo'],
                        'kg_p_ha': (130, 160)
                    },
                    'baixo': {
                        'faixa': general_dict_potassio['faixa_1']['baixo'],
                        'kg_p_ha': (90, 130)
                    },
                    'medio': {
                        'faixa': general_dict_potassio['faixa_1']['medio'],
                        'kg_p_ha': (80, 90)
                    },
                    'alto': {
                        'faixa': general_dict_potassio['faixa_1']['alto'],
                        'kg_p_ha': (50, 80)
                    },
                    'muito_alto': {
                        'faixa': general_dict_potassio['faixa_1']['muito_alto'],
                        'kg_p_ha': (0, 50)
                    }
                }
            elif float(self.entrada.TeorArgila) > 40 and float(self.entrada.TeorArgila) < 60:
                self.PotassioDict = {
                    'muito_baixo': {
                        'faixa': general_dict_potassio['faixa_2']['muito_baixo'],
                        'kg_p_ha': (130, 160)
                    },
                    'baixo': {
                        'faixa': general_dict_potassio['faixa_2']['baixo'],
                        'kg_p_ha': (90, 130)
                    },
                    'medio': {
                        'faixa': general_dict_potassio['faixa_2']['medio'],
                        'kg_p_ha': (80, 90)
                    },
                    'alto': {
                        'faixa': general_dict_potassio['faixa_2']['alto'],
                        'kg_p_ha': (50, 80)
                    },
                    'muito_alto': {
                        'faixa': general_dict_potassio['faixa_2']['muito_alto'],
                        'kg_p_ha': (0, 50)
                    }
                }
            elif float(self.entrada.TeorArgila) > 20 and float(self.entrada.TeorArgila) <= 40:
                self.PotassioDict = {
                    'muito_baixo': {
                        'faixa': general_dict_potassio['faixa_3']['muito_baixo'],
                        'kg_p_ha': (130, 160)
                    },
                    'baixo': {
                        'faixa': general_dict_potassio['faixa_3']['baixo'],
                        'kg_p_ha': (90, 130)
                    },
                    'medio': {
                        'faixa': general_dict_potassio['faixa_3']['medio'],
                        'kg_p_ha': (80, 90)
                    },
                    'alto': {
                        'faixa': general_dict_potassio['faixa_3']['alto'],
                        'kg_p_ha': (50, 80)
                    },
                    'muito_alto': {
                        'faixa': general_dict_potassio['faixa_3']['muito_alto'],
                        'kg_p_ha': (0, 50)
                    }
                }
            elif float(self.entrada.TeorArgila) <= 20:
                self.PotassioDict = {
                    'muito_baixo': {
                        'faixa': general_dict_potassio['faixa_4']['muito_baixo'],
                        'kg_p_ha': (130, 160)
                    },
                    'baixo': {
                        'faixa': general_dict_potassio['faixa_4']['baixo'],
                        'kg_p_ha': (90, 130)
                    },
                    'medio': {
                        'faixa': general_dict_potassio['faixa_4']['medio'],
                        'kg_p_ha': (80, 90)
                    },
                    'alto': {
                        'faixa': general_dict_potassio['faixa_4']['alto'],
                        'kg_p_ha': (50, 80)
                    },
                    'muito_alto': {
                        'faixa': general_dict_potassio['faixa_4']['muito_alto'],
                        'kg_p_ha': (0, 50)
                    }
                }

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def __str__(self) -> str:
        return super().__str__()