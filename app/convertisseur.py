def convertir_minutes_heures(total_minutes):
    signe = "+"
    if (total_minutes < 0):
        signe = "-"
        total_minutes = -total_minutes
    heures = total_minutes // 60
    minutes = total_minutes % 60
    return signe, heures, minutes
