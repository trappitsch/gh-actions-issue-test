# define the parsing function run

from ghactmod.app import parse_it

import pytest

IN_OUT = [
    [
        """a
b
c
d
    e""",
        "b\nd",
    ],
    ["a\nb\nc\nd", "b\nd"],
    ["a", ""],
]


@pytest.mark.parametrize("inp, out", IN_OUT)
def test_run(inp, out):
    """Test run function."""
    assert parse_it(inp) == out
