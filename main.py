# 시드 데이터
prompts = [
    {
        "title": "블로그 글쓰기",
        "content": "주제에 맞는 블로그 글을 써줘",
        "category": "글쓰기",
        "favorite": False
    },
    {
        "title": "코드 리뷰",
        "content": "이 코드의 문제점을 찾아줘",
        "category": "개발",
        "favorite": True
    },
    {
        "title": "영어 번역",
        "content": "한국어를 영어로 번역해줘",
        "category": "번역",
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
    print("5. 종료")

    # 전체 목록 보기 함수
def show_all():
    print("\n=== 전체 프롬프트 목록 ===")
    for i, prompt in enumerate(prompts, 1):
        print(f"{i}. [{prompt['category']}] {prompt['title']}")
        print(f"   {prompt['content']}")

# 메인 실행
def main():
    while True:
        show_menu()
        choice = input("\n선택하세요: ")

        if choice == "1":
            show_all()
        elif choice == "2":
            print("→ 추가 기능 (곧 만들 예정)")
        elif choice == "3":
            print("→ 검색 기능 (곧 만들 예정)")
        elif choice == "4":
            print("→ 즐겨찾기 기능 (곧 만들 예정)")
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("❌ 1~5 중에서 선택하세요!")

# 프로그램 시작
main()