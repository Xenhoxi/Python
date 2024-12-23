from give_bmi import give_bmi, apply_limit

try:
    height = [2.71, 1.15, 1.72]
    weight = [165.3, 38.4, 64]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 24))
except AssertionError as msg:
    print(msg)
