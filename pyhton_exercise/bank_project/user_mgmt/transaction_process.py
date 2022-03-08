from bank_server import bank_server
abc_bank = bank_server()
while True:
    abc_bank.deposit_or_withdraw()