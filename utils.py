class utils:
    #returns the reversed integer of the input
    def reversed(self, number: int) -> int:
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")
        return int(str(number)[::-1])
#returns int as binary and octal representation of the input
    def formatter(self, number: int):
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")
        return bin(number), oct(number)