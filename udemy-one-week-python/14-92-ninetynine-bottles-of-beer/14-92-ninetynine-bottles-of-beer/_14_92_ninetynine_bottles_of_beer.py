for num in range(99,0,-1):
    print(f"{num} bottle(s) of beer on the wall.")
    print(f"{num} bottle(s) of beer.")
    last_line = "Takeonedown, pass it around, "
    remaining = num - 1
    if (remaining > 0): 
        last_line += f"{remaining} bottle(s) of beer on the wall."
    else:
        last_line += "no more bottles of beer on the wall"
    print(last_line)
    print("*" * 100)

