import unittest
import pandas as pd
import dropna_merge_practice_quiz as quiz_script

class TestDataProcessing(unittest.TestCase):

   
    df_left = pd.DataFrame({
            'Name': ['Anna', 'Brad', 'Charlie', 'Diana'],
            'Age': ['28', '35', '23', '31'],
            'Salary': ['54000', '68000', '59000', '77000']
    })

    df_right = pd.DataFrame({
            'Employee_Name': ['Anna', 'Brad', 'Charlie', 'Diana'],
            'Department': ['Sales', 'HR', 'Marketing', 'Finance'],
            'Location': ['Berlin', 'Paris', 'London', 'New York']
    })

    df_with_missing = pd.DataFrame({
            'Name': ['Anna', 'Brad', None, 'Diana'],
            'Age': ['28', None, None, '23'],
            'Salary': [None, '68000', None, '77000']
    })

    def test_drop_all_missing(self):
        result = quiz_script.drop_all_missing(self.df_with_missing)
        # Manually create expected DataFrame
        expected = pd.DataFrame({
            'Name': ['Anna', 'Brad', 'Diana'],
            'Age': ['28', None, '23'],
            'Salary': [None, '68000', '77000']
        }, index = [0,1,3])
        pd.testing.assert_frame_equal(result, expected)

    def test_drop_any_missing(self):
        result = quiz_script.drop_any_missing(self.df_with_missing)
        # Manually create expected DataFrame
        expected = pd.DataFrame({
            'Name': 'Diana',
            'Age': '23',
            'Salary': '77000'
        }, index = [3])
        pd.testing.assert_frame_equal(result, expected)

    def test_find_salary_sum(self):
        result = quiz_script.find_salary_sum(self.df_left)
        # Manually calculate the expected sum
        expected = 258000
        self.assertEqual(result, expected)

    def test_merge_dataframes(self):
        result = quiz_script.merge_dataframes(self.df_left, self.df_right)
        # Manually create expected DataFrame
        expected = pd.DataFrame({
            'Name': ['Anna', 'Brad', 'Charlie', 'Diana'],
            'Age': ['28', '35', '23', '31'],
            'Salary': ['54000', '68000', '59000', '77000'],
            'Department': ['Sales', 'HR', 'Marketing', 'Finance'],
            'Location': ['Berlin', 'Paris', 'London', 'New York']
        })
        pd.testing.assert_frame_equal(result, expected)

# Make sure the following is at the end of your script
if __name__ == '__main__':
    unittest.main()
