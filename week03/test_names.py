from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown;Sally"
    assert make_full_name("lily", "hernandez") == "hernandez;lily"
    assert make_full_name("john", "cena") == "cena;john"

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Smith; Jane") == "Smith"
    assert extract_family_name("Johnson; James") == "Johnson"
    assert extract_family_name("Doe; John") == "Doe"
    
def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Smith; Jane") == "Jane"
    assert extract_given_name("Johnson; James") == "James"
    assert extract_given_name("Doe; John") == "John"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])