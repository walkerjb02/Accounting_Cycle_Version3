from UDP1 import *
import threading as td

class Menu:
    def __init__(self):
        while 1:
            mcheck = input("\nfin -- Financial Accounting Options"
                           "\nmanagerial -- Managerial Accounting Options"
                           "\nexit -- Exit Program"
                           "\nWhich type of accounting do you want to do?"
                           "\n")

            menudict = {
                'fin' : 'finacctgdict',
                'managerial' : 'managerialacctgdict'
            }

            finacctgdict = {'check': 'tr.trial_balance()', 'journal': 'j.journal_entry()',
                        'adj': 'tr.adjusting_entries()', 'ni': 'f.income_statement()',
                        'ret': 'f.statement_of_retained_earnings()', 'bal': 'f.balance_sheet()',
                        'cash': 'f.statement_of_cash_flows()', 'error': 'e.create_report()',
                        'wri': 't.write_new()', 'ver': 'v.verify()', 'hash': 'Bank'}
            # add in functions
            managerialacctgdict = {

            }
            for i in menudict:
                if i in mcheck and mcheck == 'fin':
                    fincheck = input("Financial Options-----------"
                             "\njournal -- journal entry"
                             "\ncheck -- trial balance | adj -- adjusting entries"
                             "\nni -- net income | ret -- statement of retained earnings | bal -- balance sheet | cash -- statement of cash flows"
                             "\nerror -- error statement | wri -- write new hashbank, storage, etc. | ver -- verify hashes\nWhat do today?\n")
                    for j in fincheck:
                        for f in finacctgdict:
                            if j in f:
                                print(exec(f))
                if i in mcheck and mcheck == 'managerial':
                    mancheck = input('Managerial Choice?\n')
                    for j in mancheck:
                        for m in finacctgdict:
                            if j in m:
                                print(exec(m))
                if mcheck in i and mcheck == 'exit':
                    break
            if mcheck == 'exit':
                break

tr.Thread(target=s.messagereceive).start()
tr.Thread(target=s.connectionestablish).start()
time.sleep(30)
td.Thread(target=Menu).start()


# To do:
# 2. Add managerial accounting component
#   2a. Budgets
#   2b. Mixed costs + graphs + con margin
#   2c. Manufacturing income statements
