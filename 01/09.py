def main():
    # Определяем количество бит в одном байте
    BitsInByte = 8

    # Определяем количество байт в килобайте
    BytesInKilobyte = 1024

    # Рассчитываем количество бит в одном килобайте
    BytesInKilobyte = BitsInByte * BytesInKilobyte

    # Выводим памятку
    print("Памятка для начинающего программиста:")
    print("1 бит - минимальная единица количества информации.")
    print("1 байт = 8 бит.")
    print("1 Килобит = 1024 бита.")
    print("1 Килобайт = 1024 байта.")
    print(f"1 Килобайт = {BytesInKilobyte} бит.")


if __name__ == "__main__":
    main()