import text_ru as text
from model import PhoneBook


def main_menu():
    for i, item in enumerate(text.menu):
        if i == 0:
            print(item)
        else:
            print(f'\t{i}. {item}')
    while True:
        choice = input(text.input_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.menu):
            return int(choice)
        else:
            print(text.input_menu_error)


def print_massage(msg: str):
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n')


def show_phonebook(book: PhoneBook, msg: str):
    if book:
        print('\n' + '*' * (book.max_len("name") + book.max_len("phone") + book.max_len("comment") + 8))
        for i, contact in book.phone_book.items():
            print(f'{i:>3}. {contact.name:<{book.max_len("name")}} '
                  f'{contact.phone:<{book.max_len("phone")}} '
                  f'{contact.comment:<{book.max_len("comment")}}')
        print('*' * (book.max_len("name") + book.max_len("phone") + book.max_len("comment") + 8) + '\n')
    else:
        print_massage(msg)


def input_contact(msg: list[str]) -> list[str]:
    contact = []
    for text_input in msg:
        contact.append(input(text_input))
    return contact


def input_request(msg: str) -> str:
    return input(msg)
