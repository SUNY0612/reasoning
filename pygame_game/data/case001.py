"""CASE 001의 장소와 증거 데이터입니다.

증거품의 x, y, width, height 값만 바꾸면 화면 위치를 쉽게 조정할 수 있습니다.
image 값은 프로젝트 폴더 기준 경로입니다.
"""

CASE_TITLE = "사라진 발의 목격자"
CASE_CODE = "CASE FILE 001"
CASE_SUMMARY = (
    "자정이 되기 11분 전, 도시에서 가장 오래된 극장의 보관실이 열렸다. "
    "문은 안쪽에서 잠겨 있었고, 현장에는 낡은 카세트테이프 하나만 남아 있었다."
)

LOCATIONS = [
    {
        "id": "storage_room",
        "name": "극장 보관실",
        "background": "assets/backgrounds/storage_room.png",
        "subtitle": "잠긴 문과 먼지 쌓인 바닥",
    },
    {
        "id": "hallway",
        "name": "극장 복도",
        "background": "assets/backgrounds/hallway.png",
        "subtitle": "오래된 근무표가 붙은 복도",
    },
    {
        "id": "back_alley",
        "name": "극장 뒷골목",
        "background": "assets/backgrounds/back_alley.png",
        "subtitle": "공연장 뒤편의 어두운 골목",
    },
]

EVIDENCE = [
    {
        "id": "cassette",
        "name": "낡은 카세트테이프",
        "location": "storage_room",
        "image": "Evidence/스크린샷 2026-08-26 203030.png",
        "x": 650, "y": 420, "width": 150, "height": 105,
        "description": "오래된 검은색 카세트테이프다. 라벨에는 23:49라고 적혀 있다.",
        "result": "오래된 녹음 파일이 남아 있다. 문이 열리는 소리와 희미한 발소리가 녹음되어 있다. 녹음 시각은 23:49로 추정된다.",
        "clue": "23:49에 녹음된 의문의 음성이 남아 있다.",
        "importance": "핵심 증거",
    },
    {
        "id": "footprint",
        "name": "희미한 발자국",
        "location": "storage_room",
        "image": "Evidence/스크린샷 2026-08-26 203034.png",
        "x": 335, "y": 595, "width": 190, "height": 90,
        "description": "먼지가 쌓인 바닥에 남겨진 신발 자국이다.",
        "result": "희미한 발자국이 남아 있다. 크기는 약 270mm 정도로 보이며, 발자국의 방향은 보관실 안쪽을 향하고 있다.",
        "clue": "270mm 크기의 발자국이 보관실 안쪽을 향한다.",
        "importance": "핵심 증거",
    },
    {
        "id": "lock",
        "name": "낡은 잠금장치",
        "location": "storage_room",
        "image": "Evidence/스크린샷 2026-08-26 203037.png",
        "x": 1030, "y": 275, "width": 110, "height": 155,
        "description": "오래된 금속 잠금장치다.",
        "result": "문은 안쪽에서도 잠글 수 있는 구조다. 잠금장치에는 최근 생긴 것으로 보이는 긁힌 흔적이 남아 있다.",
        "clue": "안쪽에서도 잠글 수 있지만, 잠금장치에 최근 긁힌 흔적이 있다.",
        "importance": "중요 증거",
    },
    {
        "id": "schedule",
        "name": "극장 직원 근무표",
        "location": "hallway",
        "image": "Evidence/스크린샷 2026-08-26 203045.png",
        "x": 720, "y": 255, "width": 250, "height": 270,
        "description": "극장 직원들의 당일 근무 시간이 적힌 표다.",
        "result": "서준호 15:00~23:30, 박지현 14:00~22:00, 이도현 16:00~24:00, 최민수 15:00~22:30으로 기록되어 있다.",
        "clue": "서준호의 근무 종료 시간은 23:30으로 기록되어 있다.",
        "importance": "핵심 증거",
    },
    {
        "id": "torn_note",
        "name": "찢어진 메모",
        "location": "back_alley",
        "image": "Evidence/스크린샷 2026-08-26 203055.png",
        "x": 420, "y": 355, "width": 210, "height": 145,
        "description": "구겨지고 찢긴 메모다. 종이 일부에 붉은 얼룩이 남아 있다.",
        "result": "메모에는 '...목격자가 되어서는 안 됐다.'라는 문장이 남아 있다. 누군가 급하게 찢어버린 것으로 보인다.",
        "clue": "누군가 '목격자가 되어서는 안 됐다'는 메모를 급하게 숨겼다.",
        "importance": "핵심 증거",
    },
    {
        "id": "cigarette",
        "name": "낯선 담배꽁초",
        "location": "back_alley",
        "image": "Evidence/스크린샷 2026-08-26 203100.png",
        "x": 895, "y": 620, "width": 155, "height": 85,
        "description": "최근에 버려진 담배꽁초다.",
        "result": "극장 직원들이 주로 사용하는 담배와는 다른 브랜드로 보인다.",
        "clue": "외부인의 개입 가능성을 보여주는 보조 단서다.",
        "importance": "보조 증거",
    },
]
