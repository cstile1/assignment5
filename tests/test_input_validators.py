import pytest
from app.input_validators import parse_two_floats

def test_parse_ok():
    assert parse_two_floats(["add","2","3"]) == (2.0, 3.0)

@pytest.mark.parametrize("tokens", [
    (["add","x","3"]), (["add","2","y"]), (["add","2"]), (["add"])
])
def test_parse_bad(tokens):
    with pytest.raises(Exception):
        parse_two_floats(tokens)
