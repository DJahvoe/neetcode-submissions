class Singleton:
    instance = None

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls.instance == None:
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


    def getValue(self) -> str:
        return self.val

    def setValue(self, value: str):
        self.val = value
