"""CASE 001 data. Evidence coordinates are authored for a 1280x720 scene."""

CASE_TITLE = "사라진 밤의 목격자"
CASE_CODE = "CASE FILE 001"
CASE_SUMMARY = ("자정이 되기 11분 전, 도시에서 가장 오래된 극장의 보관실이 열렸다. "
                "문은 안쪽에서 잠겨 있었고, 현장에는 낡은 카세트테이프 하나만 남아 있었다.")

LOCATIONS = [
    {"id": "storage_room", "name": "극장 보관실", "background": "pygame_game/assets/backgrounds/storage_room.png", "subtitle": "잠긴 문과 먼지 쌓인 바닥"},
    {"id": "hallway", "name": "극장 복도", "background": "pygame_game/assets/backgrounds/hallway.png", "subtitle": "직원 출입 기록과 근무표"},
    {"id": "back_alley", "name": "극장 뒷골목", "background": "pygame_game/assets/backgrounds/back_alley.png", "subtitle": "찢어진 메모와 낯선 흔적"},
]

# image is optional. Missing images are rendered as labelled evidence cards.
EVIDENCE = [
    {"id":"cassette","name":"낡은 카세트테이프","location":"storage_room","image":"Evidence/스크린샷 2026-08-26 203030.png","x":650,"y":420,"width":150,"height":105,"description":"라벨에 23:49라고 적힌 검은색 카세트다.","result":"문이 열리는 소리와 희미한 발소리가 남아 있다. 녹음 시각은 23:49다.","clue":"23:49에 문이 열리고 발소리가 녹음됐다.","importance":"핵심 증거"},
    {"id":"footprint","name":"희미한 발자국","location":"storage_room","image":"Evidence/스크린샷 2026-08-26 203034.png","x":335,"y":595,"width":190,"height":90,"description":"먼지 쌓인 바닥의 신발 자국이다.","result":"크기는 약 270mm이며, 보관실 안쪽을 향한다.","clue":"270mm 발자국이 보관실 안쪽을 향한다.","importance":"핵심 증거"},
    {"id":"lock","name":"낡은 잠금장치","location":"storage_room","image":"Evidence/스크린샷 2026-08-26 203037.png","x":1030,"y":275,"width":110,"height":155,"description":"오래된 금속 잠금장치다.","result":"문은 안쪽에서도 잠글 수 있고 최근 긁힌 흔적이 있다.","clue":"밀실처럼 보이도록 안쪽에서 잠글 수 있다.","importance":"중요 증거"},
    {"id":"maintenance_key","name":"검은 작업용 키링","location":"storage_room","image":"","x":830,"y":235,"width":125,"height":90,"description":"시설관리팀만 쓰는 검은색 키링이다.","result":"보관실 잠금장치와 같은 규격의 예비 키가 걸려 있다.","clue":"시설관리 담당자만 접근 가능한 예비 키.","importance":"핵심 증거"},
    {"id":"schedule","name":"극장 직원 근무표","location":"hallway","image":"Evidence/스크린샷 2026-08-26 203045.png","x":720,"y":255,"width":250,"height":270,"description":"당일 직원들의 근무 시간이 적혀 있다.","result":"서준호 15:00~23:30, 박지현 14:00~22:00, 이도현 16:00~24:00으로 기록됐다.","clue":"서준호의 공식 퇴근 시간은 23:30이다.","importance":"핵심 증거"},
    {"id":"keycard_log","name":"직원 출입 기록","location":"hallway","image":"","x":385,"y":370,"width":210,"height":150,"description":"직원 구역 카드 출입 시스템 기록이다.","result":"22:47 박지현, 23:41 이도현의 기록은 있으나, 23:49 기록은 비어 있다.","clue":"23:49에는 카드 출입 기록이 없다.","importance":"핵심 증거"},
    {"id":"audio_log","name":"음향 장비 점검 기록","location":"hallway","image":"","x":1010,"y":575,"width":170,"height":92,"description":"음향 시스템의 자동 점검표다.","result":"23:42 외부 음향 시스템의 오류가 이도현 계정으로 기록됐다.","clue":"이도현은 23:42에 장비 오류를 처리했다.","importance":"용의자 단서"},
    {"id":"torn_note","name":"찢어진 메모","location":"back_alley","image":"Evidence/스크린샷 2026-08-26 203055.png","x":420,"y":355,"width":210,"height":145,"description":"붉은 얼룩이 남은 구겨진 메모다.","result":"'...목격자가 되어서는 안 됐다.'라는 문장이 남아 있다.","clue":"누군가 목격자를 숨기려 했다.","importance":"핵심 증거"},
    {"id":"cigarette","name":"낯선 담배꽁초","location":"back_alley","image":"Evidence/스크린샷 2026-08-26 203100.png","x":895,"y":620,"width":155,"height":85,"description":"최근에 버려진 다른 브랜드의 담배다.","result":"극장 직원들이 주로 쓰는 브랜드와 다르다.","clue":"외부인의 개입처럼 보이지만 직접 증거는 아니다.","importance":"보조 증거"},
    {"id":"necklace","name":"은색 목걸이","location":"back_alley","image":"","x":230,"y":570,"width":130,"height":88,"description":"이니셜이 새겨진 오래된 목걸이다.","result":"박지현이 잃어버린 물건이다. 22:47에 이를 찾으러 돌아왔다는 진술과 맞는다.","clue":"박지현의 거짓말에는 개인적인 이유가 있었다.","importance":"용의자 단서"},
    {"id":"contractor_badge","name":"외부업체 출입증","location":"back_alley","image":"","x":720,"y":255,"width":145,"height":100,"description":"이도현이 소속된 음향 업체의 출입증이다.","result":"이도현이 단순한 극장 직원이 아니라 외부 음향업체 소속임을 확인한다.","clue":"이도현의 23:41 재출입은 장비 점검과 연결된다.","importance":"용의자 단서"},
]

SUSPECTS = [
    {"name":"서준호","role":"시설관리팀 대리","summary":"23:30 퇴근했다고 주장한다.","interview":"카세트는 23:49를 가리키고 출입 기록은 비어 있습니다. 예비 키와 잠금장치 구조를 아는 사람은 누구죠?\n\n서준호: ...설비 점검 때문에 잠시 남아 있었습니다. 하지만 목격자에게 해를 끼치려 한 것은 아닙니다.","verdict":"23:49의 무기록 출입, 예비 키, 잠금장치 지식이 한 사람을 가리킨다."},
    {"name":"박지현","role":"매표소 주임","summary":"22:00 퇴근했지만 22:47에 직원 구역에 들어왔다.","interview":"목걸이를 찾으러 돌아왔다고요?\n\n박지현: 네. 어머니 유품이라서요. 무단 출입은 잘못했지만, 보관실에는 가지 않았어요.","verdict":"거짓말은 했지만 목걸이와 22:47 기록이 이유를 설명한다."},
    {"name":"이도현","role":"외부 음향업체 현장 엔지니어","summary":"21:40에 떠났다고 했지만 23:41에 재출입했다.","interview":"23:41에 다시 들어온 사실을 왜 숨겼습니까?\n\n이도현: 장비 오류를 고치러 왔습니다. 제 실수로 생긴 오류를 알리고 싶지 않았습니다.","verdict":"23:42 장비 기록과 출입증이 그의 진술을 뒷받침한다."},
]
