import pygame

class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[None for _ in range(width)] for _ in range(height)]  # フィールドの初期化
        self.heights = [0 for _ in range(width)]  # 各列のぷよの高さ

    def set_puyo(self, puyo):
        for i in range(2):
            x = puyo.x + puyo.shape[puyo.rotation][i][0]
            y = puyo.y + puyo.shape[puyo.rotation][i][1]
            if 0 <= x < self.width and 0 <= y < self.height:
                self.data[y][x] = puyo.color
                self.heights[x] = max(self.heights[x], y + 1)  # heights を更新 (修正)

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

    def is_game_over(self, current_puyo, GRID_WIDTH):
        next_puyo_x = GRID_WIDTH // 2 - 1
        next_puyo_y = 0
        for i in range(2):
            x = next_puyo_x + current_puyo.shape[0][i][0]
            y = next_puyo_y + current_puyo.shape[0][i][1]
            if 0 <= x < self.width and 0 <= y < self.height and self.data[y][x] is not None:
                return True
        return False
    
    def draw(self, screen, GRID_SIZE, COLORS):
        # フィールドを描画
        for y in range(self.height):
            for x in range(self.width):
                # セルの枠線を描画
                pygame.draw.rect(screen, (128, 128, 128), (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)
                if self.data[y][x]:
                    # ぷよを描画
                    pygame.draw.rect(screen, COLORS[self.data[y][x]], (x * GRID_SIZE + 1, y * GRID_SIZE + 1, GRID_SIZE - 2, GRID_SIZE - 2))

class Puyo:
    def __init__(self, x, y, shape, color, field):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.rotation = 0
        self.field = field

    def move(self, field, dx=0, dy=0):  # 引数に field を追加
        new_x = self.x + dx
        new_y = self.y + dy

        # x 方向の移動制限
        if 0 <= new_x < field.width - 1:  # 右端のブロックがはみ出ないように -1
            self.x = new_x

        # y 方向の移動制限
        if 0 <= new_y < field.height:
            self.y = new_y

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)

    def can_move_down(self, field, GRID_HEIGHT):
        for i in range(2):
            x = self.x + self.shape[self.rotation][i][0]
            y = self.y + self.shape[self.rotation][i][1] + 1
            if y >= GRID_HEIGHT or (0 <= y < GRID_HEIGHT and field.data[y][x] is not None):  # 修正
                return False
        return True
    
    def can_rotate(self, field):
        next_rotation = (self.rotation + 1) % len(self.shape)
        for i in range(2):
            x = self.x + self.shape[next_rotation][i][0]
            y = self.y + self.shape[next_rotation][i][1]
            if not (0 <= x < field.width and 0 <= y < field.height) or field.data[y][x] is not None:
                return False
        return True

    def rotate(self, field):  # 引数に field を追加
        if self.can_rotate(field):
            self.rotation = (self.rotation + 1) % len(self.shape)
    
    def move_down(self):
        self.y += 1

    def draw(self, screen, GRID_SIZE, COLORS):
        for i in range(2):
            x = self.x + self.shape[self.rotation][i][0]
            y = self.y + self.shape[self.rotation][i][1]
            pygame.draw.rect(screen, COLORS[self.color], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    def draw_next(self, screen, GRID_WIDTH, GRID_SIZE, COLORS):
        for i in range(2):
            x = GRID_WIDTH + 2 + self.shape[0][i][0]
            y = 2 + self.shape[0][i][1]
            pygame.draw.rect(screen, COLORS[self.color], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
