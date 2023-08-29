import requests
import random
import string
import time
import os

API = 'https://www.1secmail.com/api/v1/'
domain_list = [
    "1secmail.com",
    "1secmail.org",
    "1secmail.net",
    "wwjmp.com"
    ]
domain = random.choice(domain_list)


def generate_name():
    name = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(name) for i in range(10))

    return username


def check_mail(mail=''):
    req_link = f'{API}?action=getMessages&login={mail.split("@")[0]}&domain={mail.split("@")[1]}'
    r = requests.get(req_link).json()
    length = len(r)

    if length == 0:
        print('[INFO] No unread messages for now')
    else:
        id_list = []

        for i in r:
            for key, value in i.items():
                if key == 'id':
                    id_list.append(value)
        
        print(f'[+] You have {length} new messages!')

        current_dir = os.getcwd()
        final_dir = os.path.join(current_dir, 'all_mails')

        if not os.path.exists(final_dir):
            os.makedirs(final_dir)

        for id in id_list:
            read_msg = f'{API}?action=readMessage&login={mail.split("@")[0]}&domain={mail.split("@")[1]}&id={id}'
            r = requests.get(read_msg).json()

            sender = r.get('from')
            subject = r.get('subject')
            date = r.get('date')
            text = r.get('textBody')

            mail_file_path = os.path.join(final_dir, f'{id}.txt')

            with open(mail_file_path, 'w', encoding='UTF-8') as file:
                file.write(f'Sender: {sender}\nTo: {mail}\nSubject: {subject}\nDate: {date}\nText: {text}')


def delete_mail(mail=''):
    url = 'https://www.1secmail.com/mailbox'

    data = {
        'action': 'deleteMailbox',
        'login': mail.split('@')[0],
        'domain': mail.split('@')[1]
    }

    r = requests.post(url, data=data)
    print(f'[X] Email adres {mail} - Deleted!\n')


def main():
    try:
        username = generate_name()
        mail = f'{username}@{domain}'
        print(f'[+] Your email adres is: {mail}')

        mail_req = requests.get(f'{API}?login={mail.split("@")[0]}&domain={mail.split("@")[1]}')

        while True:
            check_mail(mail=mail)
            time.sleep(5)
    
    except(KeyboardInterrupt):
        delete_mail(mail=mail)
        print('Programm closed')



if __name__ == '__main__':
    main()