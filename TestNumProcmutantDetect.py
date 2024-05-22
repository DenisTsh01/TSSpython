import unittest
from NumProc2 import NumberProcessor

####pentru prezentarea mutantilor la examen
class NumberProcessorTest(unittest.TestCase):  

    # higher order mutant detect.
    def test_higher_order_mutants(self):
        processor = NumberProcessor(20, 20)
        result = processor.process_numbers_mutant2()
        self.assertEqual(processor.x, 0)  # Mutantul ar cauza bucla să continue
        self.assertEqual(result, -20)     # Verificăm rezultatul final

        processor = NumberProcessor(15, 19)
        result = processor.process_numbers_mutant2()
        self.assertEqual(result, -5)      # Verificăm rezultatul final
        
    # first order
    def test_loop_condition_mutant(self):
        processor = NumberProcessor(10, 10)
        result = processor.process_numbers_mutant1()
        self.assertEqual(processor.x, 0)  # Mutantul ar cauza bucla să continue
        self.assertEqual(result, -20)     # Verificăm rezultatul final
        
    # weak mutant detect.
    def test_weak_mutation(self):
        processor = NumberProcessor(11, 19)
        result = processor.process_numbers_weak()
        self.assertNotEqual(result, 2 * 1 - 1)  # Detectăm schimbarea în operație

    # strong mutant detect.
    def test_strong_mutation(self):
        processor = NumberProcessor(10, 15)
        result = processor.process_numbers_strong()
        self.assertNotEqual(result, 2 * 10 + 35)  # Detectăm schimbarea logicii
        
     # test suplimentar pt a omori mutant1 neechivalent
    def test_while_loop_condition_neechivalent1(self):
        # Acest test eșuează dacă bucla se execută atunci când x este exact 10.
        processor = NumberProcessor(10, 10)
        result = processor.process_numbers_neechivalent1()
        self.assertEqual(processor.x, 10)  # x nu ar trebui să fie schimbat
        self.assertEqual(processor.y, -10)  # y ar trebui să fie scăzut cu 20
        self.assertEqual(result, 2 * 10 - 10)  # Așteptăm ca rezultatul să fie 10
        
    # test suplimentar pt a omori mutant2 neechivalent 
    def test_y_adjustment_condition(self):
        # Acest test eșuează dacă y este crescut atunci când y este exact 20.
        processor = NumberProcessor(10, 20)
        result = processor.process_numbers_neechivalent2()
        self.assertEqual(processor.y, 0)  # y ar trebui să fie scăzut cu 20
        self.assertEqual(result, 2 * 10 + 0)  # Așteptăm ca rezultatul să fie 20


if __name__ == '__main__':
    unittest.main()