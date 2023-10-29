from Infraestructure.CalcCalculator import CalcCalculator
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class APIManager:

    def define_funcao_pertinencia(self, entrada, nivel_n, nivel_k, nivel_p, eficiencia_inoculacao, quantidade_nitrogenio, quantidade_fosforo, quantidade_potassio, teor_materia_organica=None):
        if entrada.Cultura == 'Alfafa':
            # Cria os conjuntos de pertinência para o Fósforo
            nivel_p['muito_baixo'] = fuzz.trimf(nivel_p.universe, [170, 170, 195])
            nivel_p['baixo'] = fuzz.trimf(nivel_p.universe, [135, 150, 150])
            nivel_p['medio'] = fuzz.trimf(nivel_p.universe, [120, 120, 125])
            nivel_p['alto'] = fuzz.trimf(nivel_p.universe, [85, 120, 120])

            # Cria os conjuntos de pertinência para a Quantidade de Fósforo
            quantidade_fosforo['muito_baixo'] = fuzz.trimf(quantidade_fosforo.universe, [0, 0, 20])
            quantidade_fosforo['baixo'] = fuzz.trimf(quantidade_fosforo.universe, [10, 20, 30])
            quantidade_fosforo['medio'] = fuzz.trimf(quantidade_fosforo.universe, [25, 35, 45])
            quantidade_fosforo['alto'] = fuzz.trimf(quantidade_fosforo.universe, [40, 50, 60])

            # Cria os conjuntos de pertinência para a Quantidade de Potássio
            quantidade_potassio['muito_baixo'] = fuzz.trimf(quantidade_potassio.universe, [0, 0, 50])
            quantidade_potassio['baixo'] = fuzz.trimf(quantidade_potassio.universe, [0, 50, 100])
            quantidade_potassio['medio'] = fuzz.trimf(quantidade_potassio.universe, [50, 100, 100])
            quantidade_potassio['alto'] = fuzz.trimf(quantidade_potassio.universe, [50, 100, 100])

            # Cria os conjuntos de pertinência para o Nível de Potássio (K)
            nivel_k['muito_baixo'] = fuzz.trimf(nivel_k.universe, [0, 0, 50])
            nivel_k['baixo'] = fuzz.trimf(nivel_k.universe, [0, 50, 100])
            nivel_k['medio'] = fuzz.trimf(nivel_k.universe, [50, 100, 150])
            nivel_k['alto'] = fuzz.trimf(nivel_k.universe, [100, 150, 200])

        elif entrada.Cultura == 'Espécies perenes':
            # Defina as funções de pertinência para as variáveis de entrada (níveis de fósforo, potássio e eficiência de inoculação)
            nivel_p['muito_baixo'] = fuzz.smf(nivel_p.universe, 215,225)
            nivel_p['baixo'] = fuzz.trapmf(nivel_p.universe, [155, 180, 195, 219])
            nivel_p['medio'] = fuzz.trapmf(nivel_p.universe, [145, 150, 155, 159])
            nivel_p['alto'] = fuzz.trapmf(nivel_p.universe, [110, 120, 130, 149])
            nivel_p['muito_alto'] = fuzz.zmf(nivel_p.universe,105, 110)

            nivel_k['muito_baixo'] = fuzz.smf(nivel_p.universe, 295,300)
            nivel_k['baixo'] = fuzz.trapmf(nivel_p.universe, [255, 265, 280, 299])
            nivel_k['medio'] = fuzz.trapmf(nivel_p.universe, [245, 250, 254, 259])
            nivel_k['alto'] = fuzz.trapmf(nivel_p.universe, [220, 230, 240, 249])
            nivel_k['muito_alto'] = fuzz.zmf(nivel_p.universe, 215, 220)

            eficiencia_inoculacao['ineficiente'] = fuzz.trimf(eficiencia_inoculacao.universe, [0, 0, 50])
            eficiencia_inoculacao['eficiente'] = fuzz.trimf(eficiencia_inoculacao.universe, [40, 70, 100])

            # Defina as funções de pertinência para as variáveis de saída (quantidade de NPK e quantidade de nitrogênio)
            quantidade_nitrogenio['nitrogenio'] = fuzz.trimf(quantidade_nitrogenio.universe, [0, 0, 80])
            
        elif entrada.Cultura == 'Gramíneas':
            if entrada.Estacao == 'Fria':
                # Crie os conjuntos de pertinência para o Teor de Matéria Orgânica no Solo
                teor_materia_organica['muito_baixo'] = fuzz.trimf(teor_materia_organica.universe, [0, 0, 1.6])
                teor_materia_organica['baixo'] = fuzz.trimf(teor_materia_organica.universe, [1.6, 2.5, 3.5])
                teor_materia_organica['medio'] = fuzz.trimf(teor_materia_organica.universe, [2.6, 3.5, 4.5])
                teor_materia_organica['alto'] = fuzz.trimf(teor_materia_organica.universe, [3.6, 4.5, 100])

                # Crie os conjuntos de pertinência para a Quantidade de Nitrogênio
                quantidade_nitrogenio['muito_baixo'] = fuzz.trimf(quantidade_nitrogenio.universe, [80, 80, 100])
                quantidade_nitrogenio['baixo'] = fuzz.trimf(quantidade_nitrogenio.universe, [100, 120, 140])
                quantidade_nitrogenio['medio'] = fuzz.trimf(quantidade_nitrogenio.universe, [120, 140, 160])
                quantidade_nitrogenio['alto'] = fuzz.trimf(quantidade_nitrogenio.universe, [140, 160, 180])

                # Crie os conjuntos de pertinência para o Nível de Fósforo
                nivel_p['muito_baixo'] = fuzz.trimf(nivel_p.universe, [110, 110, 170])
                nivel_p['baixo'] = fuzz.trimf(nivel_p.universe, [90, 110, 110])
                nivel_p['medio'] = fuzz.trimf(nivel_p.universe, [60, 100, 100])
                nivel_p['alto'] = fuzz.trimf(nivel_p.universe, [60, 60, 100])

                # Crie os conjuntos de pertinência para a Quantidade de Fósforo
                quantidade_fosforo['muito_baixo'] = fuzz.trimf(quantidade_fosforo.universe, [0, 0, 50])
                quantidade_fosforo['baixo'] = fuzz.trimf(quantidade_fosforo.universe, [0, 50, 100])
                quantidade_fosforo['medio'] = fuzz.trimf(quantidade_fosforo.universe, [50, 100, 100])
                quantidade_fosforo['alto'] = fuzz.trimf(quantidade_fosforo.universe, [50, 100, 100])

                # Crie os conjuntos de pertinência para o Nível de Potássio
                nivel_k['muito_baixo'] = fuzz.trimf(nivel_k.universe, [100, 140, 180])
                nivel_k['baixo'] = fuzz.trimf(nivel_k.universe, [80, 100, 120])
                nivel_k['medio'] = fuzz.trimf(nivel_k.universe, [60, 90, 120])
                nivel_k['alto'] = fuzz.trimf(nivel_k.universe, [60, 60, 60])

                # Crie os conjuntos de pertinência para a Quantidade de Potássio
                quantidade_potassio['muito_baixo'] = fuzz.trimf(quantidade_potassio.universe, [0, 0, 50])
                quantidade_potassio['baixo'] = fuzz.trimf(quantidade_potassio.universe, [0, 50, 100])
                quantidade_potassio['medio'] = fuzz.trimf(quantidade_potassio.universe, [50, 100, 100])
                quantidade_potassio['alto'] = fuzz.trimf(quantidade_potassio.universe, [50, 100, 100])

        elif entrada.Cultura == 'Leguminosas':
            # Defina as funções de pertinência para as variáveis de entrada (níveis de fósforo, potássio e eficiência de inoculação)
            nivel_p['muito_baixo'] = fuzz.smf(nivel_p.universe, 165,170)
            nivel_p['baixo'] = fuzz.trapmf(nivel_p.universe, [105, 135, 155, 169])
            nivel_p['medio'] = fuzz.trapmf(nivel_p.universe, [95, 104, 106, 109])
            nivel_p['alto'] = fuzz.trapmf(nivel_p.universe, [55, 68, 78, 99])
            nivel_p['muito_alto'] = fuzz.zmf(nivel_p.universe,40, 60)

            nivel_k['muito_baixo'] = fuzz.smf(nivel_p.universe, 135,145)
            nivel_k['baixo'] = fuzz.trapmf(nivel_p.universe, [95, 120, 130, 139])
            nivel_k['medio'] = fuzz.trapmf(nivel_p.universe, [85, 90, 94, 99])
            nivel_k['alto'] = fuzz.trapmf(nivel_p.universe, [55, 65, 75, 89])
            nivel_k['muito_alto'] = fuzz.zmf(nivel_p.universe, 40, 60)

            eficiencia_inoculacao['ineficiente'] = fuzz.trimf(eficiencia_inoculacao.universe, [0, 0, 50])
            eficiencia_inoculacao['eficiente'] = fuzz.trimf(eficiencia_inoculacao.universe, [40, 70, 100])

            # Defina as funções de pertinência para as variáveis de saída (quantidade de NPK e quantidade de nitrogênio)
            quantidade_nitrogenio['nitrogenio'] = fuzz.trimf(quantidade_nitrogenio.universe, [0, 0, 80])

        elif entrada.Cultura == 'Consórcios':    
            # Defina as funções de pertinência para as variáveis de entrada (níveis de fósforo, potássio e eficiência de inoculação)
            nivel_p['muito_baixo'] = fuzz.smf(nivel_p.universe, 190,195)
            nivel_p['baixo'] = fuzz.trapmf(nivel_p.universe, [125, 150, 160, 179])
            nivel_p['medio'] = fuzz.trapmf(nivel_p.universe, [115, 122, 125, 129])
            nivel_p['alto'] = fuzz.trapmf(nivel_p.universe, [75, 95, 115, 119])
            nivel_p['muito_alto'] = fuzz.zmf(nivel_p.universe,75, 80)

            nivel_k['muito_baixo'] = fuzz.smf(nivel_p.universe, 175,185)
            nivel_k['baixo'] = fuzz.trapmf(nivel_p.universe, [135, 145, 155, 179])
            nivel_k['medio'] = fuzz.trapmf(nivel_p.universe, [125, 132, 135, 139])
            nivel_k['alto'] = fuzz.trapmf(nivel_p.universe, [95, 115, 120, 129])
            nivel_k['muito_alto'] = fuzz.zmf(nivel_p.universe, 80, 100)

            eficiencia_inoculacao['ineficiente'] = fuzz.trimf(eficiencia_inoculacao.universe, [0, 0, 50])
            eficiencia_inoculacao['eficiente'] = fuzz.trimf(eficiencia_inoculacao.universe, [40, 70, 100])

            # Defina as funções de pertinência para as variáveis de saída (quantidade de NPK e quantidade de nitrogênio)
            quantidade_nitrogenio['nitrogenio'] = fuzz.trimf(quantidade_nitrogenio.universe, [0, 0, 80])
        
        elif entrada.Cultura == 'Campo natural':
            # Defina as funções de pertinência para as variáveis de entrada (níveis de fósforo, potássio e eficiência de inoculação)
            nivel_p['muito_baixo'] = fuzz.smf(nivel_p.universe, 95,105)
            nivel_p['baixo'] = fuzz.trapmf(nivel_p.universe, [70, 80, 90, 99])
            nivel_p['medio'] = fuzz.trapmf(nivel_p.universe, [65, 69, 72, 74])
            nivel_p['alto'] = fuzz.trapmf(nivel_p.universe, [45, 55, 65, 69])
            nivel_p['muito_alto'] = fuzz.zmf(nivel_p.universe,40, 50)

            nivel_k['muito_baixo'] = fuzz.smf(nivel_p.universe, 95,105)
            nivel_k['baixo'] = fuzz.trapmf(nivel_p.universe, [70, 80, 90, 99])
            nivel_k['medio'] = fuzz.trapmf(nivel_p.universe, [65, 69, 72, 74])
            nivel_k['alto'] = fuzz.trapmf(nivel_p.universe, [45, 55, 65, 69])
            nivel_k['muito_alto'] = fuzz.zmf(nivel_p.universe,40, 50)

            eficiencia_inoculacao['ineficiente'] = fuzz.trimf(eficiencia_inoculacao.universe, [0, 0, 50])
            eficiencia_inoculacao['eficiente'] = fuzz.trimf(eficiencia_inoculacao.universe, [40, 70, 100])

            # Defina as funções de pertinência para as variáveis de saída (quantidade de NPK e quantidade de nitrogênio)
            quantidade_nitrogenio['nitrogenio'] = fuzz.trimf(quantidade_nitrogenio.universe, [0, 0, 80])
            



    def processa_adubacao(self, entrada):
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

            # Cria as variáveis de entrada (níveis de fósforo, potássio, nitrogênio e eficiência de inoculação)
            nivel_p = ctrl.Antecedent(np.arange(0, 200, 1), 'Nível de Fósforo (P)')
            nivel_k = ctrl.Antecedent(np.arange(0, 200, 1), 'Nível de Potássio (K)')
            nivel_n = ctrl.Antecedent(np.arange(0, 200, 1), 'Nível de Nitrogênio (N)')
            eficiencia_inoculacao = ctrl.Antecedent(np.arange(0, 101, 1), 'Eficiência de Inoculação')
            quantidade_nitrogenio = ctrl.Consequent(np.arange(0, 80, 1), 'Quantidade de Nitrogênio')
            quantidade_fosforo = ctrl.Consequent(np.arange(0, 80, 1), 'Quantidade de Fósforo')
            quantidade_potassio = ctrl.Consequent(np.arange(0, 80, 1), 'Quantidade de Potássio')

            # Define as funções de pertinência para as variáveis de entrada e saída
            self.define_funcao_pertinencia(entrada, nivel_n, nivel_k, nivel_p, eficiencia_inoculacao,
                                           quantidade_nitrogenio, quantidade_fosforo, quantidade_potassio)

            # Cria regras Fuzzy para o Fósforo
            regra1_fosforo = ctrl.Rule(nivel_p['muito_baixo'], quantidade_fosforo['muito_baixo'])
            regra2_fosforo = ctrl.Rule(nivel_p['baixo'], quantidade_fosforo['baixo'])
            regra3_fosforo = ctrl.Rule(nivel_p['medio'], quantidade_fosforo['medio'])
            regra4_fosforo = ctrl.Rule(nivel_p['alto'], quantidade_fosforo['alto'])

            sistema_controle = ctrl.ControlSystem([regra1_fosforo, regra2_fosforo, regra3_fosforo, regra4_fosforo])
            sistema = ctrl.ControlSystemSimulation(sistema_controle)
            sistema.input['Nível de Fósforo (P)'] = int(entrada.p)
            sistema.compute()
            mensagem_P = f"É preciso aplicar {round(float(sistema.output['Quantidade de Fósforo']), 2)}kg/ha."
            print("Quantidade de Fósforo:", sistema.output['Quantidade de Fósforo'])

            # Cria regras Fuzzy para o Potássio
            regra1_potassio = ctrl.Rule(nivel_k['muito_baixo'], quantidade_potassio['muito_baixo'])
            regra2_potassio = ctrl.Rule(nivel_k['baixo'], quantidade_potassio['baixo'])
            regra3_potassio = ctrl.Rule(nivel_k['medio'], quantidade_potassio['medio'])
            regra4_potassio = ctrl.Rule(nivel_k['alto'], quantidade_potassio['alto'])

            sistema_controle = ctrl.ControlSystem([regra1_potassio, regra2_potassio, regra3_potassio, regra4_potassio])
            sistema = ctrl.ControlSystemSimulation(sistema_controle)
            sistema.input['Nível de Potássio (K)'] = int(entrada.k)
            sistema.compute()
            mensagem_K = f"É preciso aplicar {round(float(sistema.output['Quantidade de Potássio']), 2)}kg/ha."
            print("Quantidade de Potássio:", sistema.output['Quantidade de Potássio'])

        if entrada.Cultura == 'Gramíneas':
            if entrada.Estacao == 'Fria':
                teor_materia_organica = ctrl.Antecedent(np.arange(0, 5.1, 0.1), 'Teor de Matéria Orgânica no Solo')
                quantidade_nitrogenio = ctrl.Consequent(np.arange(80, 181, 1), 'Quantidade de Nitrogênio')
                nivel_p = ctrl.Antecedent(np.arange(0, 200, 1), 'Nível de Fósforo (P)')
                quantidade_fosforo = ctrl.Consequent(np.arange(0, 101, 1), 'Quantidade de Fósforo')
                nivel_k = ctrl.Antecedent(np.arange(0, 200, 1), 'Nível de Potássio (K)')
                quantidade_potassio = ctrl.Consequent(np.arange(0, 101, 1), 'Quantidade de Potássio')
                # Define as funções de pertinência para as variáveis de entrada e saída
                self.define_funcao_pertinencia(entrada=entrada, nivel_n=nivel_k, nivel_p=nivel_p, nivel_k=nivel_k,
                                               eficiencia_inoculacao=0,
                                               quantidade_nitrogenio=quantidade_nitrogenio,
                                               quantidade_fosforo=quantidade_fosforo,
                                               quantidade_potassio=quantidade_potassio,
                                               teor_materia_organica=teor_materia_organica)

                # Crie regras Fuzzy para o Nitrogênio
                regra1_nitrogenio = ctrl.Rule(teor_materia_organica['muito_baixo'],quantidade_nitrogenio['muito_baixo'])
                regra2_nitrogenio = ctrl.Rule(teor_materia_organica['baixo'], quantidade_nitrogenio['baixo'])
                regra3_nitrogenio = ctrl.Rule(teor_materia_organica['medio'], quantidade_nitrogenio['medio'])
                regra4_nitrogenio = ctrl.Rule(teor_materia_organica['alto'], quantidade_nitrogenio['alto'])

                # Crie o sistema de controle fuzzy
                sistema_controle_nitrogenio = ctrl.ControlSystem([regra1_nitrogenio, regra2_nitrogenio, regra3_nitrogenio, regra4_nitrogenio])
                sistema_nitrogenio = ctrl.ControlSystemSimulation(sistema_controle_nitrogenio)
                sistema_nitrogenio.input['Teor de Matéria Orgânica no Solo'] = float(entrada.MateriaOrganica)
                sistema_nitrogenio.compute()
                mensagem_N = f"É preciso aplicar {round(float(sistema_nitrogenio.output['Quantidade de Nitrogênio']), 2)}kg/ha."
                print("Quantidade de Nitrogênio:", sistema_nitrogenio.output['Quantidade de Nitrogênio'])

                # Crie regras Fuzzy para o Fósforo
                regra1_fosforo = ctrl.Rule(nivel_p['muito_baixo'], quantidade_fosforo['muito_baixo'])
                regra2_fosforo = ctrl.Rule(nivel_p['baixo'], quantidade_fosforo['baixo'])
                regra3_fosforo = ctrl.Rule(nivel_p['medio'], quantidade_fosforo['medio'])
                regra4_fosforo = ctrl.Rule(nivel_p['alto'], quantidade_fosforo['alto'])

                # Crie o sistema de controle fuzzy
                sistema_controle_fosforo = ctrl.ControlSystem(
                    [regra1_fosforo, regra2_fosforo, regra3_fosforo, regra4_fosforo])
                sistema_fosforo = ctrl.ControlSystemSimulation(sistema_controle_fosforo)
                sistema_fosforo.input['Nível de Fósforo (P)'] = int(entrada.p)
                sistema_fosforo.compute()
                mensagem_P = f"É preciso aplicar {round(float(sistema_fosforo.output['Quantidade de Fósforo']), 2)}kg/ha."
                print(mensagem_P)

                # Crie regras Fuzzy para o Potássio
                regra1_potassio = ctrl.Rule(nivel_k['muito_baixo'], quantidade_potassio['muito_baixo'])
                regra2_potassio = ctrl.Rule(nivel_k['baixo'], quantidade_potassio['baixo'])
                regra3_potassio = ctrl.Rule(nivel_k['medio'], quantidade_potassio['medio'])
                regra4_potassio = ctrl.Rule(nivel_k['alto'], quantidade_potassio['alto'])

                # Crie o sistema de controle fuzzy
                sistema_controle_potassio = ctrl.ControlSystem(
                    [regra1_potassio, regra2_potassio, regra3_potassio, regra4_potassio])
                sistema_potassio = ctrl.ControlSystemSimulation(sistema_controle_potassio)
                sistema_potassio.input['Nível de Potássio (K)'] = int(entrada.k)
                sistema_potassio.compute()
                mensagem_K = f"É preciso aplicar {round(float(sistema_potassio.output['Quantidade de Potássio']), 2)}kg/ha."
                print(mensagem_K)

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
