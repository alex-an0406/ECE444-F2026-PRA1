class utils:
    def reversed(self, number: int) -> int:
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")
        return int(str(number)[::-1])

    def formatter(self, number: int):
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")
        return bin(number), oct(number)