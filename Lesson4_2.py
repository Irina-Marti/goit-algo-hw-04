from pathlib import Path

def get_cats_info(path):
    file_name = Path(path)
    cats_info = []

    try:
        with open(file_name, "r", encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                cat_id, name, age = line.split(',')
                cats_info.append({'id':cat_id, 'name': name, 'age': age})
        return cats_info

    except FileNotFoundError:
        print('Unfortunatelly, your file is not found')
    except Exception as e:
        print(f'{e} with file')


cats = get_cats_info('cats.txt')
for cat in cats:
    print(cat)
