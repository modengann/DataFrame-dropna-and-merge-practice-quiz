import pandas as pd

#drops any rows or columns where ALL data is missing and returns the dataframe
def drop_all_missing(df):
    # Your code here
    pass

#drops any rows or columns where ANY data is missing and returns the dataframe
def drop_any_missing(df):
    # Your code here
    pass

#Takes in teh demographic data DataFrame, returns the sum of the salary
def find_salary_sum(df):
    # Your code here
    pass

#Merge two dataframes based on a common feature
#Returns a dataframe where with any duplicate columns (i.e. same data) removed
def merge_dataframes(df_left, df_right):
    # Your code here
    pass


def main():
    #csv data loaded
    salary_data = pd.read_csv("hr_demographic_data.csv")
    job_description = pd.read_csv("hr_job_description.csv")



    print(f"The total spent on salaries is {find_salary_sum(salary_data)}")
    merged_data = merge_dataframes(salary_data, job_description)
    only_complete_data = drop_any_missing(merged_data)




    

if __name__ == "__main__":
        main()