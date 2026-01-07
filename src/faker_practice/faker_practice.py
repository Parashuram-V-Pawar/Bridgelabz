from faker import Faker
import pandas as pd
import random

fake = Faker(locale="en")
name = fake.name()
print(name)
first_name = fake.first_name()
print(first_name)

print("\nEmployee Data:")

def fake_employee_data(number_of_employees):
    employee_list = []
    for i in range((number_of_employees+1)):
        employee = {}
        employee["First Name"] = fake.first_name()
        employee["Last Name"] = fake.last_name()
        employee["Address"] = fake.address()
        employee["Department"] = fake.random_element(elements=("IT", "Networking", "HR", ))
        employee["Salary"] = fake.random_int(min=30000, max=80000)
        employee["E-mail"] = fake.email()
        employee_list.append(employee)
    return pd.DataFrame(employee_list)
print(fake_employee_data(20))

print("\nIP Addresses:")
def generate_ips(num):
    ips = []
    for i in range(num):
        ip = fake.ipv4_public()
        ips.append(ip)
    return pd.DataFrame(ips)
print(generate_ips(10))


print("\nHTTP status codes:")
def generate_status_codes(num):
    status_codes = []
    for i in range(num):
        code = fake.http_status_code()
        status_codes.append(code)
    return pd.DataFrame(status_codes)
print(generate_status_codes(25))

print("\nLog Data: ")
def generate_log_data(num):
    log_levels = ['INFO', 'WARNING', 'ERROR', 'DEBUG', 'CRITICAL']
    log = []
    for i in range(num):
        log_data = random.choice(log_levels)
        log.append(log_data)
    return pd.DataFrame(log)
print(generate_log_data(20))

print("\nDate time:")
def fake_date_time(num):
    date_times = []
    for i in range(num):
        date_time = {}
        date_time["date"] = fake.date_between(start_date="-20d", end_date="now")
        date_time["time"] = fake.time()
        date_times.append(date_time)
    return pd.DataFrame(date_times)
print(fake_date_time(20))

