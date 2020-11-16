from script import main


def test_main() -> None:
    assert main(["foo"]) == 0, "Expected foo to return 0"
    assert main(["bar"]) == 1, "Expected bar to return 1"


test_main()
