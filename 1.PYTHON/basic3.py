# my_library.py
# 도서관 프로그램

class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} | {self.author} | {self.isbn} | {self.year} | {'대출중' if self.is_borrowed else '비치중'}"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"{self.name} ({self.member_id})"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def register_member(self, member):
        self.members[member.member_id] = member

    def search_books(self, keyword, by='title'):
        result = []
        for book in self.books.values():
            if by == 'title' and keyword.lower() in book.title.lower():
                result.append(book)
            elif by == 'author' and keyword.lower() in book.author.lower():
                result.append(book)
            elif by == 'isbn' and keyword == book.isbn:
                result.append(book)
        return result

    def borrow_book(self, member_id, isbn):
        if member_id not in self.members:
            print("회원 없음")
            return
        if isbn not in self.books:
            print("책 없음")
            return
        book = self.books[isbn]
        member = self.members[member_id]
        if book.is_borrowed:
            print("이미 대출됨")
            return
        book.is_borrowed = True
        member.borrowed_books.append(isbn)
        print(f"{member.name} → {book.title} 대출")

    def return_book(self, member_id, isbn):
        if member_id not in self.members or isbn not in self.books:
            print("정보 오류")
            return
        member = self.members[member_id]
        book = self.books[isbn]
        if isbn not in member.borrowed_books:
            print("안 빌린 책")
            return
        book.is_borrowed = False
        member.borrowed_books.remove(isbn)
        print(f"{member.name} → {book.title} 반납")

    def member_borrow_status(self, member_id):
        if member_id not in self.members:
            print("회원 없음")
            return
        member = self.members[member_id]
        print(f"{member.name} 대출 목록:")
        if not member.borrowed_books:
            print("없음")
        for isbn in member.borrowed_books:
            print("-", self.books[isbn])

if __name__ == "__main__":
    lib = Library()

    # 책 2권 추가
    b1 = Book("파이썬 입문", "비니", "1111", 2023)
    b2 = Book("AI 기초", "햇살", "2222", 2024)
    lib.add_book(b1)
    lib.add_book(b2)

    # 회원 2명 추가
    m1 = Member("주빈", "m001")
    m2 = Member("사무엘", "m002")
    lib.register_member(m1)
    lib.register_member(m2)

    # 책 검색
    print("\n[도서 검색: 파이썬]")
    result = lib.search_books("파이썬")
    for b in result:
        print(b)

    # 대출
    print("\n[대출]")
    lib.borrow_book("m001", "1111")  # 주빈이 파이썬 책 대출
    lib.borrow_book("m002", "2222")  # 사무엘이 AI 기초 대출

    # 현황
    print("\n[대출 현황]")
    lib.member_borrow_status("m001")
    lib.member_borrow_status("m002")

    # 반납
    print("\n[반납]")
    lib.return_book("m001", "1111")
    lib.return_book("m001", "3333")  # 없는 책 반납 시도

    # 최종 현황
    print("\n[최종 대출 현황]")
    lib.member_borrow_status("m001")
    lib.member_borrow_status("m002")