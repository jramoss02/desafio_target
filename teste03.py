"""
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
"""

import json

# Exemplo de dados de faturamento em JSON
dados_json = '''{
    "faturamento_diario": [0, 1200, 800, 0, 1500, 900, 0, 1700, 1400, 0, 0, 2000, 1300, 1600, 0, 1800, 0, 2100, 0, 1900]
}'''

dados = json.loads(dados_json)["faturamento_diario"]

# Filtrando dias sem faturamento (0)
faturamento_filtrado = [valor for valor in dados if valor > 0]

# Calculando estatísticas
menor_faturamento = min(faturamento_filtrado)
maior_faturamento = max(faturamento_filtrado)
media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

dias_acima_da_media = sum(1 for valor in faturamento_filtrado if valor > media_mensal)

print(f"Menor faturamento diário: R${menor_faturamento:.2f}")
print(f"Maior faturamento diário: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
