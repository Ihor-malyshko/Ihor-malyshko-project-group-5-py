from bot import AddressBook, Record  # Заміни 'bot_done' на назву свого файла, якщо потрібно

def run_tests():
    book = AddressBook()

    print("=== Test 1: Додавання контакту ===")
    john = Record("John")
    john.add_address("Kyiv")
    john.add_phone("1234567890")
    john.add_email("john@example.com")
    john.add_birthday("15.07.1990")
    book.add_record(john)

    record = book.find("John")
    assert record is not None, "❌ Record 'John' not found"
    assert record.address.value == "Kyiv"
    assert record.phones and record.phones[0].value == "1234567890"
    assert record.emails and record.emails[0].value == "john@example.com"
    assert str(record.birthday) == "15.07.1990"
    print("✅ Test 1 passed")

    print("=== Test 2: Редагування номера телефону ===")
    record.phones = []  # Очистити старі
    record.add_phone("9999999999")
    assert record.phones[0].value == "9999999999"
    print("✅ Test 2 passed")

    print("=== Test 3: Пошук за іменем (частковий) ===")
    found = [r for r in book.data.values() if "jo" in r.name.value.lower()]
    assert len(found) == 1 and found[0].name.value == "John"
    print("✅ Test 3 passed")

    print("=== Test 4: Пошук за телефоном ===")
    search_phone = "9999999999"
    matched = False
    for rec in book.data.values():
        if any(p.value == search_phone for p in rec.phones):
            matched = True
            break
    assert matched, "❌ Phone not found"
    print("✅ Test 4 passed")

    print("=== Test 5: Видалення контакту ===")
    book.delete("John")
    assert book.find("John") is None
    print("✅ Test 5 passed")

    print("\n🎉 Усі тести пройшли успішно!")

if __name__ == "__main__":
    run_tests()