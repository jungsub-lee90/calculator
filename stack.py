## python stack 자료구조 

class stack :
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items == []
    
    def push (self, item):
        self.items.append(item)
    
    def top (self):
        return self.items[-1]
    
    def size (self):
        return len(self.items)
    def pop (self) : 
        return self.items.pop()

## 글자 억순으로 읽기    
def reverseS(str):
    s = stack()
    reuslt = ''
    for i in str:
        s.push(i)
    while s.is_empty() != True:
        reuslt +=s.pop()
    return reuslt

reverseS('apple')

## 리스트 슬라이스 사용해서 stack 글자 바꾸기

test = 'string'
test[::-1]

arr = [1, 1, 3, 3, 0, 1, 1]


# 리스트 안에 중복 숫자 없는 리스트 만들기
## save는 arr 리스트에 첫번째에 없는 값이면 된다.
def dupRemove(arr):
    answer = []
    save = 'tes'
    for i in arr :
        if save != i:
            save = i 
            answer.append(save)
    return answer
dupRemove(arr)