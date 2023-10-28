from Entities.InitialInformation import InitialInformation


class APIValidator:

    def __init__(self):
        self.culturaAtendidas = ['Alfafa', 'Espécies perenes',
                                 'Gramíneas', 'Leguminosas',
                                 'Consórcios', 'Campo natural']

    def valida_chamada_calagem(self, chamada):
        try:
            especie = chamada.get('Especie')
            cultura = chamada.get('Cultura')
            tipoPlantio = chamada.get('TipoPlantio')
            phSolo = chamada.get('phSolo')
            indiceSMP = chamada.get('IndiceSMP')
            bases = chamada.get('Bases')
            alSat = chamada.get('AlSat')
            ca = chamada.get('Ca')
            mg = chamada.get('Mg')
            ctc = chamada.get('CTC')

            # Verifica a espécie
            if especie is None:
                return 'O JSON deve conter a chave "Especie".', 'ERRO'
            elif especie != "Forrageira":
                return ('A API atende apenas ao tipo de espécie "Forrageira", '
                        'para mais informações contate o nosso suporte.', 'ERRO')

            # Verifica a cultura
            elif cultura is None:
                return 'O JSON deve conter a chave "Cultura".', 'ERRO'
            elif cultura not in self.culturaAtendidas:
                return ('A API atende apenas aos tipos de cultura: Alfafa, '
                        'Espécies perenes, Gramíneas, Leguminosas, '
                        'Consórcios e Campo natural; '
                        'para mais informações contate o nosso suporte.', 'ERRO')
            elif cultura == 'Gramíneas' or cultura == 'Leguminosas' or cultura == 'Consórcios':
                if tipoPlantio is None:
                    return 'O JSON deve conter a chave "Bases".', 'ERRO'
            elif cultura == 'Campo natural':
                if bases is None:
                    return 'O JSON deve conter a chave "Bases".', 'ERRO'

            # Verifica demais tags
            elif phSolo is None:
                return 'O JSON deve conter a chave "phSolo".', 'ERRO'
            elif indiceSMP is None:
                return 'O JSON deve conter a chave "IndiceSMP".', 'ERRO'
            elif alSat is None:
                return 'O JSON deve conter a chave "AlSat".', 'ERRO'
            elif ca is None:
                return 'O JSON deve conter a chave "Ca".', 'ERRO'
            elif mg is None:
                return 'O JSON deve conter a chave "Mg".', 'ERRO'
            elif ctc is None:
                return 'O JSON deve conter a chave "CTC".', 'ERRO'

            entrada = InitialInformation(especie, cultura, tipoPlantio, phSolo, indiceSMP, bases, ca, mg, alSat, ctc)

            return entrada, 'OK'
        except Exception as e:
            print(f'Erro: {str(e)}')
            print('Traceback:')
            import traceback
            traceback.print_exc()

    def valida_chamada_adubacao(self, chamada):
        try:
            especie = chamada.get('Especie')
            cultura = chamada.get('Cultura')
            tipoPlantio = chamada.get('TipoPlantio')
            p = chamada.get('Nível de Fósforo (P)')
            k = chamada.get('Nível de Potássio (K)')
            inoculacao = chamada.get('Eficiência de Inoculação')

            # Verifica a espécie
            if especie is None:
                return 'O JSON deve conter a chave "Especie".', 'ERRO'
            elif especie != "Forrageira":
                return ('A API atende apenas ao tipo de espécie "Forrageira", '
                        'para mais informações contate o nosso suporte.', 'ERRO')

            # Verifica a cultura
            elif cultura is None:
                return 'O JSON deve conter a chave "Cultura".', 'ERRO'
            elif cultura not in self.culturaAtendidas:
                return ('A API atende apenas aos tipos de cultura: Alfafa, '
                        'Espécies perenes, Gramíneas, Leguminosas, '
                        'Consórcios e Campo natural; '
                        'para mais informações contate o nosso suporte.', 'ERRO')
            elif cultura == 'Gramíneas' or cultura == 'Leguminosas' or cultura == 'Consórcios':
                if tipoPlantio is None:
                    return 'O JSON deve conter a chave "Bases".', 'ERRO'
            

            # Verifica demais tags
            elif p is None:
                return 'O JSON deve conter a chave "Fósforo".', 'ERRO'
            elif k is None:
                return 'O JSON deve conter a chave "Potássio".', 'ERRO'
            elif inoculacao is None:
                return 'O JSON deve conter a chave "Eficiência de Inoculação".', 'ERRO'

            entrada = InitialInformation(especie, cultura, tipoPlantio, p=p, k=k, inoculacao=inoculacao)

            return entrada, 'OK'
        except Exception as e:
            print(f'Erro: {str(e)}')
            print('Traceback:')
            import traceback
            traceback.print_exc()
