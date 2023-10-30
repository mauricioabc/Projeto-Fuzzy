import unittest
from Entities.InitialInformation import InitialInformation
from Infraestructure.APIManager import APIManager


class FuzzyTest(unittest.TestCase):
    def test_adubacao(self):
        entrada = InitialInformation('Forrageira', 'Campo natural', 'Convencional',
                                     n='88', p='88', k='88', Inoculacao='70',
                                     Estacao='Quente', MateriaOrganica='5.1')
        apiManager = APIManager()
        apiManager.processa_adubacao(entrada)

    def test_formato(self):
        dict_nitrogenio = {
            'muito_baixo': {
                'faixa': (0, 1.6),
                'kg_n_ha': (200, 220)
            },
            'baixo': {
                'faixa': (1.6, 2.5),
                'kg_n_ha': (180, 200)
            },
            'medio': {
                'faixa': (2.6, 3.5),
                'kg_n_ha': (160, 180)
            },
            'alto': {
                'faixa': (3.6, 4.5),
                'kg_n_ha': (140, 160)
            },
            'muito_alto': {
                'faixa': (4.5, 100),
                'kg_n_ha': (120, 140)
            }
        }
        print('a')


if __name__ == '__main__':
    unittest.main()