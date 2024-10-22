import csv
from typing import Any, Dict, List, Tuple

## Employee Functions

def employee_count(emp: List) -> int:
    emp_cnt = len(emp)

    return emp_cnt

def male_female_count(emp: List) -> Dict[str, int]:
    male, female = 0, 0
    for row in emp:
        if row['Gender'] == 'Male':
            male += 1
        elif row['Gender'] == 'Female':
            female += 1

    gender_dict = {
        'Male' : male,
    
        'Female' : female
    }

    return gender_dict

def common_job_level(emp: List) -> str:
    
    jobs_and_cnts = {}
    for row in emp:
        jobs_and_cnts[row['JobLevel']] = jobs_and_cnts.get(row['JobLevel'],0) + 1

    max_list = [k for k,v in jobs_and_cnts.items() if v == max(jobs_and_cnts.values())]
    
    return min(max_list)

def highest_score_by_gender(emp: List) -> List[tuple]:
    gender = {'Male':0,'Female':0}

    for row in emp:
        value = float(row['ProblemSolvingScore'])
        if value > float(gender[row['Gender']]):
            gender[row['Gender']] = round(value, 2)

    gender_score = []
    for gender, score in gender.items():
        gender_score.append((score, gender))

    return sorted(gender_score, key=lambda x: (-x[0], x[1]))
    
def analyze_employee_data(filepath: str) -> Tuple[int, dict, str, List[Tuple[float, str]]]:
    """
    Write a code to analyze Employee Performance Data.
    """
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        employee = [row for row in reader]

    return employee_count(employee), male_female_count(employee), common_job_level(employee), highest_score_by_gender(employee)

## Sales Functions

def category_sales(sales: List) -> Dict[str, int]:

    cat_dict = {}
    for row in sales:
        cat_dict[row['ProductCategory']] = cat_dict.get(row['ProductCategory'], 0) + 1
        
    return cat_dict

def average_sale_regions(sales: List) -> Dict[str, float]:

    region_dict = {}
    region_cnt = {}

    for row in sales:
        region_dict[row['SalesRegion']] = float(region_dict.get(row['SalesRegion'], 0)) + float(row['SaleAmount'])
        region_cnt[row['SalesRegion']] = region_cnt.get(row['SalesRegion'], 0) + 1
    for k, v in region_dict.items():
        region_dict[k] = round(v / region_cnt[k], 2)

    return region_dict 

def highest_sale(sales: List) -> float:
    max_sale = 0.0
    for row in sales:
        curr = float(row['SaleAmount'])
        if curr > max_sale:
            max_sale = curr
    
    return round(max_sale, 2)

def highest_sales_products(sales: List) -> list[str]:

    sale_list = []
    max_sale = 0
    for row in sales:
        curr = float(row['SaleAmount'])
        if curr > max_sale:
            max_sale = curr
    for row in sales:
        curr = float(row['SaleAmount'])
        if curr == max_sale:
            sale_list.append(row['ProductID'])
    return sale_list

def analyze_sales_data(filepath: str) -> Tuple[Dict[str, int], Dict[str, float], float, List[str]]:
    """
    Write a code to analyze Sales Data.
    """
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        sales = [row for row in reader]
    
    return (category_sales(sales), average_sale_regions(sales), round(highest_sale(sales), 2), highest_sales_products(sales))

## Bank Functions

def analyze_bank_data(filepath: str) -> Dict[str, Any]:
    """
    Write a code to analyze Bank Transaction Data.
    """
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        bank = [row for row in reader]

    withdrawal, deposit = [], []
    for row in bank:
        if row['TransactionType'] == 'Deposit':
            deposit.append(row['TransactionDescription'].lower())
        if row['TransactionType'] == 'Withdrawal':
            withdrawal.append(row['TransactionDescription'].lower())

    common_list = list(set(deposit) & set(withdrawal))
    deposit_list = list(set(deposit) - set(common_list))
    withdrawal_list = list(set(withdrawal) - set(common_list))

    return {
        'only_deposit' : deposit_list,
        'common' : common_list, 
        'only_withdrawal' : withdrawal_list,
        'exclusive_count' : len(deposit_list) + len(withdrawal_list)
    }