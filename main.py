# 시드 데이터 (이전 미션에서 실제 작성·사용한 프롬프트 3개)
prompts = [
    {
        "title": "킥오프 회의록 정리 (웹에이전시 PM)",
        "content": """너는 웹에이전시 프로젝트 담당자(PM)를 보조하는 회의 기록 및 프로젝트 문서화 담당자다.
[출력 항목] 회의 목적 / 결정사항 / 후속 실행 항목 / 확인된 사실 / 가능한 리스크 / 확인 필요 사항 / 후속 일정 7개로 구분한다.
[작성 원칙] 회의 메모에 명시된 내용만 확정 표현으로 쓴다. 없는 내용은 추정해서 사실처럼 쓰지 않는다. 확정 사항과 희망사항·검토 중인 사항을 구분한다. 추론이 필요한 내용은 결정사항이 아니라 가능한 리스크로 분리한다. 정보가 부족하면 '확인 필요'로 표시한다. 인물 실명 대신 역할명을 쓴다.
[결정사항 기준] '~하기로 했다' 형태만 결정사항으로 분류한다. '가능', '좋겠다', '검토', '제안', '내부 확인 필요'는 결정사항으로 단정하지 않는다.
[후속 실행 항목] 담당 역할 / 해야 할 일 / 기한 또는 조건 / 비고 표로 작성한다. 기한이 없으면 임의로 날짜를 만들지 않고 '확인 필요'라고 쓴다.""",
        "category": "페르소나",
        "favorite": False
    },
    {
        "title": "교육과정 합격 안내 메일 생성",
        "content": """너는 교육 프로그램 운영 담당자입니다. 아래 응답자에게 보낼 합격 안내 메일 본문을 작성하세요.
[조건] 공손하고 자연스러운 한국어. 합격 사실을 명확히 안내. 평가점수는 참고용으로만 반영하고 과장된 칭찬은 금지. 다음 단계는 '추후 안내 예정'이라고만 작성. 5문장 이내. 제목 없이 본문만. 끝인사와 발신자명은 작성하지 않는다.
응답자 이름: {{1.answers.`16d21c54`.textAnswers.answers[].value}}
평가점수: {{1.answers.`2745eb6b`.textAnswers.answers[].value}}
판정 결과: 합격""",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "FIFA 뉴스 3줄 요약 (Gemini API 호출)",
        "content": '{"contents":[{"parts":[{"text":"FIFA 2026 관련 뉴스를 한국어 3줄로만 요약해줘. 핵심만. 제목: {{2.title}} 내용: {{escapeJSON(2.description)}}"}]}]}',
        "category": "자동화",
        "favorite": False
    }
]

# 빈 값이면 다시 묻는 입력 보조 함수
def input_required(question):
    while True:
        value = input(question).strip()
        if value:
            return value
        print("❌ 빈 값은 입력할 수 없습니다. 다시 입력해주세요.")

# 메뉴 출력 함수
def show_menu():
    print("\n=== 프롬프트 관리 프로그램 ===")
    print("1. 전체 목록 보기")
    print("2. 프롬프트 추가")
    print("3. 프롬프트 검색")
    print("4. 즐겨찾기 보기")
    print("5. 카테고리별 조회")
    print("6. 상세보기")
    print("7. 즐겨찾기 관리")
    print("8. 종료")

# 전체 목록 보기 함수
def show_all():
    print("\n=== 전체 프롬프트 목록 ===")
    for i, prompt in enumerate(prompts, 1):
        star = "⭐" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']} {star}")

# 프롬프트 추가 함수
def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    title = input_required("제목: ")
    content = input_required("내용: ")
    category = input_required("카테고리: ")

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)
    print(f"✅ '{title}' 프롬프트가 추가되었습니다!")

# 프롬프트 검색 함수
def search_prompt():
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어를 입력하세요: ")
    
    results = []
    for prompt in prompts:
        if keyword in prompt["title"] or keyword in prompt["content"]:
            results.append(prompt)
    if results:
        print(f"\n🔍 '{keyword}' 검색 결과: {len(results)}개")
        for i, prompt in enumerate(results, 1):
            print(f"{i}. [{prompt['category']}] {prompt['title']}")
    else:
        print(f"❌ '{keyword}'에 해당하는 프롬프트가 없습니다.")

def toggle_favorite():
    # 1. 먼저 목록을 보여줘요 (번호를 골라야 하니까!)
    for i, p in enumerate(prompts, 1):
        star = "⭐" if p["favorite"] else "☆"
        print(f"{i}. {star} [{p['category']}] {p['title']}")

    # 2. 사용자에게 번호를 물어봐요
    num = input("\n즐겨찾기를 바꿀 번호: ")

    # 3. 입력값 검증 (숫자인지, 1~개수 범위 안인지)
    if not num.isdigit() or int(num) < 1 or int(num) > len(prompts):
        print("❌ 올바른 번호를 입력하세요!")
        return

    # 4. 고른 프롬프트를 찾아요 (번호는 1부터, 리스트는 0부터라서 -1)
    target = prompts[int(num) - 1]

    # 5. 핵심! 별표를 켜고 끄기 (반대로 뒤집기!)
    target["favorite"] = not target["favorite"]

    # 6. 결과를 알려줘요
    if target["favorite"]:
        print(f"⭐ '{target['title']}'을(를) 즐겨찾기에 추가했습니다!")
    else:
        print(f"☆ '{target['title']}'을(를) 즐겨찾기에서 해제했습니다!")

# 즐겨찾기 보기 함수
def show_favorites():
    print("\n=== ⭐ 즐겨찾기 목록 ===")
    results = []
    for prompt in prompts:
        if prompt["favorite"] == True:
            results.append(prompt)
    
    if results:
        for i, prompt in enumerate(results, 1):
            print(f"{i}. [{prompt['category']}] {prompt['title']}")
    else:
        print("즐겨찾기한 프롬프트가 없습니다.")

# 카테고리 목록 (전역 변수)
categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

# 카테고리별 조회 함수
def show_by_category():
    print("\n=== 카테고리별 조회 ===")
    # 카테고리 번호 목록 출력
    for i, cat in enumerate(categories, 1):
        print(f"{i}) {cat}")

    choice = input("선택: ")

    # 입력이 1~8 사이 숫자인지 확인
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(categories):
        print("❌ 올바른 번호를 선택하세요!")
        return

    # 선택한 카테고리 이름 찾기
    selected = categories[int(choice) - 1]

    # 해당 카테고리 프롬프트만 모으기
    results = []
    for prompt in prompts:
        if prompt["category"] == selected:
            results.append(prompt)

    if results:
        print(f"\n[{selected}] 카테고리 프롬프트:")
        for i, prompt in enumerate(results, 1):
            star = "⭐" if prompt["favorite"] else ""
            print(f"{i}. {prompt['title']} {star}")
        print(f"\n총 {len(results)}개의 프롬프트")
    else:
        print(f"❌ '{selected}' 카테고리에 프롬프트가 없습니다.")

def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")
    for i, prompt in enumerate(prompts, 1):
        star = "⭐" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']} {star}")
    
    num = input("번호 입력: ")
    
    if not num.isdigit() or int(num) < 1 or int(num) > len(prompts):
        print("❌ 올바른 번호를 입력하세요!")
        return
    
    p = prompts[int(num) - 1]
    star = "⭐" if p["favorite"] else "☆"
    
    print("\n────────────────────────────")
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {star}")
    print("────────────────────────────")
    print("내용:")
    print(p['content'])
    print("────────────────────────────")

# 메인 실행
def main():
    while True:
        show_menu()
        choice = input("\n선택하세요: ")

        if choice == "1":
            show_all()
        elif choice == "2":
            add_prompt()
        elif choice == "3":
            search_prompt()
        elif choice == "4":
            show_favorites()
        elif choice == "5":
            show_by_category()
        elif choice == "6":
            show_detail()        
        elif choice == "7":
            toggle_favorite()
        elif choice == "8":      
            print("프로그램을 종료합니다.")
            break
        else:
            print("❌ 1~8 중에서 선택하세요!")

# 프로그램 시작
main()