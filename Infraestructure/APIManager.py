from Infraestructure.CalcCalculator import CalcCalculator
from Entities.InformationDicts import InformationDicts
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class APIManager:
    def __init__(self):
        self.entrada = None
        self.InformationDicts = None

    def processa_nitrogenio(self):
        # Crie os objetos 'teor_materia_organica' e 'quantidade_nitrogenio' como variáveis Antecedent e Consequente
        teor_materia_organica = ctrl.Antecedent(np.arange(self.InformationDicts.NitrogenioDict['muito_baixo']['faixa'][0], self.InformationDicts.NitrogenioDict['muito_alto']['faixa'][1], 0.1), 'Teor de Matéria Orgânica no Solo')
        quantidade_nitrogenio = ctrl.Consequent(np.arange(self.InformationDicts.NitrogenioDict['muito_alto']['kg_n_ha'][0], self.InformationDicts.NitrogenioDict['muito_baixo']['kg_n_ha'][1], 1), 'Quantidade de Nitrogênio')

        # Crie os conjuntos de pertinência para o Teor de Matéria Orgânica no Solo
        teor_materia_organica['muito_baixo'] = fuzz.trimf(teor_materia_organica.universe,[0,self.InformationDicts.NitrogenioDict['muito_baixo']['faixa'][0], self.InformationDicts.NitrogenioDict['muito_baixo']['faixa'][1]])
        teor_materia_organica['baixo'] = fuzz.trimf(teor_materia_organica.universe, [self.InformationDicts.NitrogenioDict['baixo']['faixa'][0], int(np.mean([self.InformationDicts.NitrogenioDict['baixo']['faixa'][0], self.InformationDicts.NitrogenioDict['baixo']['faixa'][1]])),self.InformationDicts.NitrogenioDict['baixo']['faixa'][1]])
        teor_materia_organica['medio'] = fuzz.trimf(teor_materia_organica.universe, [self.InformationDicts.NitrogenioDict['medio']['faixa'][0], int(np.mean([self.InformationDicts.NitrogenioDict['medio']['faixa'][0], self.InformationDicts.NitrogenioDict['medio']['faixa'][1]])),self.InformationDicts.NitrogenioDict['medio']['faixa'][1]])
        teor_materia_organica['alto'] = fuzz.trimf(teor_materia_organica.universe, [self.InformationDicts.NitrogenioDict['alto']['faixa'][0], int(np.mean([self.InformationDicts.NitrogenioDict['alto']['faixa'][0], self.InformationDicts.NitrogenioDict['alto']['faixa'][1]])),self.InformationDicts.NitrogenioDict['alto']['faixa'][1]])
        teor_materia_organica['muito_alto'] = fuzz.smf(teor_materia_organica.universe, self.InformationDicts.NitrogenioDict['muito_alto']['faixa'][0], self.InformationDicts.NitrogenioDict['muito_alto']['faixa'][1])

        # Crie os conjuntos de pertinência para a Quantidade de Nitrogênio
        quantidade_nitrogenio['muito_baixo'] = fuzz.trimf(quantidade_nitrogenio.universe, [self.InformationDicts.NitrogenioDict['muito_baixo']['kg_n_ha'][0], int(np.mean([self.InformationDicts.NitrogenioDict['muito_baixo']['kg_n_ha'][0], self.InformationDicts.NitrogenioDict['muito_baixo']['kg_n_ha'][1]])),self.InformationDicts.NitrogenioDict['muito_baixo']['kg_n_ha'][1]])
        quantidade_nitrogenio['baixo'] = fuzz.trimf(quantidade_nitrogenio.universe, [self.InformationDicts.NitrogenioDict['baixo']['kg_n_ha'][0], int(np.mean([self.InformationDicts.NitrogenioDict['baixo']['kg_n_ha'][0], self.InformationDicts.NitrogenioDict['baixo']['kg_n_ha'][1]])),self.InformationDicts.NitrogenioDict['baixo']['kg_n_ha'][1]])
        quantidade_nitrogenio['medio'] = fuzz.trimf(quantidade_nitrogenio.universe, [self.InformationDicts.NitrogenioDict['medio']['kg_n_ha'][0], int(np.mean([self.InformationDicts.NitrogenioDict['medio']['kg_n_ha'][0], self.InformationDicts.NitrogenioDict['medio']['kg_n_ha'][1]])),self.InformationDicts.NitrogenioDict['medio']['kg_n_ha'][1]])
        quantidade_nitrogenio['alto'] = fuzz.trimf(quantidade_nitrogenio.universe, [self.InformationDicts.NitrogenioDict['alto']['kg_n_ha'][0], int(np.mean([self.InformationDicts.NitrogenioDict['alto']['kg_n_ha'][0], self.InformationDicts.NitrogenioDict['alto']['kg_n_ha'][1]])),self.InformationDicts.NitrogenioDict['alto']['kg_n_ha'][1]])
        quantidade_nitrogenio['muito_alto'] = fuzz.trimf(quantidade_nitrogenio.universe, [self.InformationDicts.NitrogenioDict['muito_alto']['kg_n_ha'][0], int(np.mean([self.InformationDicts.NitrogenioDict['muito_alto']['kg_n_ha'][0], self.InformationDicts.NitrogenioDict['muito_alto']['kg_n_ha'][1]])),self.InformationDicts.NitrogenioDict['muito_alto']['kg_n_ha'][1]])

        # Crie regras Fuzzy para o Nitrogênio
        regra1_nitrogenio = ctrl.Rule(teor_materia_organica['muito_baixo'], quantidade_nitrogenio['muito_baixo'])
        regra2_nitrogenio = ctrl.Rule(teor_materia_organica['baixo'], quantidade_nitrogenio['baixo'])
        regra3_nitrogenio = ctrl.Rule(teor_materia_organica['medio'], quantidade_nitrogenio['medio'])
        regra4_nitrogenio = ctrl.Rule(teor_materia_organica['alto'], quantidade_nitrogenio['alto'])
        regra5_nitrogenio = ctrl.Rule(teor_materia_organica['muito_alto'], quantidade_nitrogenio['muito_alto'])

        # Executa Cálculo
        sistema_controle_nitrogenio = ctrl.ControlSystem([regra1_nitrogenio, regra2_nitrogenio, regra3_nitrogenio, regra4_nitrogenio, regra5_nitrogenio])
        sistema_nitrogenio = ctrl.ControlSystemSimulation(sistema_controle_nitrogenio)
        sistema_nitrogenio.input['Teor de Matéria Orgânica no Solo'] = float(self.entrada.MateriaOrganica)
        sistema_nitrogenio.compute()
        return round(float(sistema_nitrogenio.output['Quantidade de Nitrogênio']), 2)

    def processa_fosforo(self):
        # Crie os objetos 'teor_fosforo' e 'quantidade_fosforo' como variáveis Antecedent e Consequente
        teor_fosforo = ctrl.Antecedent(np.arange(self.InformationDicts.FosforoDict['muito_baixo']['faixa'][0], self.InformationDicts.FosforoDict['muito_alto']['faixa'][1], 0.1), 'Teor de Fosfóro')
        quantidade_fosforo = ctrl.Consequent(np.arange(self.InformationDicts.FosforoDict['muito_alto']['kg_p_ha'][0], self.InformationDicts.FosforoDict['muito_baixo']['kg_p_ha'][1], 1), 'Quantidade de Fosfóro')

        # Crie os conjuntos de pertinência para o Teor de Matéria Orgânica no Solo
        teor_fosforo['muito_baixo'] = fuzz.trimf(teor_fosforo.universe,[0,self.InformationDicts.FosforoDict['muito_baixo']['faixa'][0], self.InformationDicts.FosforoDict['muito_baixo']['faixa'][1]])
        teor_fosforo['baixo'] = fuzz.trimf(teor_fosforo.universe, [self.InformationDicts.FosforoDict['baixo']['faixa'][0], int(np.mean([self.InformationDicts.FosforoDict['baixo']['faixa'][0], self.InformationDicts.FosforoDict['baixo']['faixa'][1]])),self.InformationDicts.FosforoDict['baixo']['faixa'][1]])
        teor_fosforo['medio'] = fuzz.trimf(teor_fosforo.universe, [self.InformationDicts.FosforoDict['medio']['faixa'][0], int(np.mean([self.InformationDicts.FosforoDict['medio']['faixa'][0], self.InformationDicts.FosforoDict['medio']['faixa'][1]])),self.InformationDicts.FosforoDict['medio']['faixa'][1]])
        teor_fosforo['alto'] = fuzz.trimf(teor_fosforo.universe, [self.InformationDicts.FosforoDict['alto']['faixa'][0], int(np.mean([self.InformationDicts.FosforoDict['alto']['faixa'][0], self.InformationDicts.FosforoDict['alto']['faixa'][1]])),self.InformationDicts.FosforoDict['alto']['faixa'][1]])
        teor_fosforo['muito_alto'] = fuzz.smf(teor_fosforo.universe, self.InformationDicts.FosforoDict['muito_alto']['faixa'][0], self.InformationDicts.FosforoDict['muito_alto']['faixa'][1])

        # Crie os conjuntos de pertinência para a Quantidade de Nitrogênio
        quantidade_fosforo['muito_baixo'] = fuzz.trimf(quantidade_fosforo.universe, [self.InformationDicts.FosforoDict['muito_baixo']['kg_p_ha'][0], int(np.mean([self.InformationDicts.FosforoDict['muito_baixo']['kg_p_ha'][0], self.InformationDicts.FosforoDict['muito_baixo']['kg_p_ha'][1]])),self.InformationDicts.FosforoDict['muito_baixo']['kg_p_ha'][1]])
        quantidade_fosforo['baixo'] = fuzz.trimf(quantidade_fosforo.universe, [self.InformationDicts.FosforoDict['baixo']['kg_p_ha'][0], int(np.mean([self.InformationDicts.FosforoDict['baixo']['kg_p_ha'][0], self.InformationDicts.FosforoDict['baixo']['kg_p_ha'][1]])),self.InformationDicts.FosforoDict['baixo']['kg_p_ha'][1]])
        quantidade_fosforo['medio'] = fuzz.trimf(quantidade_fosforo.universe, [self.InformationDicts.FosforoDict['medio']['kg_p_ha'][0], int(np.mean([self.InformationDicts.FosforoDict['medio']['kg_p_ha'][0], self.InformationDicts.FosforoDict['medio']['kg_p_ha'][1]])),self.InformationDicts.FosforoDict['medio']['kg_p_ha'][1]])
        quantidade_fosforo['alto'] = fuzz.trimf(quantidade_fosforo.universe, [self.InformationDicts.FosforoDict['alto']['kg_p_ha'][0], int(np.mean([self.InformationDicts.FosforoDict['alto']['kg_p_ha'][0], self.InformationDicts.FosforoDict['alto']['kg_p_ha'][1]])),self.InformationDicts.FosforoDict['alto']['kg_p_ha'][1]])
        quantidade_fosforo['muito_alto'] = fuzz.trimf(quantidade_fosforo.universe, [self.InformationDicts.FosforoDict['muito_alto']['kg_p_ha'][0], int(np.mean([self.InformationDicts.FosforoDict['muito_alto']['kg_p_ha'][0], self.InformationDicts.FosforoDict['muito_alto']['kg_p_ha'][1]])),self.InformationDicts.FosforoDict['muito_alto']['kg_p_ha'][1]])

        # Crie regras Fuzzy para o Nitrogênio
        regra1_fosforo = ctrl.Rule(teor_fosforo['muito_baixo'], quantidade_fosforo['muito_baixo'])
        regra2_fosforo = ctrl.Rule(teor_fosforo['baixo'], quantidade_fosforo['baixo'])
        regra3_fosforo = ctrl.Rule(teor_fosforo['medio'], quantidade_fosforo['medio'])
        regra4_fosforo = ctrl.Rule(teor_fosforo['alto'], quantidade_fosforo['alto'])
        regra5_fosforo = ctrl.Rule(teor_fosforo['muito_alto'], quantidade_fosforo['muito_alto'])

        sistema_controle_fosforo = ctrl.ControlSystem([regra1_fosforo, regra2_fosforo, regra3_fosforo, regra4_fosforo, regra5_fosforo])
        sistema_fosforo = ctrl.ControlSystemSimulation(sistema_controle_fosforo)
        sistema_fosforo.input['Teor de Fosfóro'] = float(self.entrada.p)
        sistema_fosforo.compute()
        return round(float(sistema_fosforo.output['Quantidade de Fosfóro']), 2)

    def processa_potassio(self):
        # Crie os objetos 'teor_potassio' e 'quantidade_potassio' como variáveis Antecedent e Consequente
        teor_potassio = ctrl.Antecedent(np.arange(self.InformationDicts.PotassioDict['muito_baixo']['faixa'][0], self.InformationDicts.PotassioDict['muito_alto']['faixa'][1], 0.1), 'Teor de Potássio')
        quantidade_potassio = ctrl.Consequent(np.arange(self.InformationDicts.PotassioDict['muito_alto']['kg_p_ha'][0], self.InformationDicts.PotassioDict['muito_baixo']['kg_p_ha'][1], 1), 'Quantidade de Potássio')

        # Crie os conjuntos de pertinência para o Teor de Matéria Orgânica no Solo
        teor_potassio['muito_baixo'] = fuzz.trimf(teor_potassio.universe,[0,self.InformationDicts.PotassioDict['muito_baixo']['faixa'][0], self.InformationDicts.PotassioDict['muito_baixo']['faixa'][1]])
        teor_potassio['baixo'] = fuzz.trimf(teor_potassio.universe, [self.InformationDicts.PotassioDict['baixo']['faixa'][0], int(np.mean([self.InformationDicts.PotassioDict['baixo']['faixa'][0], self.InformationDicts.PotassioDict['baixo']['faixa'][1]])),self.InformationDicts.PotassioDict['baixo']['faixa'][1]])
        teor_potassio['medio'] = fuzz.trimf(teor_potassio.universe, [self.InformationDicts.PotassioDict['medio']['faixa'][0], int(np.mean([self.InformationDicts.PotassioDict['medio']['faixa'][0], self.InformationDicts.PotassioDict['medio']['faixa'][1]])),self.InformationDicts.PotassioDict['medio']['faixa'][1]])
        teor_potassio['alto'] = fuzz.trimf(teor_potassio.universe, [self.InformationDicts.PotassioDict['alto']['faixa'][0], int(np.mean([self.InformationDicts.PotassioDict['alto']['faixa'][0], self.InformationDicts.PotassioDict['alto']['faixa'][1]])),self.InformationDicts.PotassioDict['alto']['faixa'][1]])
        teor_potassio['muito_alto'] = fuzz.smf(teor_potassio.universe, self.InformationDicts.PotassioDict['muito_alto']['faixa'][0], self.InformationDicts.PotassioDict['muito_alto']['faixa'][1])

        # Crie os conjuntos de pertinência para a Quantidade de Nitrogênio
        quantidade_potassio['muito_baixo'] = fuzz.trimf(quantidade_potassio.universe, [self.InformationDicts.PotassioDict['muito_baixo']['kg_p_ha'][0], int(np.mean([self.InformationDicts.PotassioDict['muito_baixo']['kg_p_ha'][0], self.InformationDicts.PotassioDict['muito_baixo']['kg_p_ha'][1]])),self.InformationDicts.PotassioDict['muito_baixo']['kg_p_ha'][1]])
        quantidade_potassio['baixo'] = fuzz.trimf(quantidade_potassio.universe, [self.InformationDicts.PotassioDict['baixo']['kg_p_ha'][0], int(np.mean([self.InformationDicts.PotassioDict['baixo']['kg_p_ha'][0], self.InformationDicts.PotassioDict['baixo']['kg_p_ha'][1]])),self.InformationDicts.PotassioDict['baixo']['kg_p_ha'][1]])
        quantidade_potassio['medio'] = fuzz.trimf(quantidade_potassio.universe, [self.InformationDicts.PotassioDict['medio']['kg_p_ha'][0], int(np.mean([self.InformationDicts.PotassioDict['medio']['kg_p_ha'][0], self.InformationDicts.PotassioDict['medio']['kg_p_ha'][1]])),self.InformationDicts.PotassioDict['medio']['kg_p_ha'][1]])
        quantidade_potassio['alto'] = fuzz.trimf(quantidade_potassio.universe, [self.InformationDicts.PotassioDict['alto']['kg_p_ha'][0], int(np.mean([self.InformationDicts.PotassioDict['alto']['kg_p_ha'][0], self.InformationDicts.PotassioDict['alto']['kg_p_ha'][1]])),self.InformationDicts.PotassioDict['alto']['kg_p_ha'][1]])
        quantidade_potassio['muito_alto'] = fuzz.trimf(quantidade_potassio.universe, [self.InformationDicts.PotassioDict['muito_alto']['kg_p_ha'][0], int(np.mean([self.InformationDicts.PotassioDict['muito_alto']['kg_p_ha'][0], self.InformationDicts.PotassioDict['muito_alto']['kg_p_ha'][1]])),self.InformationDicts.PotassioDict['muito_alto']['kg_p_ha'][1]])

        # Crie regras Fuzzy para o Nitrogênio
        regra1_potassio = ctrl.Rule(teor_potassio['muito_baixo'], quantidade_potassio['muito_baixo'])
        regra2_potassio = ctrl.Rule(teor_potassio['baixo'], quantidade_potassio['baixo'])
        regra3_potassio = ctrl.Rule(teor_potassio['medio'], quantidade_potassio['medio'])
        regra4_potassio = ctrl.Rule(teor_potassio['alto'], quantidade_potassio['alto'])
        regra5_potassio = ctrl.Rule(teor_potassio['muito_alto'], quantidade_potassio['muito_alto'])

        sistema_controle_potassio = ctrl.ControlSystem([regra1_potassio, regra2_potassio, regra3_potassio, regra4_potassio, regra5_potassio])
        sistema_potassio = ctrl.ControlSystemSimulation(sistema_controle_potassio)
        sistema_potassio.input['Teor de Potássio'] = float(self.entrada.CTC)
        sistema_potassio.compute()
        return round(float(sistema_potassio.output['Quantidade de Potássio']), 2)

    def processa_adubacao(self, entrada):
        # Cria dados que serão utilizados nos cálculos e retornos
        self.entrada = entrada
        self.InformationDicts = InformationDicts(entrada)
        mensagem_N = ""
        mensagem_P = ""
        mensagem_K = ""

        # Processa Alfafa
        if entrada.Cultura == 'Alfafa':
            # Processa o N
            if entrada.Inoculacao == 'true':
                mensagem_N = 'A adubação nitrogenada não é necessária.'
            else :
                mensagem_N = 'Aplicar de 20 a 40 kg de N/ha após cada corte, dependendo do desenvolvimento da cultura.'
            # Processa o P
            mensagem_P = f"É preciso aplicar {self.processa_fosforo()}kg/ha."
            mensagem_K = f"É preciso aplicar {self.processa_potassio()}kg/ha."

        # Processa Gramíneas
        if entrada.Cultura == 'Gramíneas':
            mensagem_N = f"É preciso aplicar {self.processa_nitrogenio()}kg/ha."
            mensagem_P = f"É preciso aplicar {self.processa_fosforo()}kg/ha."
            mensagem_K = f"É preciso aplicar {self.processa_potassio()}kg/ha."

        # Processa Leguminosas
        if entrada.Cultura == 'Leguminosas':
            # Processa o N
            if entrada.Inoculacao == 'true':
                mensagem_N = 'A adubação nitrogenada não é necessária.'
            else :
                mensagem_N = 'Aplicar nitrogênio na dose de 20 kg de N/ha, após cada duas utilizações da pastagem.'
            mensagem_P = f"É preciso aplicar {self.processa_fosforo()}kg/ha."
            mensagem_K = f"É preciso aplicar {self.processa_potassio()}kg/ha."

        # Processa Consórcios
        if entrada.Cultura == 'Consórcios':
            # Processa o N
            if entrada.Inoculacao == 'true':
                mensagem_N = 'A adubação nitrogenada não é necessária.'
            else:
                mensagem_N = 'Aaplicar 20 kg de N/ha por ocasião do perfilhamento da gramínea e 20 kg de N/ha após cada duas utilizações da pastagem'
            mensagem_P = f"É preciso aplicar {self.processa_fosforo()}kg/ha."
            mensagem_K = f"É preciso aplicar {self.processa_potassio()}kg/ha."

        # Processa Milho e Sorgo
        if entrada.Cultura == 'Milho':
            mensagem_N = f"É preciso aplicar {self.processa_nitrogenio()}kg/ha."
            mensagem_P = f"É preciso aplicar {self.processa_fosforo()}kg/ha."
            mensagem_K = f"É preciso aplicar {self.processa_potassio()}kg/ha."

        # Processa Pastagens Naturais
        if entrada.Cultura == 'Campo natural':
            mensagem_N = f"É preciso aplicar {self.processa_nitrogenio()}kg/ha."
            mensagem_P = f"É preciso aplicar {self.processa_fosforo()}kg/ha."
            mensagem_K = f"É preciso aplicar {self.processa_potassio()}kg/ha."

        # Processa Pastagens Misturadas
        if entrada.Cultura == 'Campo natural misturado':
            mensagem_N = f"É preciso aplicar {self.processa_nitrogenio()}kg/ha."
            mensagem_P = f"É preciso aplicar {self.processa_fosforo()}kg/ha."
            mensagem_K = f"É preciso aplicar {self.processa_potassio()}kg/ha."

        return mensagem_N, mensagem_P, mensagem_K



    def processa_calagem(self, entrada):
        phSolo = float(entrada.phSolo)
        bases = float(entrada.Bases)
        ctc = float(entrada.CTC)
        alSat = float(entrada.AlSat)
        calculadora = CalcCalculator()

        if entrada.Cultura == 'Alfafa':
            if phSolo < 6.0:
                return calculadora.processa_SMP(entrada.IndiceSMP, 6.5), 'incorporada'
        elif (entrada.Cultura == 'Espécies perenes' or entrada.Cultura == 'Gramíneas' or
              entrada.Cultura == 'Leguminosas' or entrada.Cultura == 'Consórcios'):
            if entrada.TipoPlantio == 'Consolidado':
                if bases >= 65.0 and alSat < 10.0:
                    return -1, -1
                if phSolo < 5.5:
                    if calculadora.processa_SMP(entrada.IndiceSMP, 6.0) > 5:
                        return 5.0, 'superficial'
            if phSolo < 5.5:
                return calculadora.processa_SMP(entrada.IndiceSMP, 6.0), 'incorporada'
        elif entrada.Cultura == 'Campo natural':
            if float(entrada.Ca) >= 4.0 and float(entrada.Mg) >= 1.0:
                return -1, -1
            if bases <= 40.0:
                nc = (40 - bases) / 100 * ctc
                if nc > 5:
                    return 5.0, 'superficial'
                return round(float(nc), 2), 'superficial'

        return -1, -1
