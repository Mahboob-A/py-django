# 150125, Wednesday, 08.00 AM
# https://realpython.com/python-type-checking/#type-systems


# headlines.py


def headline(text: str, centered: bool = False) -> str:
    if not centered:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")

        


print(headline("python type checking"))
print(headline("use mypy", centered=True)) # Correct 
print(headline("use mypy", centered="True")) # for mypy, the type of centered is bool, not str
# for mypy type checking, run as: mypy filename.py

