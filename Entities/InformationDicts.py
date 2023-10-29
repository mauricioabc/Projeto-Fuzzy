from typing import Any


class InformationDicts:

    def __init__(self, entrada):
        self.entrada = entrada
        self.NitrogenioDict = None
        self.FosforoDict = None
        self.processa_nitrogenio()
        self.processa_fosforo()

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
                'muito_baixo': (0, 1.5),
                'baixo': (1.5, 3.0),
                'medio': (3.1, 4.5),
                'alto': (4.6, 9.0),
                'muito_alto': (9.0, 12)
            },
            'faixa_2': {
                'muito_baixo': (0, 2),
                'baixo': (2.1, 4.0),
                'medio': (4.1, 6.0),
                'alto': (6.1, 12.0),
                'muito_alto': (12.0, 15)
            },
            'faixa_3': {
                'muito_baixo': (0, 3),
                'baixo': (3.1, 6.0),
                'medio': (6.1, 9.0),
                'alto': (9.1, 18.0),
                'muito_alto': (18.0, 21)
            },
            'faixa_4': {
                'muito_baixo': (0, 5),
                'baixo': (5.1, 10.0),
                'medio': (10.1, 15),
                'alto': (15.1, 30.0),
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

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def __str__(self) -> str:
        return super().__str__()