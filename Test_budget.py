import unittest
from Expense import Expense
from Budget_Services import BudgetService

class TestBudgetService(unittest.TestCase):    
    def setUp(self):        
        self.expenses = [           
             Expense("Lunch", "Food 🍔", 15.0),           
             Expense("Dinner", "Food 🍔", 25.0),           
             Expense("Bus", "Travel 🚌", 10.0)        
             ]   
    def test_categorize_expenses(self):       
         totals = BudgetService.categorize_expenses(self.expenses)        
         self.assertEqual(totals["Food 🍔"], 40.0)        
         self.assertEqual(totals["Travel 🚌"], 10.0)   

    def test_total_spending(self):        
        total = sum(e.amount for e in self.expenses)        
        self.assertEqual(total, 50.0)

if __name__ == "__main__":    
    unittest.main()