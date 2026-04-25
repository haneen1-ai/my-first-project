dirty_price = " 1.500 EGP"

step1 = dirty_price.strip()
print(step1)

step2 = step1.replace(".", "").replace(" EGP", "")
print(step2)

result = float(step2)
print(result)
