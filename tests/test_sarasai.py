import unittest
from Justina_S_Mod1_Atsiskaitymas.Gintarine import gintarine_vaistine, irasyti_i_faila

class Testpavadinimu_sarasas(unittest.TestCase):

    def test_ar_isrenka(self):

        pavadinimai, kainos = gintarine_vaistine()


        self.assertEqual(len(kainos),20)
        self.assertEqual(len(pavadinimai), 20)

    def test_ar_yrakaina1399(self):

        pavadinimai, kainos = gintarine_vaistine()

        self.assertIn('13.99',kainos)


    def test_ar_iraso(self):
            pavadinimai, kainos = gintarine_vaistine()

            irasyti_i_faila(pavadinimai,kainos)

            with open("failas.txt", 'r') as failas:
                nuskaityta_pavadinimai = failas.readline()
                nuskaityta_kainos = failas.readline()

            self.assertEqual(nuskaityta_kainos,"['13.49', '13.99', '11.99', '19.49', '14.99', '14.99', '39.99', '17.99', '18.89', '31.39', '15.49', '24.00', '32.49', '32.59', '16.39', '14.99', '27.29', '14.99', '14.99', '31.29']")
