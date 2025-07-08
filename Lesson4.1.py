from pathlib import Path

def total_salary(path):
    file_name = Path(path)
    total = 0
    count = 0

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    name, month_salary = line.split(',')
                    month_salary = int(month_salary)
                    print(f'Name: {name}/ Salary: {month_salary}')
                    total += month_salary
                    count += 1
                except ValueError:
                    print('The file has invalid data')
        average = total / count if count >0 else 0
        return (total, average)

    except FileNotFoundError:
        print('Unfortunatelly, your file is not found')
    except Exception as e:
        print(f'{e} with file')
        return 0,0


total, average = total_salary('salary.txt')
print(f'Total month salary: {total}, Average month salary: {average:.0f}')