import unittest
from app.convertisseur import convertir_minutes_heures

class TestConvertisseur(unittest.TestCase):
    def test_positive_hours_minutes(self):
        self.assertEqual(convertir_minutes_heures(130), ("+", 2, 10))

    def test_positive_hours(self):
        self.assertEqual(convertir_minutes_heures(180), ("+", 3, 0))

    def test_positive_minutes(self):
        self.assertEqual(convertir_minutes_heures(33), ("+", 0, 33))

    def test_negative_hours_minutes(self):
        self.assertEqual(convertir_minutes_heures(-61), ("-", 1, 1))
        self.assertEqual(convertir_minutes_heures(-132), ("-", 2, 12))

    def test_zero(self):
        self.assertEqual(convertir_minutes_heures(0), ("+", 0, 0))

    def test_error_on_string(self):
        with self.assertRaises(TypeError) as context:
            convertir_minutes_heures("abc")
        self.assertEqual(str(context.exception), "L'argument doit être un entier.")

    def test_error_on_float(self):
        with self.assertRaises(TypeError) as context:
            convertir_minutes_heures(78.3)
        self.assertEqual(str(context.exception), "L'argument doit être un entier.")

    def test_error_on_null(self):
        with self.assertRaises(TypeError) as context:
            convertir_minutes_heures(None)
        self.assertEqual(str(context.exception), "L'argument doit être un entier.")
