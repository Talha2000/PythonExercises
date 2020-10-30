while True:
    try:
        user = input()
        print((eval(user)))
    except Exception:
        print("Enter an expression to evaluate")
