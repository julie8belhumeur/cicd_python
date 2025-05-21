from cicd_python.app.convertisseur import convertir_minutes_heures
 
def run_tests():
    assert convertir_minutes_heures(1) == ("+", 0, 1)
    assert convertir_minutes_heures(130) == ("+", 2, 10)
    assert convertir_minutes_heures(60) == ("+", 1, 0)
    assert convertir_minutes_heures(-61) == ("-", 1, 1)
    assert convertir_minutes_heures(-132) == ("-", 2, 12)
    assert convertir_minutes_heures(0) == ("+", 0, 0)

    try:
        convertir_minutes_heures("abc")
    except TypeError as e:
        assert str(e) == "L'argument doit être un entier."
    else:
        assert False, "TypeError non levée pour une chaîne"

    try:
        convertir_minutes_heures(12.5)
    except TypeError as e:
        assert str(e) == "L'argument doit être un entier."
    else:
        assert False, "TypeError non levée pour un float"

    try:
        convertir_minutes_heures(None)
    except TypeError as e:
        assert str(e) == "L'argument doit être un entier."
    else:
        assert False, "TypeError non levée pour None"




if __name__ == "__main__":
    run_tests()
