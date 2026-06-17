def temperaturas(temp_media = 0):
    import calendar
    temp = []
    for cont in range(1, 13):
        temp_media = int(input(f"Temperatura média do {cont} mês: "))
        temp.append(temp_media)
    print("=" * 30)
    for i, temperatura in enumerate(temp, start=1): # Start altera o valor inicial do indice
        print(f"{calendar.month_abbr[i]}: {temperatura}°C")
    print("=" * 30)
    return f"Média anual: {sum(temp) / 12:.1f}°C"


print(temperaturas())
