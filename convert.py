import xml.etree.ElementTree as ET
import json
import os
import platform

def get_desktop_path():
    system_name = platform.system()
    
    # Получаем путь к рабочему столу
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # Если путь к рабочему столу не существует, используем домашнюю директорию
    if not os.path.exists(desktop_path):
        print(f"Рабочий стол не найден для ОС {system_name}, используется домашняя директория.")
        return os.path.expanduser("~")
    else:
        return desktop_path

def xml_to_dict(xml_file):
    data = []
    for event, elem in ET.iterparse(xml_file, events=("end",)):
        if elem.tag == 'person':
            person_data = {
                "Имя": elem.find('name').text,
                "Возраст": int(elem.find('age').text),
                "Профессия": elem.find('profession').text,
                "Город": elem.find('city').text
            }
            data.append(person_data)
            elem.clear()  # Освобождаем память после обработки элемента
    return data

def save_to_json(data, json_file):
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    desktop_path = get_desktop_path()
    xml_file = os.path.join(desktop_path, 'data.xml')
    json_file = os.path.join(desktop_path, 'data.json')

    # Проверка наличия XML файла
    if not os.path.exists(xml_file):
        print(f"Файл {xml_file} не найден. Поместите XML-файл в каталог и запустите программу снова.")
        return
    
    # Проверка наличия JSON файла
    if os.path.exists(json_file):
        print("Файл data.json уже существует и будет перезаписан.")
    
    # Конвертация XML в JSON
    data = xml_to_dict(xml_file)
    save_to_json(data, json_file)
    print(f"Конвертация завершена. Данные сохранены в {json_file}")

if __name__ == "__main__":
    main()