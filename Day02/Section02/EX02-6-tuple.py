'''
파일명 : Ex02-6-tuple.py
튜플
    단일 변수에 여러 항목을 저장하는 데 사용된다.
    순서가 있고, 변경할 수 없는 List
    둥근 괄호로 작성된다.
'''
thistuple = ("피카츄", "라이츄", "파이리") #한 번 선언하면 값 변경이 불가능하다.
print(thistuple)
# 튜플 길이
print(len(thistuple))

# 항목 접근
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:3])

#튜플값 변경 방법 (억지로 변경하는 법)
thistuple = ("피카츄", "라이츄", "파이리")
thiscast = list(thistuple) #casting 또는 형변환
thiscast[1] = "잠만보"
thistuple = tuple(thiscast) #다시 튜플로 바꾸기
print(thistuple)

#튜플 압축풀기
thistuple = ("피카츄", "라이츄", "파이리", "꼬부기")
(p1, p2, p3, p4) = thistuple
print(p1)
print(p2)
print(p3) #줄 삭제는 Ctrl Y
print(p4)

# 두 개 튜플 조인
thistuple1 = ("피카츄", "라이츄", "파이리", "꼬부기")
thistuple2 = ("버터플", "야도란", "파이리", "꼬부기")
thistuple3 = thistuple1 + thistuple2
print(thistuple3)


