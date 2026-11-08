from datetime import date
from decimal import Decimal, ROUND_HALF_UP

employees = [
    # Engineering: 3 คน เงินเดือนรวมหารสามไม่ลงตัว
    {"id": 1, "name": "Somchai",  "department": "Engineering", "salary": Decimal("55000.00"), "hire_date": date(2019, 3, 15)},
    {"id": 2, "name": "Malee",    "department": "Engineering", "salary": Decimal("62000.50"), "hire_date": date(2021, 11, 7)},
    {"id": 3, "name": "Anan",     "department": "Engineering", "salary": Decimal("48000.00"), "hire_date": date(2021, 11, 8)},
    # Sales: 2 คน ค่าเฉลี่ยลงที่ครึ่งสตางค์พอดี
    {"id": 4, "name": "Pimchai",  "department": "Sales",       "salary": Decimal("40000.00"), "hire_date": date(2020, 2, 29)},
    {"id": 5, "name": "Wichai",   "department": "Sales",       "salary": Decimal("40000.01"), "hire_date": date(2023, 6, 1)},
    # Finance: 2 คน ค่าเฉลี่ยลงตัว
    {"id": 6, "name": "Suda",     "department": "Finance",     "salary": Decimal("70000.00"), "hire_date": date(2015, 1, 12)},
    {"id": 7, "name": "Niran",    "department": "Finance",     "salary": Decimal("71000.00"), "hire_date": date(2018, 9, 30)},
    # HR: คนเดียวในแผนก
    {"id": 8, "name": "Kanda",    "department": "HR",          "salary": Decimal("38500.75"), "hire_date": date(2022, 4, 20)},
]

def group_by_department(employees: list[dict]) -> dict[str, list[dict]]:
    depart_group = {}
    for emp in employees:
        depart_group[emp["department"]] = depart_group.get(emp["department"], [])
        depart_group[emp["department"]].append(emp)
    return depart_group
    
def average_salary_by_department(employees: list[dict]) -> dict[str, Decimal]:
    depart_group = group_by_department(employees)
    depart_salary = {department: (sum(emp["salary"] for emp in members) / len(members)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP) for department, members in depart_group.items() }
    return depart_salary

def full_years_between(start: date, end: date) -> int:
    full_years = end.year - start.year
    if ((end.month, end.day) < (start.month, start.day)):
        full_years -=1
    return full_years
    
def find_senior_employees(employees: list[dict], min_years: int, today_date: date) -> list[dict]:
    return [emp for emp in employees if full_years_between(emp["hire_date"], today_date) >= min_years]
    
def get_employee(employees: list[dict], emp_id: int) -> dict:
    for emp in employees:
        if "id" in emp and emp["id"] == emp_id:
            return emp
    raise LookupError(f"No Employee Id: {emp_id} found.")
    
today = date(2026, 11, 7)
snapshot = list(employees)
grouped_depart = group_by_department(employees)

assert len([department for department, members in grouped_depart.items()]) == 4
assert [emp["name"] for emp in grouped_depart["Engineering"]] == ["Somchai","Malee", "Anan"]
assert [emp["name"] for emp in grouped_depart["Sales"]] == ["Pimchai","Wichai"]
assert [emp["name"] for emp in grouped_depart["Finance"]] == ["Suda","Niran"]
assert [emp["name"] for emp in grouped_depart["HR"]] == ["Kanda"]

try:
    grouped_depart["Marketing"]
except KeyError as e:
    assert "Marketing" in str(e)
else:
    raise AssertionError("expected KeyError was not raised")

empty_grouped_depart = group_by_department([])
assert empty_grouped_depart == {}


avg_depart = average_salary_by_department(employees)
assert avg_depart["Engineering"] == Decimal("55000.17")
assert avg_depart["Sales"] == Decimal("40000.01")
assert avg_depart["Finance"] == Decimal("70500.00")
assert avg_depart["HR"] == Decimal("38500.75")


empty_avg_depart = average_salary_by_department([])
assert empty_avg_depart == {}

assert len(find_senior_employees(employees, 0, today)) == 8
assert len(find_senior_employees(employees, 5, today)) == 5
assert [emp["id"] for emp in find_senior_employees(employees, 5, today)] == [1, 2, 4, 6, 7]
assert len(find_senior_employees(employees, 6, today)) == 4
assert len(find_senior_employees(employees, 10, today)) == 1
assert len(find_senior_employees(employees, 5, date(2020, 1, 13))) == 1
assert len(find_senior_employees(employees, 7, date(2027, 2, 28))) == 3
assert len(find_senior_employees(employees, 7, date(2027, 3, 1))) == 4
assert 4 not in [emp["id"] for emp in find_senior_employees(employees, 7, date(2027, 2, 28))]
assert 4 in [emp["id"] for emp in find_senior_employees(employees, 7, date(2027, 3, 1))]
assert find_senior_employees([], 5, today) == []

assert get_employee(employees, 1)["name"] == "Somchai"
try:
    get_employee(employees, 111)
except LookupError as e:
    assert "111" in str(e)
else:
    raise AssertionError("expected LookupError was not raised")
try:
    avg_depart["Marketing"]
except KeyError as e:
    assert "Marketing" in str(e)
else:
    raise AssertionError("expected KeyError was not raised")


try:
    found_emp = get_employee([{"name": "Somchaix",  "department": "Engineering", "salary": Decimal("55000.00"), "hire_date": date(2019, 3, 15)},
                                {"id": 1, "name": "Somchai",  "department": "Engineering", "salary": Decimal("55000.00"), "hire_date": date(2019, 3, 15)}], 1)
    assert found_emp["id"] == 1
except LookupError as e:
    assert "1" in str(e)
assert employees == snapshot