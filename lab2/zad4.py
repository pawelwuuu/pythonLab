def is_balanced(expression: str):
    return expression.count("(") == expression.count(")") and expression.count("{") == expression.count("}") and expression.count("[") == expression.count("]")



print(is_balanced("({ } [] []  )"))