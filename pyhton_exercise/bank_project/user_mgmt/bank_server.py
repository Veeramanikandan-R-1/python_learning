import datetime
import re, os, json
from common_code import basic_functions
from common_macros import *
import logging,threading

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


class bank_server(basic_functions):
    def __int__(self):
        pass

    def validation(type, value):
        if type == "First_name":
            condition = re.findall('[a-zA-Z0-9]{1,25}', value)
        elif type == 'Lastname':
            condition = re.findall('[a-zA-Z0-9]{0,25}', value)
        elif type == 'Mobile_no':
            user_details = bank_server.read_json(user_detail_json_path)
            condition = re.findall('^(0|91)?[7-9][0-9]{9}$', value)
            if user_details != 'Failure':
                if (value in list(user_details.keys())):
                    print('mobile no already registered')
                    condition = False
        elif type == 'Email_id':
            condition = re.findall('[a-z0-9]{3,25}@gmail.com', value)

        if condition:
            return True
        else:
            return False

    def ask_value(field_name):
        value = input('enter {}'.format(field_name))
        return value

    def add_to_json(new_data):
        if not (user_detail_json_path):
            with open('user_details.json', 'w') as file:
                file.write(json.dumps(new_data))
        else:
            with open('user_details.json', 'r') as file:
                content = bank_server.read_json(user_detail_json_path)
                if content != 'Failure':
                    if content == None:
                        bank_server.write_json(user_detail_json_path, new_data)
                    else:
                        content.update(new_data)
                        bank_server.write_json(user_detail_json_path, content)

                else:
                    bank_server.write_json(user_detail_json_path, new_data)

    def get_user_details(self):
        required_parameters = ['First_name', 'Lastname', 'Mobile_no', 'Email_id', 'Address']
        user_detail = {}
        user_detail1 = {}
        for value in required_parameters:
            user_detail[value] = bank_server.ask_value(value)
            if value != 'Address':
                while not bank_server.validation(value, user_detail[value]):
                    print('Enter valid {}'.format(value))
                    user_detail[value] = bank_server.ask_value(value)
                else:
                    continue
        user_detail['Balance'] = 0
        # user_detail={'First_name': 'mani2', 'Lastname': 'kandan', 'Mobile_no': '9159250701', 'Email_id': 'mani@gmail.com', 'Address': 'chennai'}

        # reading current acc no
        current_acc_no = (bank_server.read_json(account_no_json_path))['account_number']
        user_detail['Account_number'] = current_acc_no

        # incrementing the account number for next iteration
        current_acc_no += 1
        acc_no = {}
        acc_no["account_number"] = current_acc_no
        bank_server.write_json(account_no_json_path, acc_no)

        user_detail1[user_detail['Mobile_no']] = user_detail
        bank_server.add_to_json(user_detail1)

    def validating_acc_info():
        account_no = int(input(('Enter Account no')))
        user_details = bank_server.read_json(user_detail_json_path)
        account_no_registered = [x['Account_number'] for x in user_details.values()]
        while account_no not in account_no_registered:
            print('Enter valid account number')
            account_no = input(('Enter Account no'))
        else:
            for x, y in user_details.items():
                if (y['Account_number'] == account_no):
                    user_detail = user_details[x]
                    print('Confirm details {}'.format(user_detail))
        return user_details, user_detail['Mobile_no']

    def deposit_or_withdraw(self):
        transaction_type = int(input('enter 1 for withdraw or 2 for deposit or 3 for transfer'))
        while transaction_type in [1, 2, 3]:
            break
        else:
            print('enter valid types')
            transaction_type = int(input('enter 1 for withdraw or 2 for deposit or 3 for transfer'))

        if transaction_type != 3:
            user_details_db, mobile_no = bank_server.validating_acc_info()
            # print(user_details_db)
            deposit_or_withdraw_amount = int(input('Enter amount'))
            # print(user_details_db[mobile_no]['Balance'])
            curr_balance = int(user_details_db[mobile_no]['Balance'])
            # print(type(curr_balance))
            if transaction_type == 2:
                curr_balance = curr_balance + int(deposit_or_withdraw_amount)
            elif transaction_type == 1:
                if (curr_balance > deposit_or_withdraw_amount):
                    curr_balance = curr_balance - int(deposit_or_withdraw_amount)
                else:
                    return print('insufficient fund')
            transaction={}
            transaction[user_details_db[mobile_no]['Account_number']]={}
            curr_time=datetime.datetime.now()
            transaction[user_details_db[mobile_no]['Account_number']][curr_time.strftime("%d:%m:%Y-%H:%M:%S")]='{} amount - {} => Available Balance: {}'.format(transaction_type,deposit_or_withdraw_amount,curr_balance)
            user_details_db_old = bank_server.read_json(user_detail_json_path)
            user_details_db[mobile_no]['Balance'] = curr_balance
            user_details_db_old.update(user_details_db)
            bank_server.write_json(user_detail_json_path, user_details_db_old)
            transaction_db=bank_server.read_json(user_transaction_json_path)
            print(transaction_db)
            print(transaction)
            if transaction_db != 'Failure' or None:
                transaction_db.update(transaction)
                bank_server.write_json(user_transaction_json_path,transaction_db)
            else:
                # print((transaction))
                bank_server.write_json(user_transaction_json_path, transaction)
            # print(user_details_db)

        else:
            print('enter sender details')
            user_details, sender_mobile_no = bank_server.validating_acc_info()
            print(user_details)
            print('enter receiver details')
            user_details, receiver_mobile_no = bank_server.validating_acc_info()
            print(user_details)
            while user_details[sender_mobile_no]['Account_number'] != user_details[receiver_mobile_no]['Account_number']:
                break
            else:
                print('sender and receiver cannot be same')
                reciever_user_details_db, receiver_mobile_no = bank_server.validating_acc_info()

            amount=int(input('enter amount to be transferred'))
            if(user_details[sender_mobile_no]['Balance']>amount):
                print('yes')
                user_details[sender_mobile_no]['Balance']-=amount
                user_details[receiver_mobile_no]['Balance'] += amount
            print(user_details)
            user_details_db=bank_server.read_json(user_detail_json_path)
            user_details_db.update(user_details)
            bank_server.write_json(user_detail_json_path,user_details_db)
            print('Trasnferred succesfully')


abc_bank = bank_server()
# user_registration_thread=threading.Thread(target=abc_bank.get_user_details)
# user_registration_thread.start()

while True:
    options = int(input('1 for registration and 2 for transaction 3 for exit'))
    if options == 1:
        abc_bank.get_user_details()
    elif options == 2:
        abc_bank.deposit_or_withdraw()
    elif options == 3:
        break
