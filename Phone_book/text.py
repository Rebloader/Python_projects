
menu = ['Main menu',
        'Open file',
        'Save file',
        'Show contacts',
        'Create contact',
        'Find contact',
        'Change contact',
        'Delete contact',
        'Exit']

input_menu = 'Select menu option: '
input_menu_error = f'Input number between 1 and {len(menu)-1} !'


load_successful = 'Phonebook loaded successfully !!!'
save_successful = 'Changes in Phonebook saved successfully !!!'

empty_book_error = 'Phonebook is empty or unopened !!!'


def input_contact(new: bool = False):
    add = ' or click "ENTER"' if new else ''

    return [f'Input name {add}: ',
            f'Input phone number{add}: ',
            f'Input comment{add}: ']


input_search_word = 'Input keyword for search: '

input_edit_contact_id = 'Input contact\'s ID for changes: '

input_del_contact_id = 'Input contact\'s ID for delete: '

operation = ['created', 'changed', 'deleted']

confirm_exit = 'You have unsaved changes! Save changes? (Y / N)'

exit_program = 'Rock\'n\'Roll'

error_message = 'Error, check input ID!'


def contact_action(name: str, action: str) -> str:
        return f'Contact "{name}" successfully {action} !!!'


def not_find(word: str) -> str:
        return f'No match found for "{word}" !!! '
