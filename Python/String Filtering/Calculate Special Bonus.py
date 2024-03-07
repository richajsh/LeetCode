import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus']= employees[(employees.employee_id%2==1)&(~employees['name'].str.startswith('M'))] ['salary']
    df= employees[['employee_id','bonus']].sort_values(by='employee_id').fillna(value=0)
    return df