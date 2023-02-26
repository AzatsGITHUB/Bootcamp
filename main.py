import os


def up_or_lower(string: str, flag=0) -> str:
    """
    Upperize or lowerize a string depending on flag.

    :param string:
    :param flag:
    :return:
    """
    if flag:
        return string.upper()
    else:
        return string.lower()
    # TODO: Azat aga, accept eteniz, otinem.


if __name__ == '__main__':
    case = int(os.environ.get("CASE"))
    print(up_or_lower("Hello world!", case))
