def calculate_change(total_amount, item_price):
    coins = [500, 100, 50, 10]
    change = total_amount - item_price

    if change < 0:
        return "支払額が不足しています。"

    result = {}

    for coin in coins:
        coin_count = change // coin
        if coin_count > 0:
            result[coin] = coin_count
            change -= coin_count * coin

    if change > 0:
        result["未処理の残額"] = change  
    return result

def main():
    try:
        total_amount = int(input("支払う金額を入力してください（円）: "))
        item_price = int(input("商品の金額を入力してください（円）: "))

        result = calculate_change(total_amount, item_price)

        if isinstance(result, str):
            print(result)
        else:
            print("おつりの枚数:")
            for coin, count in result.items():
                if coin == "未処理の残額":
                    print(f"{coin}: {count}円")
                else:
                    print(f"{coin}円: {count}枚")
    except ValueError:
        print("無効な入力です。数値を入力してください。")

if __name__ == "__main__":
    main()
