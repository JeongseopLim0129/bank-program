class BankAccount:
    def open_account():
        print('\n[계좌개설]')
        try:
            a = int(input('계좌ID:(숫자로 입력)'))
        except ValueError:
            print('숫자만 입력하세요')
            return
        try:
            amount = int(input('입금액: '))
        except:
            print('숫자만 입력하세요')
            return
        
        accounts[a][0] = [input('이름: ')]
        accounts[a][1] = amount

    def deposit():
        for i in accounts.keys():
            if i == deposit_id:
                accounts[i][1] += deposit_amount

        print('입금완료')
            
    def withdrawal():
        for i in accounts.keys():
            if i == withdrawal_id:
                accounts[i][1] -= withdrawal_amount

        print('출금완료')

    def print_all_account():
        for key in accounts:
            print()
            print('계좌ID: {}\n이름: {}\n잔액: {}'.format(key, accounts[key][0], accounts[key][1]))
            

accounts = {}

i = 0
while i != 5:
    print('-----MENU-----\n1. 계좌개설\n2. 입금\n3. 출금\n4. 계좌번호 전체 출력\n5. 프로그램 종료')
    try:
        i = int(input('선택(1~5 숫자만 입력) : '))
    except ValueError:
        print('1~5의 숫자만 입력하세요')
        break

    if i == 1:
        BankAccount.open_account()

    elif i == 2:
        print('\n[입금]')
        try:
            deposit_id = int(input('계좌ID: '))
        except:
            print('숫자만 입력하세요')
            break
        try:
            deposit_amount = int(input('입금액: '))
        except:
            print('숫자만 입력하세요')
            break

        if deposit_id in accounts.keys():
            BankAccount.deposit
        else:
            print('유효하지 않은 ID 입니다')
            break
            # return
            # sys.exit()

    elif i == 3:
        print('\n[출금]')
        try:
            withdrawal_id = int(input('계좌ID: '))
        except:
            print('숫자만 입력하세요')
            break
        try:
            withdrawal_amount = int(input('출금액: '))
        except:
            print('숫자만 입력하세요')
            break

        if withdrawal_id in accounts.keys():
            BankAccount.withdrawal
        else:
            print('유효하지 않은 ID 입니다')
            break
            # return
            # sys.exit()

    elif i == 4:
        BankAccount.print_all_account()
    
    print()