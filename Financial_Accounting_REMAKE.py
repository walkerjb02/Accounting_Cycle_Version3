import webbrowser as wb
from Storage import jour
class Main():
    def startup(self):
        while 1:
            check, menu = input('What would you like to do?\n'), {'journal': 'Main().journal()',
                                                                  'trial balance': 'Main().TrialBalance()',
                                                                  'income': 'Main().IncomeAndRetainedEarnings()',
                                                                  'balance': 'Main().BalanceSheet()',
                                                                  'cash': 'Main().CashFlowsStatement()'}
            for i in menu.keys():
                if check in i:
                    print(exec(menu[check]))
    def journal(self):
        with open('Journal.csv', 'a') as journalfile:
            journalfile.write(f'{input("""Date?""")}\n\n\n')
            while not done:
                journal = jour
                category, cattitle, amount = input('Debit or Credit?\n').lower(), input('Category name?\n').lower(), int(input('How much in this category?\n'))
                if 'debit' in category:
                    journalfile.write(f'{cattitle},,,{str(amount)}\n')
                    modified = cattitle.replace(cattitle, 'd' + cattitle)
                else:
                    modified = cattitle.replace(cattitle, 'c' + cattitle)
                    journalfile.write(f',{cattitle},,,{str(amount)}\n')
                for i in journal.keys():
                    if i in modified:
                        journal[i] = journal[i] + amount
                    else: journal[modified] = amount
                check = input('Done?\n').lower()
                if not 'no' in check:
                    with open('Storage.py', 'w') as storage:
                        storage.writelines(f'jour = {journal}\n')
                    done = True
                    wb.open('Journal.csv')
    def TrialBalance(self):
        with open('Trial_Balance.csv', 'a') as tbfile:
            tbfile.write('Trial Balance\n\n\n')
            for i in jour.keys():
                if str(i).startswith('d'):
                    tdebits = sum(jour[i])
                    tbfile.write(f'{str(i).replace(str(i), str(i)[1:])},,{str(jour[i])}\n')
                else:
                    tcredits = sum(jour[i])
                    tbfile.write(f'{str(i).replace(str(i), str(i)[1:])},,,{str(jour[i])}\n')
            tbfile.write(f',,{tdebits},{tcredits}')
            if tcredits == tdebits:
                print('Categories Balance')
            else:
                print('Categories Do Not Balance -- Creating TB Chart!')
                wb.open('Trial_Balance.csv')
    def adjusting_entries(self):
        adjcheck = input('Adj entries y/n?\n').lower()
        if 'y' in adjcheck:
            print(Main().journal())
            print(Main().TrialBalance())
        else: pass
                
    def Statements(self):
        acctgcycle = ['Income_Statement.csv', 'Retained_Earnings.csv', 'Balance_Sheet.csv', 'Cash_Flows.csv']
        for a in acctgcycle:
            with open(f'{a}', 'w') as Statement:
                companyname, revenues, expenses, revenueamounts, expenseamounts, dividends = input('Insert Company Name Here: '), [
                    i[1::] for i in jour.keys() if
                    'revenue' in i or 'sales' in i or 'profit' in i or 'operating' in i], [j[1::] for j in jour.keys() if
                                                                                           'taxes' in j or 'expense' in j or 'cost' in j], [
                                                                                      jour[i] for i in jour.keys() if
                                                                                      'revenue' in i or 'sales' in i or 'profit' in i or 'operating' in i], [
                                                                                      jour[j] for j in jour.keys() if
                                                                                      'taxes' in j or 'expense' in j or 'cost' in j], [sum(jour[i]) for i in jour.keys() if 'dividend' in jour.keys()]
                net = sum(revenueamounts) - sum(expenseamounts)
                if 'Income_Statement.csv' in a:
                    Statement.write(f"""Consolidated Income Statement for {companyname}\n\n\n Revenues\n""")
                    for b, c in revenues, revenueamounts:
                        Statement.write(f'{b},,,{c}\n')
                    Statement.write('Expenses\n')
                    for e, f in expenses, expenseamounts:
                        Statement.write(f',{e},,{f}\n')
                    Statement.write(f'Net Income:,,,{net}')
                elif 'Retained_Earnings.csv' in a:
                    Statement.write(f"""Statement of Retained Earnings for {companyname}\n\n\n Net Income,,,{net}\n{}""")
                elif 'Balance_Sheet.csv' in a:
                    pass
                else:
                    pass
                break
            
Main().startup()
