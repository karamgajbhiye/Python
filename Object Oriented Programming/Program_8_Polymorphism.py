class India():
    def Currency(self):
        print("Indian rupee")

    def language(self):
        print("Hindi and English")


class USA():
    def Currency(self):
        print("United States Dollar")

    def language(self):
        print("English")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.Currency()
country.language()