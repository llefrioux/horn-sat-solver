import difflib
import os
import unittest

# Test suite for script horn-sat-solver.py
class HornSATSolverTest(unittest.TestCase):

   def setUp(self):
      pass

   def launchTestWithRessource(self, inputFile):
      tmpFile = "tmp.file"
      os.system(f"cat {inputFile} | python3 src/horn-sat-solver.py > {tmpFile}")

      outputFile = inputFile[:-2] + "out"
      with open(outputFile) as f1:
         f1_content = f1.readlines()
      with open(tmpFile) as f2:
         f2_content = f2.readlines()
      diff = difflib.unified_diff(f1_content, f2_content)
      self.assertEqual("".join(diff), "")
      os.system(f"rm -f {tmpFile}")

   def test_EmptyClause1(self):
      self.launchTestWithRessource("test/ressources/empty_clause_1.in")

   def test_EmptyClause2(self):
      self.launchTestWithRessource("test/ressources/empty_clause_2.in")

   def test_NegativeLiteralsOnly1(self):
      self.launchTestWithRessource("test/ressources/negative_literals_only_1.in")

   def test_NegativeLiteralsOnly2(self):
      self.launchTestWithRessource("test/ressources/negative_literals_only_2.in")

   def test_OnlyOneNonUnitClause1(self):
      self.launchTestWithRessource("test/ressources/only_one_non_unit_clause_1.in")

   def test_OnlyOneNonUnitClause2(self):
      self.launchTestWithRessource("test/ressources/only_one_non_unit_clause_2.in")
   def test_ShortSAT1(self):
      self.launchTestWithRessource("test/ressources/short_sat_1.in")

   def test_ShortSAT2(self):
      self.launchTestWithRessource("test/ressources/short_sat_2.in")

   def test_ShortUNSAT1(self):
      self.launchTestWithRessource("test/ressources/short_unsat_1.in")

   def test_ShortUNSAT2(self):
      self.launchTestWithRessource("test/ressources/short_unsat_2.in")
   
   def test_MediumSAT1(self):
      self.launchTestWithRessource("test/ressources/medium_sat_1.in")

   def test_MediumSAT2(self):
      self.launchTestWithRessource("test/ressources/medium_sat_2.in")

   def test_MediumUNSAT1(self):
      self.launchTestWithRessource("test/ressources/medium_unsat_1.in")

   def test_MediumUNSAT2(self):
      self.launchTestWithRessource("test/ressources/medium_unsat_2.in")
   
   def test_HugeSAT1(self):
      self.launchTestWithRessource("test/ressources/huge_sat_1.in")

   def test_HugeSAT2(self):
      self.launchTestWithRessource("test/ressources/huge_sat_2.in")

   def test_HugeUNSAT1(self):
      self.launchTestWithRessource("test/ressources/huge_unsat_1.in")

   def test_HugeUNSAT2(self):
      self.launchTestWithRessource("test/ressources/huge_unsat_2.in")

#### MAIN ####

if __name__ == '__main__':
   unittest.main()
