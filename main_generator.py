# main_generator.py

import random
from list_utils import find_max, remove_duplicates
# TODO 3: Importiere die Funktionen 'find_max' und 'remove_duplicates'
# aus deinem eigenen Modul 'list_utils'.

def generate_random_numbers(count, min_val, max_val):
    """
    Generiert eine Liste von Zufallszahlen.
    """
    numbers = []
    # TODO 4: Generiere 'count' viele Zufallszahlen zwischen 'min_val' und 'max_val'
    # und füge sie der Liste 'numbers' hinzu. Nutze random.randint().
    for _ in range(count):
        numbers.append(random.randint(min_val, max_val))
    return numbers

if __name__ == "__main__":
    print("Willkommen zum Zufallszahlen-Generator und Listen-Helfer!")

    # TODO 5: Generiere eine Liste mit 10 Zufallszahlen zwischen 1 und 50.
    random_numbers = generate_random_numbers(10, 1, 50)
    print("Generierte Zufallszahlen:", random_numbers)

    # TODO 6: Finde die größte Zahl in der generierten Liste und gib sie aus.
    max_number = find_max(random_numbers)
    print("Größte Zufallszahl:", max_number)

    # TODO 7: Erstelle eine Liste mit Duplikaten zum Testen.
    duplicate_numbers = random_numbers + [random.randint(1, 50) for _ in range(5)]
    print("Liste mit Duplikaten:", duplicate_numbers)

    # TODO 8: Entferne Duplikate aus der Liste und gib die bereinigte Liste aus.
    unique_numbers = remove_duplicates(duplicate_numbers)
    print("Bereinigte Liste ohne Duplikate:", unique_numbers)

    #print("Bitte implementieren Sie die TODOs, um die App zu starten!")