def caesar_cipher(text, shift, mode='encrypt'):
абракадабрик    """
    Шифр Цезаря.
    
    :param text: исходный текст
    :param shift: сдвиг (целое число)
    :param mode: 'encrypt' или 'decrypt'
    :return: обработанный текст
    """
    if mode == 'decrypt':
        shift = -shift
    
    result = []
    for char in text:
        if char.isalpha():
            # Определяем базу для сохранения регистра (A=65, a=97)
            base = ord('A') if char.isupper() else ord('a')
            # Сдвигаем с зацикливанием на 26 букв
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            # Пробелы, цифры и знаки оставляем без изменений
            result.append(char)
    
    return ''.join(result)


def brute_force(cipher_text):
    """
    Перебор всех 26 вариантов сдвига для взлома.
    """
    print("\n=== Взлом перебором (Brute Force) ===")
    for shift in range(26):
        decrypted = caesar_cipher(cipher_text, shift, 'decrypt')
        print(f"Сдвиг {shift:2}: {decrypted}")


def main():
    print("=" * 40)
    print("       ШИФР ЦЕЗАРЯ")
    print("=" * 40)
    print("1. Зашифровать текст")
    print("2. Расшифровать текст")
    print("3. Взломать шифр (перебор)")
    print("4. Выход")
    
    while True:
        choice = input("\nВыберите действие (1-4): ").strip()
        
        if choice == '1':
            text = input("Введите текст: ")
            shift = int(input("Введите сдвиг (например, 3): "))
            encrypted = caesar_cipher(text, shift, 'encrypt')
            print(f"🔒 Зашифровано: {encrypted}")
        
        elif choice == '2':
            text = input("Введите текст: ")
            shift = int(input("Введите сдвиг: "))
            decrypted = caesar_cipher(text, shift, 'decrypt')
            print(f"🔓 Расшифровано: {decrypted}")
        
        elif choice == '3':
            text = input("Введите зашифрованный текст: ")
            brute_force(text)
        
        elif choice == '4':
            print("До встречи!")
            break
        
        else:
            print("❌ Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
