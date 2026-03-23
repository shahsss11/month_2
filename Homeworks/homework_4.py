class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        if len(phone_number) == 10 and phone_number.isdigit():
            return True
        else:
            return False

class ContactList:
    all_contacts = []  

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number) :
            new_contact = Contact(name, phone_number)
            cls.all_contacts.append(new_contact)
        else:
            raise ValueError("Неверный номер телефона! Должно быть 10 цифр.")

ContactList.add_contact("Канат", "0522223568")  
ContactList.add_contact("Артем", "0555323868")  
ContactList.add_contact("Амир", "0555321668")  
ContactList.add_contact("Данил", "0555338608")  
ContactList.add_contact("Байэл", "0555384268")  

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)