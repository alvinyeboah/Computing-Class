def eval_loop():
    while True:
        entry = input("Enter your input :")
        if entry == "done":
            print(entry)
            break
        else:
            print(eval(entry))

eval_loop()