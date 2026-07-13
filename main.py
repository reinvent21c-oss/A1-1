#프롬프트 데이터를 저장할 리스트 (딕셔너리 3개 담기)
prompts = [
    {
        "title": "회의록 정리 프롬프트 v2",
        "content": "너는 웹에이전시 PM을 보조하는 회의 기록 담당자다. 회의 내용을 7개 항목으로 정리한다.",
        "category": "자동화",
        "favorite": False
    },
    {
        "title": "영어 번역 프롬프트",
        "content": "다음 문장을 자연스운 영어로 번역해줘",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "이미지 생성 키워드",
        "content": "a cozy coffee shop, warm lighting, atercolor style",
        "category": "이미지 생성",
        "favorite": False
    }
]

#잘 담겼는지 확인 (테스트용)
print(prompts)