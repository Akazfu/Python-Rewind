class Asciint(int):
    def __new__(cls, usr_input):
        if isinstance(usr_input, str):
            sum_ascii = 0
            for i in usr_input:
                sum_ascii += ord(i)
            usr_input = sum_ascii
        return int.__new__(cls, usr_input)


print(Asciint(123))
print(Asciint(1.5))
print(Asciint('A'))
print(Asciint('FishC'))
