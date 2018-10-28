# Stock Transaction Program2_12

def main():
    # calculate purchased stock.
    paid_for=2000.00*42
    comm1=paid_for*3/100

    # calculate sold stock.
    sold_for=2000*42.75
    comm2=sold_for*3/100
    total_comm=comm1+comm2

    # calculate profit.
    profit=(sold_for-paid_for)-total_comm

    # display the result.
    print('The amount of money paid for the stock $:',format(paid_for,'.2f'),sep='')
    print('The amount of commission when he bought: the stock $:',format(comm1,'.2f'),sep='')
    print('The amount for which sold the stock $:',format(sold_for,'.2f'),sep='')
    print('The amount of commission paid when he sold the stock $:',format(comm2,'.2f'),sep='')
    print('Profit is: $ ',format(profit,'.2f'),sep='')

main()
