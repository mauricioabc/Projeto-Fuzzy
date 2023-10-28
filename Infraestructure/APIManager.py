from Infraestructure.CalcCalculator import CalcCalculator
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class APIManager:

    def define_funcao_pertinencia(self, entrada, nivel_k, nivel_p, eficiencia_inoculacao, quantidade_npk, quantidade_nitrogenio):
        if entrada.Cultura == 'Alfafa':
            # Defina as funções de pertinência para as variáveis de entrada (níveis de fósforo, potássio e eficiência de inoculação)
            nivel_p['muito_baixo'] = fuzz.trapmf(nivel_p.universe, [190, 194, 196, 200])
            nivel_p['baixo'] = fuzz.trapmf(nivel_p.universe, [130, 135, 155, 194])
            nivel_p['medio'] = fuzz.trapmf(nivel_p.universe, [120, 126, 130, 134])
            nivel_p['alto'] = fuzz.trapmf(nivel_p.universe, [80, 95, 105, 124])
            nivel_p['muito_alto'] = fuzz.zmf(nivel_p.universe, 50, 84)

            nivel_k['muito_baixo'] = fuzz.trapmf(nivel_p.universe, [330, 350, 360, 370])
            nivel_k['baixo'] = fuzz.trapmf(nivel_p.universe, [250, 280, 290, 330])
            nivel_k['medio'] = fuzz.trapmf(nivel_p.universe, [280, 284, 286, 289])
            nivel_k['alto'] = fuzz.trapmf(nivel_p.universe, [250, 260, 270, 279])
            nivel_k['muito_alto'] = fuzz.zmf(nivel_p.universe, 150, 249)

            eficiencia_inoculacao['ineficiente'] = fuzz.trimf(eficiencia_inoculacao.universe, [0, 0, 50])
            eficiencia_inoculacao['eficiente'] = fuzz.trimf(eficiencia_inoculacao.universe, [40, 70, 100])

            # Defina as funções de pertinência para as variáveis de saída (quantidade de NPK e quantidade de nitrogênio)

            quantidade_npk['correcao'] = fuzz.trimf(quantidade_npk.universe, [0, 0, 100])
            quantidade_npk['manutencao'] = fuzz.trimf(quantidade_npk.universe, [90, 150, 200])
            quantidade_nitrogenio['nitrogenio'] = fuzz.trimf(quantidade_nitrogenio.universe, [0, 0, 80])
            
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

            quantidade_npk['correcao'] = fuzz.trimf(quantidade_npk.universe, [0, 0, 100])
            quantidade_npk['manutencao'] = fuzz.trimf(quantidade_npk.universe, [90, 150, 200])
            quantidade_nitrogenio['nitrogenio'] = fuzz.trimf(quantidade_nitrogenio.universe, [0, 0, 80])
            
        elif entrada.Cultura == 'Gramíneas':
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

            quantidade_npk['correcao'] = fuzz.trimf(quantidade_npk.universe, [0, 0, 100])
            quantidade_npk['manutencao'] = fuzz.trimf(quantidade_npk.universe, [90, 150, 200])
            quantidade_nitrogenio['nitrogenio'] = fuzz.trimf(quantidade_nitrogenio.universe, [0, 0, 80])

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

            quantidade_npk['correcao'] = fuzz.trimf(quantidade_npk.universe, [0, 0, 100])
            quantidade_npk['manutencao'] = fuzz.trimf(quantidade_npk.universe, [90, 150, 200])
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

            quantidade_npk['correcao'] = fuzz.trimf(quantidade_npk.universe, [0, 0, 100])
            quantidade_npk['manutencao'] = fuzz.trimf(quantidade_npk.universe, [90, 150, 200])
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

            quantidade_npk['correcao'] = fuzz.trimf(quantidade_npk.universe, [0, 0, 100])
            quantidade_npk['manutencao'] = fuzz.trimf(quantidade_npk.universe, [90, 150, 200])
            quantidade_nitrogenio['nitrogenio'] = fuzz.trimf(quantidade_nitrogenio.universe, [0, 0, 80])
            

    def processa_adubacao(self, entrada):
        # Cria as variáveis de entrada (níveis de fósforo, potássio e eficiência de inoculação)
        nivel_p = ctrl.Antecedent(np.arange(0, 200, 1), 'Nível de Fósforo (P)')
        nivel_k = ctrl.Antecedent(np.arange(0, 200, 1), 'Nível de Potássio (K)')
        eficiencia_inoculacao = ctrl.Antecedent(np.arange(0, 101, 1), 'Eficiência de Inoculação')

        # Cria as variáveis de saída (quantidade de NPK e quantidade de Nitrogênio)
        quantidade_npk = ctrl.Consequent(np.arange(0, 300, 1), 'Quantidade de NPK')
        quantidade_nitrogenio = ctrl.Consequent(np.arange(0, 80, 1), 'Quantidade de Nitrogênio')

        # Define as funções de pertinência para as variáveis de entrada e saída
        self.define_funcao_pertinencia(entrada, nivel_k, nivel_p, eficiencia_inoculacao, quantidade_npk, quantidade_nitrogenio)

        # Cria regras Fuzzy para o NPK
        regra1_npk = ctrl.Rule(nivel_p['muito_baixo'] & nivel_k['muito_baixo'] & eficiencia_inoculacao['ineficiente'], quantidade_npk['correcao'])
        regra2_npk = ctrl.Rule(nivel_p['baixo'] & nivel_k['baixo'] & eficiencia_inoculacao['ineficiente'], quantidade_npk['correcao'])
        regra3_npk = ctrl.Rule(nivel_p['medio'] & nivel_k['medio'] & eficiencia_inoculacao['ineficiente'], quantidade_npk['correcao'])
        regra4_npk = ctrl.Rule(nivel_p['alto'] & nivel_k['alto'] & eficiencia_inoculacao['ineficiente'], quantidade_npk['correcao'])
        regra5_npk = ctrl.Rule(nivel_p['muito_alto'] & nivel_k['muito_alto'] & eficiencia_inoculacao['ineficiente'], quantidade_npk['correcao'])

        regra6_npk = ctrl.Rule(nivel_p['muito_baixo'] & nivel_k['muito_baixo'] & eficiencia_inoculacao['eficiente'], quantidade_npk['manutencao'])
        regra7_npk = ctrl.Rule(nivel_p['baixo'] & nivel_k['baixo'] & eficiencia_inoculacao['eficiente'], quantidade_npk['manutencao'])
        regra8_npk = ctrl.Rule(nivel_p['medio'] & nivel_k['medio'] & eficiencia_inoculacao['eficiente'], quantidade_npk['manutencao'])
        regra9_npk = ctrl.Rule(nivel_p['alto'] & nivel_k['alto'] & eficiencia_inoculacao['eficiente'], quantidade_npk['manutencao'])
        regra10_npk = ctrl.Rule(nivel_p['muito_alto'] & nivel_k['muito_alto'] & eficiencia_inoculacao['eficiente'], quantidade_npk['manutencao'])

        # Cria regras Fuzzy para o Nitrogênio
        regra1_nitrogenio = ctrl.Rule(nivel_p['muito_baixo'] & nivel_k['muito_baixo'] & eficiencia_inoculacao['ineficiente'], quantidade_nitrogenio['nitrogenio'])
        regra2_nitrogenio = ctrl.Rule(nivel_p['baixo'] & nivel_k['baixo'] & eficiencia_inoculacao['ineficiente'], quantidade_nitrogenio['nitrogenio'])
        regra3_nitrogenio = ctrl.Rule(nivel_p['medio'] & nivel_k['medio'] & eficiencia_inoculacao['ineficiente'], quantidade_nitrogenio['nitrogenio'])
        regra4_nitrogenio = ctrl.Rule(nivel_p['alto'] & nivel_k['alto'] & eficiencia_inoculacao['ineficiente'], quantidade_nitrogenio['nitrogenio'])
        regra5_nitrogenio = ctrl.Rule(nivel_p['muito_alto'] & nivel_k['muito_alto'] & eficiencia_inoculacao['ineficiente'], quantidade_nitrogenio['nitrogenio'])

        regra6_nitrogenio = ctrl.Rule(nivel_p['muito_baixo'] & nivel_k['muito_baixo'] & eficiencia_inoculacao['eficiente'], quantidade_nitrogenio['nitrogenio'])
        regra7_nitrogenio = ctrl.Rule(nivel_p['baixo'] & nivel_k['baixo'] & eficiencia_inoculacao['eficiente'], quantidade_nitrogenio['nitrogenio'])
        regra8_nitrogenio = ctrl.Rule(nivel_p['medio'] & nivel_k['medio'] & eficiencia_inoculacao['eficiente'], quantidade_nitrogenio['nitrogenio'])
        regra9_nitrogenio = ctrl.Rule(nivel_p['alto'] & nivel_k['alto'] & eficiencia_inoculacao['eficiente'], quantidade_nitrogenio['nitrogenio'])
        regra10_nitrogenio = ctrl.Rule(nivel_p['muito_alto'] & nivel_k['muito_alto'] & eficiencia_inoculacao['eficiente'], quantidade_nitrogenio['nitrogenio'])

        # Adicione as regras ao sistema de controle Fuzzy para NPK
        sistema_adubacao_npk = ctrl.ControlSystem([regra1_npk, regra2_npk, regra3_npk, regra4_npk, regra5_npk, regra6_npk, regra7_npk, regra8_npk, regra9_npk, regra10_npk])
        adubacao_npk = ctrl.ControlSystemSimulation(sistema_adubacao_npk)

        # Adicione as regras ao sistema de controle Fuzzy para Nitrogênio
        sistema_adubacao_nitrogenio = ctrl.ControlSystem([regra1_nitrogenio, regra2_nitrogenio, regra3_nitrogenio, regra4_nitrogenio, regra5_nitrogenio, regra6_nitrogenio, regra7_nitrogenio, regra8_nitrogenio, regra9_nitrogenio, regra10_nitrogenio])
        adubacao_nitrogenio = ctrl.ControlSystemSimulation(sistema_adubacao_nitrogenio)

        # Define os valores de entrada para as variáveis antecedentes
        adubacao_npk.input['Nível de Fósforo (P)'] = float(entrada.p)
        adubacao_npk.input['Nível de Potássio (K)'] = float(entrada.k)
        adubacao_npk.input['Eficiência de Inoculação'] = float(entrada.inoculacao)


        # Computa o resultado para NPK
        adubacao_npk.compute()

        # Computa o resultado para Nitrogênio
        adubacao_nitrogenio.compute()

        # Imprime as quantidades necessárias de NPK e Nitrogênio
        quantidade_npk = round(float(adubacao_npk.output['Quantidade de NPK']), 2)
        quantidade_nitrogenio = round(float(adubacao_nitrogenio.output['Quantidade de Nitrogênio']), 2)

        mensagem_npk = f"É preciso aplicar {quantidade_npk} kg/ha."
        mensagem_nitrogenio = f"É preciso aplicar {quantidade_nitrogenio}kg/ha."

        return mensagem_npk, mensagem_nitrogenio



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
