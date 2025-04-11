def check_vowels():
    # Código a implementar utilizando input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
    name = input().lower()
    print(f"Contiene a: {'a' in name}")
    print(f"Contiene e: {'e' in name}")
    print(f"Contiene i: {'i' in name}")
    print(f"Contiene o: {'o' in name}")
    print(f"Contiene u: {'u' in name}")
