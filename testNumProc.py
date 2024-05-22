import unittest
from NumProc import NumberProcessor

class NumberProcessorTest(unittest.TestCase):  
    def test_statement_coverage(self):
        Np = NumberProcessor(20, 10)
        self.assertEqual(Np.process_numbers(), 50)
        Np = NumberProcessor(20, 30)
        self.assertEqual(Np.process_numbers(), 30)

    def test_decision_coverage(self):
        Np = NumberProcessor(20, 10)
        self.assertEqual(Np.process_numbers(), 50)
        Np = NumberProcessor(15, 30)
        self.assertEqual(Np.process_numbers(), 20)

    def test_condition_coverage(self):
        Np = NumberProcessor(20, 10)
        self.assertEqual(Np.process_numbers(), 50)
        Np = NumberProcessor(5, 30)
        self.assertEqual(Np.process_numbers(), 20)
        Np = NumberProcessor(21, 10)
        self.assertEqual(Np.process_numbers(), -8)

    #===========Partiționare de echivalență==============#

    def test_x_and_y_are_integers(self):
        Np = NumberProcessor(10, 20)
        self.assertEqual(Np.process_numbers(), 20)

    def test_x_or_y_not_integer(self):
        with self.assertRaises(ValueError):
            Np = NumberProcessor('10', 20)
            Np.process_numbers()
        with self.assertRaises(ValueError):
            Np = NumberProcessor(10, '20')
            Np.process_numbers()
    
   
    

    def test_x_greater_than_10(self):
        Np = NumberProcessor(15, 20)
        self.assertEqual(Np.process_numbers(), 10)
        
        
     

    def test_x_less_or_equal_to_10(self):
        Np = NumberProcessor(10, 20)
        self.assertEqual(Np.process_numbers(), 20)

    def test_y_less_than_20_x_even(self):
        Np = NumberProcessor(10, 10)
        self.assertEqual(Np.process_numbers(), 50)

    #=====================================================#

    #==========Analiza valorilor de frontieră=============#

    def test_x_just_above_10_y_below_20(self):
        processor = NumberProcessor(11, 19)
        result = processor.process_numbers()
        self.assertEqual(processor.x, 1)
        self.assertEqual(processor.y, -1)
        self.assertEqual(result, 2 * 1 - 1)
        
        
    def test_while_loop_decrement_by_9_mutant(self):
        # Acest test eșuează dacă `x` este decrementat cu 9 în loc de 10.
        processor = NumberProcessor(29, 15)  # alegem 29 pentru a verifica cum se comportă după mai multe iterații
        result = processor.process_numbers()
        expected_x = 9  # Așteptăm ca x să fie 9 după decrementări (29 - 10 - 10)
        expected_y = -5  # y scăzut cu 20 pentru că y inițial este < 20 și x final nu este par
        self.assertEqual(processor.x, expected_x)
        print(processor.x)
        self.assertEqual(processor.y, expected_y)
        self.assertEqual(result, 2 * expected_x + expected_y)

    def test_x_is_exactly_10_y_exactly_20(self):
        processor = NumberProcessor(10, 20)
        result = processor.process_numbers()
        self.assertEqual(processor.x, 10)
        self.assertEqual(processor.y, 0)  
        self.assertEqual(result, 2 * 10 + 0)

    def test_x_below_10_y_above_20(self):
        processor = NumberProcessor(8, 25)
        result = processor.process_numbers()
        self.assertEqual(processor.x, 8)
        self.assertEqual(processor.y, 5)  
        self.assertEqual(result, 2 * 8 + 5)

    def test_x_is_negative(self):
        processor = NumberProcessor(-5, 15)
        result = processor.process_numbers()
        self.assertEqual(processor.x, -5)
        self.assertEqual(processor.y, -5)  
        self.assertEqual(result, 2 * -5 + -5)

    def test_x_is_zero_y_is_negative(self):
        processor = NumberProcessor(0, -10)
        result = processor.process_numbers()
        self.assertEqual(processor.x, 0)
        self.assertEqual(processor.y, 10)  
        self.assertEqual(result, 2 * 0 + 10)

    def test_x_above_10_and_even_y_below_20(self):
        processor = NumberProcessor(12, 18)
        result = processor.process_numbers()
        self.assertEqual(processor.x, 2)
        self.assertEqual(processor.y, 38) 
        self.assertEqual(result, 2 * 2 + 38)

    def test_x_below_10_and_even_y_below_20(self):
        processor = NumberProcessor(4, 15)
        result = processor.process_numbers()
        self.assertEqual(processor.x, 4)
        self.assertEqual(processor.y, 35)  
        self.assertEqual(result, 2 * 4 + 35)  

    def test_x_above_10_and_odd_y_above_20(self):
        processor = NumberProcessor(13, 30)
        result = processor.process_numbers()
        self.assertEqual(processor.x, 3)
        self.assertEqual(processor.y, 10)  
        self.assertEqual(result, 2 * 3 + 10)  
    #=====================================================#
    #           Mutanti
    #first order mutant detect.
    # def test_loop_condition_mutant(self):
    #     processor = NumberProcessor(10, 10)
    #     result = processor.process_numbers()
    #     self.assertEqual(processor.x, 0)  # Mutantul ar cauza bucla să continue
    #     self.assertEqual(result, -20)     # Verificăm rezultatul final
        
    # # higher order mutant detect.
    # def test_higher_order_mutants(self):
    #     processor = NumberProcessor(20, 20)
    #     result = processor.process_numbers()
    #     self.assertEqual(processor.x, 0)  # Mutantul ar cauza bucla să continue
    #     self.assertEqual(result, -20)     # Verificăm rezultatul final

    #     processor = NumberProcessor(15, 19)
    #     result = processor.process_numbers()
    #     self.assertEqual(result, -5)      # Verificăm rezultatul final

    # # weak mutant detect.
    # def test_weak_mutation(self):
    #     processor = NumberProcessor(11, 19)
    #     result = processor.process_numbers()
    #     self.assertNotEqual(result, 2 * 1 - 1)  # Detectăm schimbarea în operație

    # # strong mutant detect.
    # def test_strong_mutation(self):
    #     processor = NumberProcessor(10, 15)
    #     result = processor.process_numbers()
    #     self.assertNotEqual(result, 2 * 10 + 35)  # Detectăm schimbarea logicii
        
    ## test suplimentar pt a omori mutant1 neechivalent
    # def test_while_loop_condition_neechivalent1(self):
        # # Acest test eșuează dacă bucla se execută atunci când x este exact 10.
        # processor = NumberProcessor(10, 10)
        # result = processor.process_numbers_neechivalent1()
        # self.assertEqual(processor.x, 10)  # x nu ar trebui să fie schimbat
        # self.assertEqual(processor.y, -10)  # y ar trebui să fie scăzut cu 20
        # self.assertEqual(result, 2 * 10 - 10)  # Așteptăm ca rezultatul să fie 10
        
    # # test suplimentar pt a omori mutant2 neechivalent 
    # def test_y_adjustment_condition(self):
    #     # Acest test eșuează dacă y este crescut atunci când y este exact 20.
    #     processor = NumberProcessor(10, 20)
    #     result = processor.process_numbers_neechivalent2()
    #     self.assertEqual(processor.y, 0)  # y ar trebui să fie scăzut cu 20
    #     self.assertEqual(result, 2 * 10 + 0)  # Așteptăm ca rezultatul să fie 20

    #=====================================================#
    #blackbox testing
    def test_blackbox_case1(self):
        # Test atunci cand 'x' este mai mare decat 10 si 'y' este mai mic decat 20
        np = NumberProcessor(15, 10)
        self.assertEqual(np.process_numbers(), 0)

    def test_blackbox_case2(self):
        # Test atunci cand 'x' este egal cu 10 si 'y' este mai mic deccat 20
        np = NumberProcessor(10, 15)
        self.assertEqual(np.process_numbers(), 55)

    def test_blackbox_case3(self):
        # Test atunci cand 'x' este mai mare decat 10 si 'y' este mai mare sau egal decat 20
        np = NumberProcessor(20, 30)
        self.assertEqual(np.process_numbers(), 30)

    def test_blackbox_case4(self):
        # Test atunci cand 'x' este mai mic sau egal decat 10 si 'y' este mai mic decat 20 si 'x' este par
        np = NumberProcessor(6, 15)
        self.assertEqual(np.process_numbers(), 47)

    def test_blackbox_case5(self):
        # Test atunci cand 'x' este mai mic sau egal decat 10 si 'y' este mai mic decat 20 si 'x' este impar
        np = NumberProcessor(7, 15)
        self.assertEqual(np.process_numbers(), 9)

    def test_blackbox_case6(self):
        # Test atunci cand 'x' este mai mare decat 10 si 'y' este mai mic decat 20 si 'x' este impar
        np = NumberProcessor(17, 15)
        self.assertEqual(np.process_numbers(), 9)

    def test_blackbox_case7(self):
        # Test atunci cand 'x' este mai mare decat 10 si 'y' este mai mic decat 20 si 'x' este par
        np = NumberProcessor(16, 15)
        self.assertEqual(np.process_numbers(), 47)

    def test_blackbox_case8(self):
        # Test atunci cand 'x' este mai mare decat 10 si 'y' este mai mare sau egal decat 20
        np = NumberProcessor(20, 25)
        self.assertEqual(np.process_numbers(), 25)

    
if __name__ == '__main__':
    unittest.main()