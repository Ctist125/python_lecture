# 주식 이득
def stock_gain(stock_money, stock, bond_money, bond):
    stock_money = stock_money + (stock_money * (stock / 100))
    bond_money = bond_money + (bond_money * (bond / 100))
    total_money = stock_money + bond_money

    stock_money_float2 = "{:.2f}".format(stock_money)
    bond_money_float2 = "{:.2f}".format(bond_money)
    total_money_float2 = "{:.2f}".format((total_money))

    print(f"주식: {stock_money_float2}원, 채권: {bond_money_float2}원, 총: {total_money_float2}원")
    print("-------------------------------------------------------")

    return [stock_money, bond_money, total_money]

# 주식 손실
def stock_loss(stock_money, stock, bond_money, bond):
    stock_money = stock_money - (stock_money * (stock / 100))
    bond_money = bond_money + (bond_money * (bond / 100))
    total_money = stock_money + bond_money

    stock_money_float2 = "{:.2f}".format(stock_money)
    bond_money_float2 = "{:.2f}".format(bond_money)
    total_money_float2 = "{:.2f}".format((total_money))

    print(f"주식: {stock_money_float2}원, 채권: {bond_money_float2}원, 총: {total_money_float2}원")
    print("-------------------------------------------------------")

    return [stock_money, bond_money, total_money]

# 리벨런싱
def rebalancing(total_money, stock_ratio, bond_ratio):
    stock_money = total_money * (stock_ratio / 100)
    bond_money = total_money * (bond_ratio / 100)
    print("리밸런싱")
    print("-------------------------------------------------------")

    return [stock_money, bond_money]