#Made by Google Gemini 1.5 Pro

import pygame
import random
import time
import puyo_util as util

# --- 定数 ---
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
FPS = 2

COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
}

SHAPES = [
    [[(0, 0), (1, 0)], [(0, 0), (0, 1)]],  # I
    [[(0, 0), (1, 0)], [(0, 0), (1, 1)]],  # L
    [[(0, 0), (1, 0)], [(1, 0), (1, 1)]],  # 逆L
    [[(0, 0), (1, 0)], [(0, 1), (1, 1)]],  # O
    [[(0, 0), (1, 0)], [(0, 1), (1, -1)]],  # Z
    [[(0, 0), (1, 0)], [(1, 1), (0, -1)]],  # 逆Z
    [[(0, 0), (1, 0), (0, 1)]],  # T
]

# --- 関数 ---
def create_puyo():
    random.seed(time.time())

    shape = random.choice(SHAPES)
    color = random.choice(list(COLORS.keys()))
    return util.Puyo(GRID_WIDTH // 2 - 1, 0, shape, color, util.Field(GRID_WIDTH, GRID_HEIGHT))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    field = util.Field(GRID_WIDTH, GRID_HEIGHT)
    current_puyo = create_puyo()
    next_puyo = create_puyo()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_puyo.move(field, -1, 0)  # 左に移動
                elif event.key == pygame.K_RIGHT:
                    current_puyo.move(field, 1, 0)   # 右に移動
                elif event.key == pygame.K_DOWN:
                    current_puyo.move(field, 0, 1)   # 下に移動
                elif event.key == pygame.K_UP:
                    current_puyo.rotate(field)    # 回転

        # ぷよの落下
        if current_puyo.can_move_down(field, GRID_HEIGHT):
            current_puyo.move_down()
        else:
            field.set_puyo(current_puyo)

            # ゲームオーバー判定 (修正箇所)
            if field.is_game_over(current_puyo, GRID_WIDTH):
                running = False
            else:
                # 新しいぷよを生成 (修正箇所)
                current_puyo = next_puyo
                next_puyo = create_puyo()

                # ぷよの消去 (修正箇所)
                field.check_erase()


        # 描画
        screen.fill((0, 0, 0))
        field.draw(screen, GRID_SIZE, COLORS)
        current_puyo.draw(screen, GRID_SIZE, COLORS)
        next_puyo.draw_next(screen, GRID_WIDTH, GRID_SIZE, COLORS)  # NEXT ぷよの描画

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()