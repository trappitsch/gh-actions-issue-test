# app to parse and return odd lines of input


def run(inp: str) -> None:
    """Parse the input with parse_it and print it.

    :param inp: Input string
    """
    print(parse_it(inp))


def parse_it(inp: str) -> str:
    """Parse input string and return all odd lines.

    :param inp: Input string
    """
    lst = inp.split("\n")
    lst = [it.rstrip() for it in lst]  # sanitize

    out_list = []
    for it, line in enumerate(lst):
        if it % 2 != 0:
            out_list.append(line)

    return "\n".join(out_list)
