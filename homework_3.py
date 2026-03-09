class Person():
    def __init__(self, name, who_is, birth_date, occupation, high_education):
        self.name = name
        self.who_is = who_is
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__education = high_education

    def get_occupation(self):
        return self.__occupation
        
    def get_education(self):
        return self.__education
    
    def show_education(self):
        if self.__education == True:
            return("У меня есть высшее образование")
        else:
            return('У меня нет высшего образования')

    
    def introduce(self):
        return(f'Привет, меня зовут {self.name}, я {self.who_is} Байэля, родился {self.birth_date}, моя профессия {self.get_occupation()}, {self.show_education()}')
    
    
class Friend(Person):
    def __init__(self, name, who_is, birth_date, occupation, hobby, education):
        super().__init__(name, who_is, birth_date, occupation, education)
        self.hobby = hobby

    def introduce(self):
        return(f'Привет, меня зовут {self.name}, я {self.who_is} Байэля, родился {self.birth_date}, моя профессия {self.get_occupation()}, мое хобби {self.hobby}, {self.show_education()}')
    

class Classmate(Person):
    def __init__(self, name, who_is, birth_date, occupation, group_name, education ):
        super().__init__(name, who_is, birth_date, occupation, education)
        self.group_name = group_name

    def introduce(self):
        return (f'Привет, меня зовут {self.name}, я {self.who_is} Байэля, родился {self.birth_date}, моя профессия {self.get_occupation()},  я учусь в группе под номером {self.group_name}, {self.show_education()}')
    

friend = Friend('Артем', 'друг', '29.02.2000', 'программист', 'футбол', True)
print(friend.introduce())

friend = Friend('Данил', 'друг', '23.05.2009', 'инженеро', 'рисование', True)
print(friend.introduce())

classmate = Classmate('Мурат', 'одноклассник', '22.09.2010', 'кассир', '222', False)
print(classmate.introduce())

classmate = Classmate('Семен', 'одноклассник', '11.01.2008', 'официант', '222', False)
print(classmate.introduce())

