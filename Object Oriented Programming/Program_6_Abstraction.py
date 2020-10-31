class Person:
    def __init__(self, name, surname, year_of_birth):
        self._name = name
        self._surname = surname
        self._year_of_birth = year_of_birth

    def age(self, current_year):
        return current_year - self._year_of_birth

    def __str__(self):
        return "%s %s and was born %d." \
               % (self._name, self._surname, self._year_of_birth)


alec = Person("Karam", "G", 1997)
print(alec)
print(alec._surname)  # _Protect your abstraction


class Person:
    def __init__(self, name, surname, year_of_birth):
        self.__name = name  # Protect your abstraction
        self.__surname = surname
        self.__year_of_birth = year_of_birth

    def age(self, current_year):
        return current_year - self.__year_of_birth

    def __str__(self):
        return "%s %s and was born %d." % (self.__name, self.__surname, self.__year_of_birth)


alec = Person("Karam", "G", 1997)
print(alec._Person__name)  # We can see that prepending two underscores every key has _ClassName__ prepended.