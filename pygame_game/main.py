"""뭐든 해결합니다 - CASE 001 Pygame 프로토타입

실행: 프로젝트 루트에서 `python pygame_game/main.py`
이미지는 assets 또는 Evidence 폴더에서 읽으며, 없는 이미지는 placeholder로 표시합니다.
"""

from pathlib import Path
import sys
import pygame

from data.case001 import CASE_CODE, CASE_SUMMARY, CASE_TITLE, EVIDENCE, LOCATIONS

pygame.init()
pygame.font.init()

ROOT = Path(__file__).resolve().parent.parent
WIDTH, HEIGHT = 1280, 720
FPS = 60
BG = (39, 38, 35)
PAPER = (232, 223, 201)
PAPER_DARK = (199, 187, 161)
INK = (42, 40, 36)
MUTED = (137, 128, 110)
RED = (171, 69, 54)
GOLD = (194, 153, 83)

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("뭐든 해결합니다 | CASE 001")
clock = pygame.time.Clock()

# 시스템에 있는 한글 폰트를 우선 사용하고, 없으면 Pygame 기본 폰트를 사용합니다.
def make_font(size, bold=False):
    candidates = ["malgungothic", "맑은 고딕", "notosanscjkkr", "arial"]
    for name in candidates:
        font = pygame.font.SysFont(name, size, bold=bold)
        if font.get_height() > 0:
            return font
    return pygame.font.Font(None, size)

FONT_SMALL = make_font(14)
FONT_BODY = make_font(18)
FONT_TITLE = make_font(42, True)
FONT_BIG = make_font(64, True)
FONT_TINY = make_font(11)

state = "home"
current_location = None
selected_evidence = None
popup_mode = None
answer_choice = None
result_correct = False
collected_ids = set()
notebook_ids = []


def load_image(relative_path, size=None):
    """이미지를 읽고 실패하면 None을 반환합니다."""
    path = ROOT / relative_path
    try:
        image = pygame.image.load(path).convert_alpha()
        if size:
            image = pygame.transform.smoothscale(image, size)
        return image
    except (pygame.error, FileNotFoundError):
        return None


def wrap_text(text, font, max_width):
    lines, current = [], ""
    for word in text.split(" "):
        trial = f"{current} {word}".strip()
        if font.size(trial)[0] <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_text(text, position, font=FONT_BODY, color=INK, max_width=None, line_gap=7):
    x, y = position
    lines = wrap_text(text, font, max_width) if max_width else text.split("\n")
    for line in lines:
        screen.blit(font.render(line, True, color), (x, y))
        y += font.get_height() + line_gap
    return y


def button(rect, label, active=True, accent=False):
    mouse_over = rect.collidepoint(pygame.mouse.get_pos())
    fill = RED if accent else (PAPER if active else (75, 72, 65))
    if mouse_over and active:
        fill = GOLD if accent else (247, 239, 216)
    pygame.draw.rect(screen, fill, rect, border_radius=4)
    pygame.draw.rect(screen, PAPER_DARK if not accent else RED, rect, 1, border_radius=4)
    color = PAPER if accent else INK
    if not active:
        color = MUTED
    label_surface = FONT_SMALL.render(label, True, color)
    screen.blit(label_surface, label_surface.get_rect(center=rect.center))
    return mouse_over


def top_bar(title, show_back=True):
    pygame.draw.rect(screen, (29, 29, 27), (0, 0, WIDTH, 72))
    draw_text("뭐든 해결합니다", (32, 22), FONT_BODY, PAPER)
    draw_text(title, (WIDTH - 330, 26), FONT_TINY, PAPER_DARK)
    if show_back:
        return pygame.Rect(WIDTH - 145, 17, 112, 36)
    return None


def draw_home():
    screen.fill(BG)
    pygame.draw.rect(screen, (54, 48, 40), (0, 0, WIDTH, 9))
    draw_text("의뢰 0     신뢰 0     수첩 0/30", (42, 32), FONT_SMALL, PAPER_DARK)
    draw_text("뭐든\n해결합니다", (80, 140), FONT_BIG, PAPER)
    draw_text("사건을 직접 보고, 직접 연결하고, 직접 해결하세요.", (85, 310), FONT_BODY, MUTED)
    card = pygame.Rect(610, 120, 530, 425)
    pygame.draw.rect(screen, (52, 49, 43), card, border_radius=5)
    pygame.draw.rect(screen, PAPER_DARK, card, 1, border_radius=5)
    draw_text("새로운 의뢰", (650, 160), FONT_SMALL, RED)
    draw_text(CASE_CODE, (650, 195), FONT_TINY, PAPER_DARK)
    draw_text(CASE_TITLE, (650, 235), FONT_TITLE, PAPER)
    draw_text("도시에서 가장 오래된 극장의 보관실.\n밀실처럼 보이는 현장에 남겨진 카세트.", (650, 315), FONT_BODY, PAPER_DARK, 420)
    button(pygame.Rect(650, 455, 190, 45), "사건 접수", accent=True)
    draw_text("CLICK TO INVESTIGATE", (650, 570), FONT_TINY, MUTED)


def draw_case_file():
    screen.fill(PAPER)
    top_bar(CASE_CODE, False)
    draw_text("사건 파일", (75, 130), FONT_SMALL, RED)
    draw_text(CASE_CODE, (75, 165), FONT_TINY, MUTED)
    draw_text(CASE_TITLE, (75, 210), FONT_TITLE, INK)
    pygame.draw.line(screen, PAPER_DARK, (75, 285), (WIDTH - 75, 285), 1)
    draw_text("사건 개요", (75, 330), FONT_SMALL, RED)
    draw_text(CASE_SUMMARY, (75, 370), FONT_BODY, INK, 630, 10)
    draw_text("STATUS: OPEN", (900, 175), FONT_SMALL, RED)
    draw_text("조사 가능한 장소 3곳\n수집 가능한 단서 6개", (900, 225), FONT_BODY, MUTED, 260)
    button(pygame.Rect(75, 555, 220, 48), "수사 기록 보기", accent=True)


def location_card(location, rect):
    pygame.draw.rect(screen, (55, 52, 46), rect, border_radius=4)
    pygame.draw.rect(screen, PAPER_DARK, rect, 1, border_radius=4)
    preview = load_image(location["background"], (rect.width - 2, 118))
    if preview:
        screen.blit(preview, (rect.x + 1, rect.y + 1))
    else:
        pygame.draw.rect(screen, (71, 65, 55), (rect.x + 1, rect.y + 1, rect.width - 2, 118))
        draw_text("배경 이미지 준비 중", (rect.x + 28, rect.y + 53), FONT_SMALL, PAPER_DARK)
    draw_text(location["name"], (rect.x + 18, rect.y + 140), FONT_BODY, PAPER)
    draw_text(location["subtitle"], (rect.x + 18, rect.y + 172), FONT_TINY, MUTED)
    draw_text("조사 가능  →", (rect.x + 18, rect.bottom - 28), FONT_TINY, GOLD)


def draw_board():
    screen.fill(BG)
    top_bar("수사 기록 / 사건판", False)
    draw_text("사건판", (52, 115), FONT_TITLE, PAPER)
    draw_text("장소를 선택해 현장을 조사하고, 발견한 단서를 수첩에 기록하세요.", (55, 175), FONT_SMALL, MUTED)
    for index, location in enumerate(LOCATIONS):
        x = 55 + index * 390
        location_card(location, pygame.Rect(x, 235, 350, 245))
    notebook_button = pygame.Rect(55, 560, 170, 44)
    answer_button = pygame.Rect(WIDTH - 225, 560, 170, 44)
    button(notebook_button, f"수첩  {len(notebook_ids)}/30")
    button(answer_button, "정답 제출", accent=True)
    draw_text(f"발견한 단서 {len(collected_ids)} / 6", (255, 575), FONT_SMALL, PAPER_DARK)


def draw_placeholder_background(location):
    screen.fill((57, 54, 48))
    for y in range(85, HEIGHT, 70):
        pygame.draw.line(screen, (72, 68, 59), (0, y), (WIDTH, y), 1)
    pygame.draw.rect(screen, (42, 40, 36), (0, HEIGHT - 155, WIDTH, 155))
    draw_text(location["name"], (52, 118), FONT_BIG, PAPER)
    draw_text("배경 이미지가 없습니다. assets/backgrounds/에 PNG를 넣으면 자동으로 표시됩니다.", (56, 205), FONT_SMALL, PAPER_DARK, 620)
    draw_text("PLACEHOLDER SCENE", (56, 245), FONT_TINY, RED)


def evidence_rect(evidence):
    scale_x = WIDTH / 1280
    scale_y = (HEIGHT - 72) / 648
    return pygame.Rect(int(evidence["x"] * scale_x), int(72 + (evidence["y"] - 72) * scale_y), int(evidence["width"] * scale_x), int(evidence["height"] * scale_y))


def draw_evidence(evidence):
    rect = evidence_rect(evidence)
    image = load_image(evidence["image"], (rect.width, rect.height))
    if image:
        screen.blit(image, rect)
    else:
        pygame.draw.rect(screen, (156, 137, 105), rect, border_radius=3)
        pygame.draw.rect(screen, GOLD, rect, 2, border_radius=3)
        draw_text("증거 이미지 없음", (rect.x + 12, rect.centery - 8), FONT_TINY, INK)
    if evidence["id"] in collected_ids:
        pygame.draw.rect(screen, (113, 176, 112), rect, 2, border_radius=3)
    if rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, GOLD, rect.inflate(8, 8), 2, border_radius=4)
        draw_text(evidence["name"], (rect.x, max(80, rect.y - 25)), FONT_TINY, PAPER)


def draw_location():
    location = next(item for item in LOCATIONS if item["id"] == current_location)
    background = load_image(location["background"], (WIDTH, HEIGHT))
    if background:
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, WIDTH, HEIGHT), 0)
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((15, 14, 12, 72))
        screen.blit(overlay, (0, 0))
    else:
        draw_placeholder_background(location)
    pygame.draw.rect(screen, (25, 24, 22), (0, 0, WIDTH, 72))
    draw_text(location["name"], (30, 25), FONT_BODY, PAPER)
    back_button = pygame.Rect(WIDTH - 215, 18, 175, 36)
    button(back_button, "사건판으로 돌아가기")
    for evidence in EVIDENCE:
        if evidence["location"] == current_location:
            draw_evidence(evidence)
    draw_text("물건을 클릭하여 조사", (30, HEIGHT - 38), FONT_TINY, PAPER_DARK)


def draw_notebook():
    screen.fill(PAPER)
    top_bar("수첩", False)
    draw_text("수첩", (65, 120), FONT_TITLE, INK)
    draw_text("발견하지 않은 단서는 ???로 표시됩니다.", (68, 180), FONT_SMALL, MUTED)
    for index, evidence in enumerate(EVIDENCE):
        y = 235 + index * 62
        pygame.draw.line(screen, PAPER_DARK, (68, y + 45), (WIDTH - 68, y + 45), 1)
        if evidence["id"] in notebook_ids:
            draw_text(f"단서 {index + 1:02d}   ✓", (75, y), FONT_SMALL, RED)
            draw_text(f"{evidence['name']}  →  {evidence['clue']}", (250, y), FONT_SMALL, INK, 850)
        else:
            draw_text(f"단서 {index + 1:02d}   ???", (75, y), FONT_SMALL, MUTED)
            draw_text("아직 발견하지 않음", (250, y), FONT_SMALL, MUTED)
    button(pygame.Rect(68, HEIGHT - 65, 130, 40), "사건판으로")


def draw_answer():
    screen.fill(PAPER)
    top_bar("정답 제출", False)
    draw_text("마지막 질문", (80, 135), FONT_SMALL, RED)
    draw_text("23:49에 극장에 있었던 인물은?", (80, 190), FONT_TITLE, INK)
    draw_text("근무표와 카세트의 시간을 비교해 가장 가능성 높은 인물을 선택하세요.", (82, 270), FONT_BODY, MUTED)
    choices = ["서준호", "박지현", "이도현", "외부인"]
    for index, choice in enumerate(choices):
        rect = pygame.Rect(85 + (index % 2) * 280, 355 + (index // 2) * 75, 240, 48)
        selected = answer_choice == choice
        pygame.draw.rect(screen, RED if selected else (216, 204, 179), rect, border_radius=4)
        pygame.draw.rect(screen, RED if selected else PAPER_DARK, rect, 2, border_radius=4)
        draw_text(choice, (rect.x + 25, rect.y + 13), FONT_BODY, PAPER if selected else INK)
    button(pygame.Rect(85, 550, 155, 46), "제출하기", accent=True)
    button(pygame.Rect(260, 550, 155, 46), "사건판으로")


def draw_result():
    screen.fill(BG)
    title = "사건 해결" if result_correct else "추리가 틀렸습니다."
    color = GOLD if result_correct else RED
    draw_text("CASE FILE 001", (80, 130), FONT_SMALL, MUTED)
    draw_text(title, (80, 190), FONT_BIG, color)
    if result_correct:
        text = "서준호는 23:30 퇴근 기록 이후에도 현장에 있었을 가능성이 높습니다. 카세트의 23:49 녹음과 잠금장치의 흔적이 그의 알리바이를 흔듭니다."
    else:
        text = "카세트의 녹음 시각 23:49와 직원 근무표를 다시 확인해 보세요. 사건판으로 돌아가 놓친 단서를 조사할 수 있습니다."
    draw_text(text, (85, 320), FONT_BODY, PAPER_DARK, 650, 10)
    button(pygame.Rect(85, 520, 180, 45), "사건판으로")


def show_popup():
    if not selected_evidence:
        return
    shade = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    shade.fill((0, 0, 0, 175))
    screen.blit(shade, (0, 0))
    panel = pygame.Rect(270, 125, 740, 470)
    pygame.draw.rect(screen, PAPER, panel, border_radius=5)
    pygame.draw.rect(screen, GOLD, panel, 2, border_radius=5)
    evidence = selected_evidence
    label = "새로운 단서를 발견했습니다." if evidence["id"] not in collected_ids else "조사 기록"
    draw_text(label, (315, 170), FONT_SMALL, RED)
    draw_text(evidence["name"], (315, 215), FONT_TITLE, INK)
    draw_text(evidence["result"], (315, 290), FONT_BODY, INK, 650, 10)
    draw_text(evidence["importance"], (315, 430), FONT_TINY, MUTED)
    if evidence["id"] not in collected_ids:
        button(pygame.Rect(315, 490, 170, 42), "수첩에 기록", accent=True)
    button(pygame.Rect(505, 490, 120, 42), "닫기")


def click_position(position):
    global state, current_location, selected_evidence, popup_mode, answer_choice, result_correct
    x, y = position
    if state == "home":
        if pygame.Rect(650, 455, 190, 45).collidepoint(position):
            state = "case_file"
    elif state == "case_file":
        if pygame.Rect(75, 555, 220, 48).collidepoint(position):
            state = "board"
    elif state == "board":
        for index, location in enumerate(LOCATIONS):
            if pygame.Rect(55 + index * 390, 235, 350, 245).collidepoint(position):
                current_location = location["id"]
                state = "location"
                return
        if pygame.Rect(55, 560, 170, 44).collidepoint(position):
            state = "notebook"
        elif pygame.Rect(WIDTH - 225, 560, 170, 44).collidepoint(position):
            state = "answer"
    elif state == "location":
        if pygame.Rect(WIDTH - 215, 18, 175, 36).collidepoint(position):
            state = "board"
            return
        for evidence in EVIDENCE:
            if evidence["location"] == current_location and evidence_rect(evidence).collidepoint(position):
                selected_evidence = evidence
                popup_mode = "inspect"
                return
    elif state == "notebook":
        if pygame.Rect(68, HEIGHT - 65, 130, 40).collidepoint(position):
            state = "board"
    elif state == "answer":
        choices = ["서준호", "박지현", "이도현", "외부인"]
        for index, choice in enumerate(choices):
            rect = pygame.Rect(85 + (index % 2) * 280, 355 + (index // 2) * 75, 240, 48)
            if rect.collidepoint(position):
                answer_choice = choice
                return
        if pygame.Rect(85, 550, 155, 46).collidepoint(position) and answer_choice:
            result_correct = answer_choice == "서준호"
            state = "result"
        elif pygame.Rect(260, 550, 155, 46).collidepoint(position):
            state = "board"
    elif state == "result":
        if pygame.Rect(85, 520, 180, 45).collidepoint(position):
            state = "board"
    if popup_mode == "inspect":
        popup_mode = None


def click_popup(position):
    global popup_mode, selected_evidence
    if not selected_evidence:
        return
    if selected_evidence["id"] not in collected_ids and pygame.Rect(315, 490, 170, 42).collidepoint(position):
        collected_ids.add(selected_evidence["id"])
        notebook_ids.append(selected_evidence["id"])
        popup_mode = None
        selected_evidence = None
    elif pygame.Rect(505, 490, 120, 42).collidepoint(position):
        popup_mode = None
        selected_evidence = None


def draw_current_screen():
    screens = {"home": draw_home, "case_file": draw_case_file, "board": draw_board,
               "location": draw_location, "notebook": draw_notebook, "answer": draw_answer,
               "result": draw_result}
    screens[state]()
    if popup_mode == "inspect":
        show_popup()


def main():
    global screen, WIDTH, HEIGHT, popup_mode
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = max(900, event.w), max(600, event.h)
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if popup_mode:
                    popup_mode = None
                elif state == "location":
                    state = "board"
                elif state in {"notebook", "answer", "result"}:
                    state = "board"
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if popup_mode:
                    click_popup(event.pos)
                else:
                    click_position(event.pos)
            elif event.type == pygame.FINGERUP:
                touch_position = (int(event.x * WIDTH), int(event.y * HEIGHT))
                if popup_mode:
                    click_popup(touch_position)
                else:
                    click_position(touch_position)
        draw_current_screen()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
