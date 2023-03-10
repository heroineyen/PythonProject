'''
파일명 : Ex14-1-copyFile.py

파일복사
    원본 -> 버퍼 변수(Memory) -> 복사본
'''
buffer_size = 1024 #1024 byte -> 1 KB 의미
with open('../../Day07/Section13/hello.txt', 'rb') as source:
    with open('hello2.txt', 'wb') as copy:
        while True:
            buffer = source.read(buffer_size)
            if not buffer:
                break
            copy.write(buffer)
print('hello2.txt 파일이 복사 되었습니다')