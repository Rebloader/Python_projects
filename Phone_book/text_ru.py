menu = ['Главное меню',
        'Открыть файл',
        'Сохранить файл',
        'Показать все контакты',
        'Создать контакт',
        'Найти контакт',
        'Изменить контакт',
        'Удалить контакт',
        'Выход']

input_menu = 'Выберите пункт меню: '
input_menu_error = f'Введите число от 1 до {len(menu)-1} !'


load_successful = 'Телефонная книга успешно загружена !'
save_successful = 'Телефонная книга успешно сохранена !'

empty_book_error = 'Телефонная книга пуста или не открыта !'


def input_contact(new: bool = False):
    add = ' или нажмите "ENTER"' if new else ''

    return [f'Введите имя контакта {add}: ',
            f'Введите номер телефона{add}: ',
            f'Введите комментарий{add}: ']


input_search_word = 'Введите ключевое слово для поиска: '

input_edit_contact_id = 'Введите ID контакта для изменения: '

input_del_contact_id = 'Введите ID контакта, чтобы удалить: '

operation = ['создан', 'изменен', 'удален']

confirm_exit = 'У вас есть несохраненные изменения. Сохранить? (Y / N)'

exit_program = 'Rock\'n\'Roll'

error_message = 'Ошибка при вводе ID!'


def contact_action(name: str, action: str) -> str:
        return f'Контакт "{name}" успешно {action} !!!'


def not_find(word: str) -> str:
        return f'Нет совпадений по заданному слову "{word}" !!! '