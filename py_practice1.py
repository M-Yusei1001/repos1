from func_practice import Formula

rb = Formula("Redbull_Honda")

print(rb.name)

for i in range(1,3):
    print(str(i) + ". "+ rb.driver_name(i) + ":" + str(rb.driver_number(i)))