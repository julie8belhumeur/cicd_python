def convertir_minutes_heures(total_minutes):
    if not isinstance(total_minutes, int):
        print("L'argument doit être un entier.")
        raise TypeError("L'argument doit être un entier.")

    signe = "+"
    if total_minutes < 0:
        signe = "-"
        total_minutes = -total_minutes
    heures = total_minutes // 60
    minutes = total_minutes % 60
    print(signe, heures, minutes)
    return signe, heures, minutes
