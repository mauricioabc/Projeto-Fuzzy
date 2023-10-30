# Projeto Fuzzy

## Descrição

Esta API fornece serviços de recomendação de calagem e adubação para diferentes culturas e condições de solo. As operações disponíveis incluem o cálculo de calagem com base nas propriedades do solo e a recomendação de NPK (nitrogênio, fósforo e potássio) para adubação.

## Endpoints

### Calagem

#### `POST /ProcessaCalagem`

- **Descrição:** Calcula a recomendação de calagem com base nas entradas fornecidas.
- **Corpo da Solicitação:**
  - Formato: application/json
  - Esquema: [Calagem](#calagem)
- **Resposta de Sucesso:**
  - Formato: application/json
  - Esquema: [Calagem](#calagem)

### Adubação

#### `POST /ProcessaAdubacao`

- **Descrição:** Calcula a recomendação de NPK com base nas entradas fornecidas.
- **Corpo da Solicitação:**
  - Formato: application/json
  - Esquema: [Adubacao](#adubacao)
- **Resposta de Sucesso:**
  - Formato: application/json
  - Esquema: [Adubacao](#adubacao)

## Modelos de Dados

### Calagem

```json
{
  "Especie": "string",
  "Cultura": "string",
  "TipoPlantio": "string",
  "phSolo": "string",
  "IndiceSMP": "string",
  "Bases": "string",
  "Ca": "string",
  "Mg": "string",
  "AlSat": "string",
  "CTC": "string"
}
```

### Adubacao

```json
{
  "Especie": "string",
  "Cultura": "string",
  "Estacao": "string",
  "TipoPlantio": "string",
  "NivelNitrogenio": "string",
  "EficienciaInoculacao": "string",
  "NivelFosforo": "string",
  "NivelPotassio": "string",
  "MateriaOrganica": "string",
  "TeorArgila": "string",
  "CTC": "string"
}
```

### ApiResponse

```json
{
  "message": "string",
  "status": "string"
}
```

## Observações

Certifique-se de incluir no corpo da solicitação os dados adequados conforme especificado nos esquemas de [Calagem](#calagem) ou [Adubacao](#adubacao). A resposta bem-sucedida será um objeto com o esquema correspondente.

## Exemplos de Uso

### Calagem

**Requisição:**

```json
{
  "Especie": "Forrageira",
  "Cultura": "Alfafa",
  "TipoPlantio": "Convencional",
  "phSolo": "7.0",
  "IndiceSMP": "5.19",
  "Bases": "23.85",
  "Ca": "2.07",
  "Mg": "1.17",
  "AlSat": "38.87",
  "CTC": "14.51"
}
```

**Resposta Bem-Sucedida:**

```json
{
	"message": "É preciso adicionar 2.34 toneladas de Calcário por hectare de forma superficial.",
	"status": "success"
}
```

### Adubação

**Requisição:**

```json
{
  "Especie": "Forrageira",
  "Cultura": "Alfafa",
  "Estacao": "Fria",
  "TipoPlantio": "Convencional",
  "NivelNitrogenio": "1.20",
  "EficienciaInoculacao": "true",
  "NivelFosforo": "1.20",
  "NivelPotassio": "1.20",
  "MateriaOrganica": "5.1",
  "TeorArgila": "45",
  "CTC": "14.51"
}
```

**Resposta Bem-Sucedida:**

```json
{
	"message": {
		"K": "É preciso aplicar 144.94kg/ha.",
		"N": "É preciso aplicar 102.34kg/ha.",
		"P": "É preciso aplicar 189.96kg/ha."
	},
	"status": "success"
}
```

## Notas Importantes

Certifique-se de validar e fornecer entradas válidas para obter resultados precisos. Consulte a documentação para obter informações detalhadas sobre os parâmetros e os formatos de resposta.

## Versão

1.0.0