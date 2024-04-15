import unittest
import ChomskyNormalForm, Variants


class UnitTestCNF(unittest.TestCase):
    def test_ChomskyNormalForm_variant1(self):
        grammar_to_ChomskyNormalForm_test = ChomskyNormalForm.Grammar(Variants.Vn1, Variants.Vt1, Variants.P1).to_ChomskyNormalForm()
        dict_to_verify = {'S': ['AC', 'EC', 'BC', 'AS', 'a', 'FB', 'FD'],
                          'A': ['GS', 'EC', 'b', 'AS', 'BC', 'a', 'FD'],
                          'B': ['b', 'GS'],
                          'C': ['BA'],
                          'D': ['HC', 'FG'],
                          'E': ['AS'],
                          'F': ['a'],
                          'G': ['b'],
                          'H': ['FG']}
        for key in grammar_to_ChomskyNormalForm_test.keys():
            grammar_to_ChomskyNormalForm_test[key] = set(grammar_to_ChomskyNormalForm_test[key])
            dict_to_verify[key] = set(dict_to_verify[key])
        self.assertDictEqual(grammar_to_ChomskyNormalForm_test, dict_to_verify)

    def test_ChomskyNormalForm_variant2(self):
        grammar_to_ChomskyNormalForm_test = ChomskyNormalForm.Grammar(Variants.Vn2, Variants.Vt2, Variants.P2).to_ChomskyNormalForm()
        dict_to_verify = {'S': ['CB', 'EA', 'b'],
                          'A': ['GB', 'CB', 'EB', 'AS', 'CD', 'ES', 'b', 'FB', 'EA'],
                          'B': ['b', 'ES'],
                          'D': ['BB'], 'C': ['a'],
                          'E': ['b'], 'F': ['EA'],
                          'G': ['FA']}
        for key in grammar_to_ChomskyNormalForm_test.keys():
            grammar_to_ChomskyNormalForm_test[key] = set(grammar_to_ChomskyNormalForm_test[key])
            dict_to_verify[key] = set(dict_to_verify[key])
        self.assertDictEqual(grammar_to_ChomskyNormalForm_test, dict_to_verify)

    def test_chomsky_for_variant3(self):
        grammar_to_ChomskyNormalForm_test = ChomskyNormalForm.Grammar(Variants.Vn3, Variants.Vt3, Variants.P3).to_ChomskyNormalForm()
        dict_to_verify = {'S': ['GB', 'DS', 'd', 'DB'],
                          'A': ['d', 'DS', 'GB'],
                          'B': ['CS', 'DS', 'GB', 'a', 'd'],
                          'C': ['a'], 'D': ['d'],
                          'E': ['CA'],
                          'F': ['ED'],
                          'G': ['FA']}
        for key in grammar_to_ChomskyNormalForm_test.keys():
            grammar_to_ChomskyNormalForm_test[key] = set(grammar_to_ChomskyNormalForm_test[key])
            dict_to_verify[key] = set(dict_to_verify[key])
        self.assertDictEqual(grammar_to_ChomskyNormalForm_test, dict_to_verify)


if __name__ == "__main__":
    unittest.main()
