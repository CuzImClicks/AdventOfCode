from typing import Iterable


def print_array(liste: Iterable) -> None:
    print("".join([str(line) + "\n" for line in liste]))

