def evaluate(choice: str):
    func = globals()[choice]
    func()