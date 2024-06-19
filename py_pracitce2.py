# 対象ユーザーの注文履歴を返す処理を作成してください
def get_order_history(USER, ORDERS):
    order_history = []

    for ORDER in ORDERS:
        if USER["user_id"] == ORDER["user_id"]:
            order_history.append(ORDER)
                
    return order_history
    
# ここから下は触らないでください
# 利用するデータ
orders = [
    {
        'order_id': 1,
        'user_id': 1,
        'items': [
            {'name': 'キャップ', 'type': 'cap', 'price': 8000},
            {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000}
        ]
    },
    {
        'order_id': 2,
        'user_id': 2,
        'items': [
            {'name': 'ランニングシューズ', 'type': 'shoes', 'price': 15000},
        ]
    },
    {
        'order_id': 3,
        'user_id': 1,
        'items': [
            {'name': 'スポーツドリンク', 'type': 'food', 'price': 150}
        ]
    },
    {
        'order_id': 4,
        'user_id': 3,
        'items': [
            {'name': 'アンダーウェア', 'type': 'clothes', 'price': 4500},
            {'name': 'テニスラケット', 'type': 'sports goods', 'price': 8000}          
        ]
    }
]

user = {'user_id': 1, 'status': 'basic'}
# 関数の呼び出し
user_orders = get_order_history(user, orders)
for order in user_orders:
    print(order)
