from abc import ABC, abstractmethod
from tkinter import Tk, Label, Entry as TkEntry, Button, Listbox, END

# Інтерфейс для класу "Адреса"
class AddressInterface(ABC):
    @abstractmethod
    def set_address(self, street, city, zip_code):
        pass

    @abstractmethod
    def get_address(self):
        pass

# Клас "Адреса", що реалізує інтерфейс
class Address(AddressInterface):
    def __init__(self, street='', city='', zip_code=''):
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def set_address(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def get_address(self):
        return f'{self.street}, {self.city}, {self.zip_code}'

# Клас "Запис" (перейменований)
class NotebookEntry:
    def __init__(self, name, address: AddressInterface):
        self.name = name
        self.address = address

    def set_address(self, street, city, zip_code):
        self.address.set_address(street, city, zip_code)

    def get_entry(self):
        return f'Name: {self.name}, Address: {self.address.get_address()}'

# Клас "Записна книжка"
class Notebook:
    def __init__(self):
        self.entries = []

    def add_entry(self, name, street, city, zip_code):
        address = Address(street, city, zip_code)
        entry = NotebookEntry(name, address)
        self.entries.append(entry)

    def get_entries(self):
        return [entry.get_entry() for entry in self.entries]

# Клас для графічного інтерфейсу
class NotebookApp:
    def __init__(self, root):
        self.notebook = Notebook()

        # Інтерфейс
        root.title("Записна книжка")

        # Поля для введення імені
        Label(root, text="Ім'я").grid(row=0, column=0)
        self.name_entry = TkEntry(root)
        self.name_entry.grid(row=0, column=1)

        # Поля для введення вулиці
        Label(root, text="Вулиця").grid(row=1, column=0)
        self.street_entry = TkEntry(root)
        self.street_entry.grid(row=1, column=1)

        # Поля для введення міста
        Label(root, text="Місто").grid(row=2, column=0)
        self.city_entry = TkEntry(root)
        self.city_entry.grid(row=2, column=1)

        # Поля для введення поштового індексу
        Label(root, text="Поштовий індекс").grid(row=3, column=0)
        self.zip_entry = TkEntry(root)
        self.zip_entry.grid(row=3, column=1)

        # Кнопка для додавання запису
        self.add_button = Button(root, text="Додати запис", command=self.add_entry)
        self.add_button.grid(row=4, column=1)

        # Список записів
        self.entry_listbox = Listbox(root)
        self.entry_listbox.grid(row=5, column=0, columnspan=2)

    # Функція для додавання запису
    def add_entry(self):
        name = self.name_entry.get()
        street = self.street_entry.get()
        city = self.city_entry.get()
        zip_code = self.zip_entry.get()

        # Додавання запису до записної книжки
        self.notebook.add_entry(name, street, city, zip_code)

        # Оновлення списку
        self.update_listbox()

    # Функція для оновлення списку записів
    def update_listbox(self):
        self.entry_listbox.delete(0, END)
        for entry in self.notebook.get_entries():
            self.entry_listbox.insert(END, entry)

# Створення вікна програми
root = Tk()
app = NotebookApp(root)
root.mainloop()
