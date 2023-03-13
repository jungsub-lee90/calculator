## 0313 palindrome algorithm
```python 
#1
def palindrome(words) :
  for w in range(len(words)//2) :
    if words[w] != words[-(1+w)]:
      return False
    else :
      return True
palindrome('level') 


#2 시퀀스 객체 문법 활용
word = 'mom'
## [::-1] == [시작인덱스:끝인덱스:step] , -1은 끝에서부터
list(word) == list(word)[::-1]


#3 reversed 함수 사용
list(word) == list(reversed(word))

#4 join 문 활용

word == ''.join(word)[::-1]
word == ''.join(list(reversed(word)))

```
