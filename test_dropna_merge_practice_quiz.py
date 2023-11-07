import unittest
import pandas as pd
from dropna_merge_practice_quiz import drop_all_missing, drop_any_missing, find_salary_sum, merge_dataframes

class TestDataProcessing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df_left = pd.DataFrame({
            'Name': ['Anna', 'Brad', 'Charlie', 'Diana'],
            'Age': [28, 35, 23, 31],
            'Salary': [54000, 68000, 59000, 77000]
        })

        cls.df_right = pd.DataFrame({
            'Employee_Name': ['Anna', 'Brad', 'Charlie', 'Diana'],
            'Department': ['Sales', 'HR', 'Marketing', 'Finance'],
            'Location': ['Berlin', 'Paris', 'London', 'New York']
        })

        cls.df_with_missing = pd.DataFrame({
            'Name': ['Anna', 'Brad', None, 'Diana'],
            'Age': [28, None, 23, None],
            'Salary': [None, 68000, None, 77000]
        })

    def test_drop_all_missing(self):
        result = drop_all_missing(self.df_with_missing)
        # Expected DataFrame should not contain any row or column with all missing values
        expected = self.df_with_missing.dropna(how='all')
        pd.testing.assert_frame_equal(result, expected)

    def test_drop_any_missing(self):
        result = drop_any_missing(self.df_with_missing)
        # Expected DataFrame should not contain any row or column with any missing values
        expected = self.df_with_missing.dropna(how='any')
        pd.testing.assert_frame_equal(result, expected)

    def test_find_salary_sum(self):
        result = find_salary_sum(self.df_left)
        # The sum should be the sum of the 'Salary' column
        expected = self.df_left['Salary'].sum()
        self.assertEqual(result, expected)

    def test_merge_dataframes(self):
        result = merge_dataframes(self.df_left, self.df_right)
        # Expected DataFrame should be the merge of df_left and df_right without duplicate columns
        expected = pd.merge(self.df_left, self.df_right, left_on='Name', right_on='Employee_Name').drop(columns=['Employee_Name'])
        pd.testing.assert_frame_equal(result, expected)

# Make sure the following is at the end of your script
if __name__ == '__main__':
    unittest.main()
