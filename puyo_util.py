class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[None for _ in range(width)] for _ in range(height)]  # フィールドの初期化
        self.heights = [0 for _ in range(width)]  # 各列のぷよの高さ

    def set_puyo(self, x, y, color):
        # 指定位置にぷよを配置
        self.data[y][x] = color
        self.heights[x] = max(self.heights[x], y + 1)

    def check_erase(self):
        erased_puyos = []  # 消去されたぷよのリスト

        for y in range(self.height - 1, -1, -1):  # 下から上に走査
            for x in range(self.width):
                if self.data[y][x]:  # ぷよがある場合
                    connected_puyos = self.get_connected_puyos(x, y)  # 連結しているぷよを取得
                    if len(connected_puyos) >= 4:  # 4つ以上繋がっていたら
                        erased_puyos.extend(connected_puyos)  # 消去リストに追加

        for x, y in erased_puyos:  # 消去されたぷよを削除
            self.data[y][x] = None

        self.drop_puyos()  # ぷよの落下処理

    def get_connected_puyos(self, x, y):
        # 指定された座標から連結している同じ色のぷよを探索
        target_color = self.data[y][x]
        visited = set()
        queue = [(x, y)]
        connected_puyos = []

        while queue:
            x, y = queue.pop(0)
            if (x, y) in visited or not (0 <= x < self.width and 0 <= y < self.height):
                continue
            visited.add((x, y))

            if self.data[y][x] == target_color:
                connected_puyos.append((x, y))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    queue.append((x + dx, y + dy))

        return connected_puyos

    def drop_puyos(self):
        # ぷよの落下処理
        for x in range(self.width):
            for y in range(self.height - 2, -1, -1):
                if self.data[y][x] and self.data[y + 1][x] is None:
                    self.data[y + 1][x] = self.data[y][x]
                    self.data[y][x] = None

    def is_game_over(self):
        # ゲームオーバー判定
        return any(h >= self.height for h in self.heights)

    def draw(self, screen):
        # フィールドを描画
        for y in range(self.height):
            for x in range(self.width):
                if self.data[y][x]:
                    # ぷよを描画
                    pass

class Puyo:
    def __init__(self, x, y, shapes, color):
        self.x = x
        self.y = y
        self.shapes = shapes  # 回転状態ごとの形状
        self.color = color
        self.rotation = 0  # 現在の回転状態

    def move(self, dx=0, dy=1):
        # ぷよを移動 (左右、落下)
        self.x += dx
        self.y += dy

    def rotate(self):
        # ぷよを回転
        self.rotation = (self.rotation + 1) % len(self.shapes)

    def draw(self, screen):
        # ぷよを描画
        current_shape = self.shapes[self.rotation]
        for i in range(2):
            x = self.x + current_shape[i][0]
            y = self.y + current_shape[i][1]
            # ぷよ1つを描画
            pass                