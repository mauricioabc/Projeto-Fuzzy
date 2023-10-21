from Infraestructure.CalcCalculator import CalcCalculator


class APIManager:

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
