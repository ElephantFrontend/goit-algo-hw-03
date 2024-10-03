import os
import shutil
import argparse

# Функція для рекурсивного копіювання файлів та сортування за розширеннями
def copy_and_sort_files(source_dir, dest_dir):
    try:
        # Перевірка, чи існує директорія призначення, якщо ні — створити її
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Перебір всіх елементів у вихідній директорії
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)
            
            # Якщо елемент є директорією, рекурсивно обробляємо її
            if os.path.isdir(source_path):
                copy_and_sort_files(source_path, dest_dir)
            else:
                # Отримуємо розширення файлу
                file_extension = os.path.splitext(item)[1].lstrip('.').lower()  # Отримати розширення файлу
                if not file_extension:
                    file_extension = 'no_extension'  # Якщо файл без розширення

                # Створюємо піддиректорію для файлів з таким розширенням
                dest_subdir = os.path.join(dest_dir, file_extension)
                if not os.path.exists(dest_subdir):
                    os.makedirs(dest_subdir)

                # Копіюємо файл у відповідну піддиректорію
                dest_path = os.path.join(dest_subdir, item)
                shutil.copy2(source_path, dest_path)  # Копіює файл разом з метаданими (час створення тощо)
                print(f"Копіювання {source_path} до {dest_path}")
    
    except Exception as e:
        print(f"Помилка: {e}")

# Функція для парсингу аргументів командного рядка
def parse_arguments():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширеннями.")
    parser.add_argument('source_dir', help="Шлях до вихідної директорії")
    parser.add_argument('dest_dir', nargs='?', default='dist', help="Шлях до директорії призначення (за замовчуванням: dist)")
    return parser.parse_args()

# Основна функція
def main():
    # Парсинг аргументів
    args = parse_arguments()
    source_dir = args.source_dir
    dest_dir = args.dest_dir

    # Перевірка, чи існує вихідна директорія
    if not os.path.exists(source_dir):
        print(f"Директорія {source_dir} не існує.")
        return

    # Виклик функції для копіювання файлів
    copy_and_sort_files(source_dir, dest_dir)
    print("Копіювання завершено.")

if __name__ == "__main__":
    main()
