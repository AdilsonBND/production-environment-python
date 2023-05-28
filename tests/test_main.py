from src.main import HelloWorld


def test_greeting():
    expected = "Hello Adilson!"
    actual = HelloWorld(name="Adilson").greeting()
    assert actual == expected


def test_goodbye():
    expected = "Goodbye!"
    actual = HelloWorld(name="adilson").Goodbye()
    assert actual == expected
