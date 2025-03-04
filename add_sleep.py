import os
import re

# Проходим по всем .py файлам в проекте
for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):  # Проверяем, что файл Python
            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:
                content = f.readlines()

            modified = False
            new_content = []
            has_import = any("from time import sleep" in line for line in content)  # Проверяем, есть ли уже импорт

            for line in content:
                new_content.append(line)

                # Ищем строку с self.browser.get(<URL>)
                if re.search(r"self\.browser\.get\(['\"](.+?)['\"]\)", line):
                    print(f"Found 'self.browser.get' in {path}")  # Печатаем, что нашли
                    new_content.append("        sleep(6)\n")  # Добавляем sleep(6) после строки
                    modified = True

            # Если нет импорта time, добавляем его в начало файла
            if modified and not has_import:
                new_content.insert(0, "from time import sleep\n")

            # Если изменения были, записываем их обратно в файл
            if modified:
                with open(path, "w", encoding="utf-8") as f:
                    f.writelines(new_content)
                print(f"Updated: {path}")
