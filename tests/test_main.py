from main import HelloWord


def test_greeting():
    excepted = "hello Adon!"
    actual = HelloWord(name="Adilson").greetin()
    assert actual == excepted


def test_goodbye():
    excepted = "GoodBye"

    actual = HelloWord(name="Adilson").Goodbye()
    assert actual == excepted
