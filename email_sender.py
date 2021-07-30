import smtplib
from email.message import EmailMessage

my_dict = {}
my_file = open('addresses.txt', 'r')
for i in range(4):
    roll = my_file.readline()
    nam = my_file.readline()
    name = nam.replace('\n', '')
    my_dict[roll] = name
my_file.close()

for i in range(1, 4):
    key = str(i)+'\n'
    address = my_dict[key]
    print(f'Sending to {address}...')
    email = EmailMessage()
    email['from'] = 'YOUR_NAME'
    email['to'] = address
    email['subject'] = 'Online Class or as you wish'
    email.set_content('  😊 😇 ')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('xyz@gmail.com', 'this emails password')
        smtp.send_message(email)

print('All good boss!')































