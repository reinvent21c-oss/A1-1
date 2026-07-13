# 시드 데이터
prompts = [
    {
        "title": "블로그 글쓰기",
        "content": "주제에 맞는 블로그 글을 써줘",
        "category": "텍스트 생성",   
        "favorite": False
    },
    {
        "title": "코드 리뷰",
        "content": "이 코드의 문제점을 찾아줘",
        "category": "자동화",         
        "favorite": True
    },
    {
        "title": "영어 번역",
        "content": "한국어를 영어로 번역해줘",
        "category": "기타",           
        "favorite": False
    }
]

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
        print(f"   {prompt['content']}")

# 프롬프트 추가 함수
def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    title = input("제목: ")
    content = input("내용: ")
    category = input("카테고리: ")

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
            print(f"   {prompt['content']}")
    else:
        print(f"❌ '{keyword}'에 해당하는 프롬프트가 없습니다.")

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
            print(f"   {prompt['content']}")
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

    # 입력이 1~6 사이 숫자인지 확인
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
    show_all()  # 목록 먼저 보여주기
    
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
            show_detail()        # ← 추가
        elif choice == "7":
            pass                 # ← 다음 단계에서 구현
        elif choice == "8":      # ← 6에서 8로 변경
            print("프로그램을 종료합니다.")
            break
        else:
            print("❌ 1~8 중에서 선택하세요!")

# 프로그램 시작
main()