import webbrowser as wb
from Storage import jour
class Main():
    def journal(self):
        with open('Journal.csv', 'a') as journalfile:
            journalfile.write(f'{input("""Date? """)}\n\n\n')
            done = False
            while done == False:
                category, cattitle, amount = input('Debit or Credit?\n').lower(), input('Category name?\n').lower(), int(input('How much in this category?\n'))
                if 'debit' in category:
                    journalfile.write(f'{cattitle},,,{str(amount)}\n')
                    modified = cattitle.replace(cattitle, 'd' + cattitle)
                else:
                    modified = cattitle.replace(cattitle, 'c' + cattitle)
                    journalfile.write(f',{cattitle},,,{str(amount)}\n')
                jour[modified] = amount
                for i in jour.keys():
                    if i in modified:
                        jour[i] = jour[i] + amount
                check = input('Done?\n').lower()
                if not 'no' in check:
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
    def IncomeAndRetainedEarnings(self):
        with open('Income_Statement.csv', 'a') as IncomeFile:
            pass
        with open('Retained_Earnings.csv', 'a') as Retfile:
            pass
    def BalanceSheet(self):
        with open('Balance_Sheet.csv', 'a') as BalanceFile:
            pass
    def CashFlowsStatement(self):
        with open('Cash_Flows.csv', 'a') as CashFile:
            pass
