# 주소록: 중첩 딕셔너리 형태 (이름이 key)
contacts = {
    "임주빈": {
        "전화번호": "010-5549-4937",
        "이메일": "wnqls2148@naver.com",
        "주소": "경기도 용인시"
    },
    "김사무엘": {
        "전화번호": "010-6483-8538",
        "이메일": "rlatkandpf77@naver.com",
        "주소": "경기도 성남시"
    },
    "조다민": {
        "전화번호": "010-7463-3846",
        "이메일": "whekals1198@naver.com",
        "주소": "경기도 수원시"
    }
}

# 특정 사람 정보 접근 예시
print("임주빈의 전화번호:", contacts["임주빈"]["전화번호"])  # 출력: 010-5549-4937

# 전체 주소록 순회 출력 예시
print("\n[딕셔너리 구조 전체 출력 예시]")
for name, info in contacts.items():
    print(f"이름: {name}")
    for key, value in info.items():
        print(f"  {key}: {value}")
    print()

# ------------------- #
# 주소록 프로그램 시작 #
address_book = {}

while True:
    print("\n===== 주소록 프로그램 =====")
    print("1. 추가")
    print("2. 삭제")
    print("3. 검색")
    print("4. 수정")
    print("5. 전체보기")
    print("0. 종료")
    menu = input("메뉴를 선택하세요: ")

    if menu == "1":
        name = input("이름: ")
        phone = input("전화번호: ")
        email = input("이메일: ")
        addr = input("주소: ")
        address_book[name] = {
            "전화번호": phone,
            "이메일": email,
            "주소": addr
        }
        print(f"{name} 연락처가 추가되었습니다.")
        print("\n현재 주소록 딕셔너리:", address_book)

    elif menu == "2":
        name = input("삭제할 이름: ")
        if name in address_book:
            del address_book[name]
            print(f"{name} 연락처가 삭제되었습니다.")
        else:
            print("해당 이름의 연락처가 없습니다.")
        print("\n현재 주소록 딕셔너리:", address_book)

    elif menu == "3":
        name = input("검색할 이름: ")
        if name in address_book:
            info = address_book[name]
            print(f"이름: {name}")
            print("전화번호:", info["전화번호"])
            print("이메일:", info["이메일"])
            print("주소:", info["주소"])
        else:
            print("해당 이름의 연락처가 없습니다.")
        print("\n현재 주소록 딕셔너리:", address_book)

    elif menu == "4":
        name = input("수정할 이름: ")
        if name in address_book:
            print("기존 정보:", address_book[name])
            phone = input("새 전화번호: ")
            email = input("새 이메일: ")
            addr = input("새 주소: ")
            address_book[name] = {
                "전화번호": phone,
                "이메일": email,
                "주소": addr
            }
            print(f"{name} 연락처가 수정되었습니다.")
        else:
            print("해당 이름의 연락처가 없습니다.")
        print("\n현재 주소록 딕셔너리:", address_book)

    elif menu == "5":
        if not address_book:
            print("주소록이 비어 있습니다.")
        else:
            print("\n[전체 연락처 목록]")
            for name, info in address_book.items():
                print(f"- 이름: {name}")
                print(f"  전화번호: {info['전화번호']}")
                print(f"  이메일: {info['이메일']}")
                print(f"  주소: {info['주소']}\n")
        print("\n현재 주소록 딕셔너리:", address_book)

    elif menu == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 메뉴 번호를 입력하세요.")
        print("\n현재 주소록 딕셔너리:", address_book)
