import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # 두 번째로 높은 급여 찾기
    second_highest = employee['salary'].drop_duplicates().nlargest(2).iloc[-1] if len(employee['salary'].unique()) > 1 else None
    return pd.DataFrame({'SecondHighestSalary': [second_highest]})