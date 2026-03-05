def calcular_simulacao(valor_inicial: float, aporte_mensal: float, taxa_anual: float, anos: int):
    total_meses = anos * 12
    taxa_mensal = taxa_anual / 100 / 12
    
    data = []
    acumulado = valor_inicial
    investido = valor_inicial

    # Mês 0 (Estado inicial)
    data.append({
        "mes": 0, 
        "valor": round(acumulado, 2), 
        "investido": round(investido, 2)
    })

    for mes in range(1, total_meses + 1):
        acumulado = acumulado * (1 + taxa_mensal) + aporte_mensal
        investido += aporte_mensal
        
        data.append({
            "mes": mes,
            "valor": round(acumulado, 2), # Equivalente ao Math.round do front
            "investido": round(investido, 2)
        })

    return data