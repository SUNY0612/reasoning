# 뭐든 해결합니다 - CASE 001

Pygame으로 만든 2D 포인트 앤 클릭 추리게임 프로토타입입니다.

## 실행 방법

PowerShell에서 프로젝트 루트(`Reasoning`)로 이동한 뒤 실행합니다.

```powershell
python -m pip install -r pygame_game/requirements.txt
python pygame_game/main.py
```

## 이미지 넣기

- 배경: `pygame_game/assets/backgrounds/`에 `storage_room.png`, `hallway.png`, `back_alley.png`를 넣습니다.
- 증거: 현재 `Evidence/` 폴더의 PNG 6개를 자동으로 사용합니다.
- 증거 이미지가 없거나 이름이 달라져도 게임은 placeholder로 실행됩니다.
- 증거 위치는 `pygame_game/data/case001.py`에서 각 항목의 `x`, `y`, `width`, `height`를 수정합니다.

## 플레이 흐름

메인 화면 → 사건 접수 → 수사 기록 보기 → 사건판 → 장소 선택 → 증거 클릭 → 조사 팝업 → 수첩 기록 → 정답 제출 순서로 진행합니다.

- 장소 화면에서 마우스 클릭과 터치에 대응하는 좌클릭 입력을 사용합니다.
- 조사 팝업은 `ESC` 또는 `닫기` 버튼으로 닫습니다.
- 정답은 `서준호`입니다. 모든 단서를 모으지 않아도 제출할 수 있지만, 수첩에서 단서를 확인하며 추리하는 구조입니다.
