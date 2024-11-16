import sys
from decimal import Decimal
def main():
    def convet_coin(coin1,coin2):
        return coin1*coin2    
    main_menu_message = """Welcome to Coin Conventer !
    this program was developed to help you 
    by : Nour mohamed :)
    """
    print(main_menu_message)
    while True:
        try:
            coin_value = Decimal(input("Inter the coin value : "))
            coin_before_convent = Decimal(input('How much coin do you want to transfer : '))
            coin_after_convent = convet_coin(coin_value,coin_before_convent)
            print(f"\nTotal coins = {coin_after_convent} $\n")
            while True:
                convet_again = input("do yo want to convent again ? (y,n) :").lower()
                if convet_again == 'y':
                    break
                elif convet_again == 'n':
                    sys.exit(0)
                else:
                    print("incorrect choice ! please choose between (y,n) ")
        except ValueError:
            print('please choose only numbers! ')
            

if __name__ == "__main__":
    main()