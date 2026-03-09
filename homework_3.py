class Person():
    def __init__(self, name, who_is, birth_date, occupation):
        self.name = name
        self.who_is = who_is
        self.birth_date = birth_date
        self.occupation = occupation

    def introduce(self):
        return(f'Привет, меня зовут {self.name}, я {self.who_is} Байэля, родился {self.birth_date}, работаю {self.occupation}')
    
class Friend(Person):
    def __init__(self, name, who_is, birth_date, occupation, hobby):
        super().__init__(name, who_is, birth_date, occupation,)
        self.hobby = hobby

    def introduce(self):
        return(f'Привет, меня зовут {self.name}, я {self.who_is} Байэля, родился {self.birth_date}, работаю {self.occupation}, мое хобби {self.hobby}')
    

class Classmate(Person):
    def __init__(self, name, who_is, birth_date, occupation, group_name):
        super().__init__(name, who_is, birth_date, occupation)
        self.group_name = group_name

    def introduce(self):
        return f'Привет, меня зовут {self.name}, я {self.who_is} Байэля, родился {self.birth_date}, работаю {self.occupation}, я учусь в группе под номером {self.group_name}'
    

friend = Friend('Артем', 'друг', '29.02.2000', 'программистом', 'футбол')
print(friend.introduce())

friend = Friend('Данил', 'друг', '23.05.2009', 'инженером', 'рисование')
print(friend.introduce())

classmate = Classmate('Мурат', 'одноклассник', '22.09.2010', 'кассиром', '222')
print(classmate.introduce())

classmate = Classmate('Семен', 'одноклассник', '11.01.2008', 'официантом', '222')
print(classmate.introduce())

