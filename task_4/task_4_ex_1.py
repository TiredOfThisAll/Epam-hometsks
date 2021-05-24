"""04 Task 1.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa. The
function should return modified string.
Usage of any replacing string functions is prohibited.
"""


def swap_quotes(string: str) -> str:
    replaced_expression = []
    for i in string:
        if i == '"':
            replaced_expression.append("'")
            continue
        elif i == "'":
            replaced_expression.append('"')
            continue
        replaced_expression.append(i)
    return "".join(replaced_expression)
