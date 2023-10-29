import unittest
from Entities.InitialInformation import InitialInformation
from Infraestructure.APIManager import APIManager


class FuzzyTest(unittest.TestCase):
    def test_adubacao(self):
        entrada = InitialInformation('Forrageira', 'Gramíneas', 'Convencional',
                                     n='88', p='88', k='88', Inoculacao='70',
                                     Estacao='Fria', MateriaOrganica='5.1')
        apiManager = APIManager()
        apiManager.processa_adubacao(entrada)


if __name__ == '__main__':
    unittest.main()