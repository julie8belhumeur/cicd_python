from cicd_python.app.convertisseur import convertir_minutes_heures

def run_tests():
    assert convertir_minutes_heures(1) == ("+", 0, 1)
    assert convertir_minutes_heures(130) == ("+", 2, 10)
    assert convertir_minutes_heures(60) == ("+", 1, 0)
    assert convertir_minutes_heures(-61) == ("-", 1, 1)
    assert convertir_minutes_heures(-132) == ("-", 2, 12)

if __name__ == "__main__":
    run_tests()
