def get_str(st, i=0):

    result = ""
    num = ""

    while i < len(st):
        if 'a' <= st[i] <= 'z' or 'A' <= st[i] <= 'Z' or st[i] == ' ':  # is letter or space
            result += st[i]
        elif st[i] == '[':                                              # k[string]
            temp = get_str(st, i + 1)
            result += temp * int(num)                                   # recursion
            i += len(temp) + 2
            num = ""
        elif st[i] == ']':                                              # end string
            return result
        else:                                                           # is num
            num += st[i]

        i += 1

    return result                                                       # end string


def get_exception():
    """
    some code:
    ...
    ...
    ...
    """

    raise 1
