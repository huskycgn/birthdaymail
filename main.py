import pandas
import smtplib
from random import randint
import datetime as dt


def sendmail(addr, text):
    my_email = 'foo@bar.com'
    my_password = 'txenueqjerfqbyrv'
    connection = smtplib.SMTP('smtp.office365.com', 587)
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.ehlo()
    connection.sendmail(from_addr=my_email,
                        to_addrs=addr,
                        msg=f'Subject:Happy Birthday!\n\n\n{text}'
                        )


def get_letter():
    randomint = randint(1, 3)
    with open(file=f'letter_templates/letter_{randomint}.txt') as file:
        letter = file.read()
        return letter


# Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
raw_data = pandas.read_csv('birthdays.csv')
data_dict = raw_data.to_dict(orient='records')

# 2. Check if today matches a birthday in the birthdays.csv

today = dt.datetime.now()

for i in data_dict:
    if (i['month']) == today.month and (i['day']) == today.day:
        templ_letter = get_letter()
        final_letter = templ_letter.replace('[NAME]', i['name'])
        sendmail(i['email'], final_letter)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv


# 4. Send the letter generated in step 3 to that person's email address.
