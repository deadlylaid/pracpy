# pracpy
*******
python version 3.6.1

## decorator

[파이썬 데코레이터](http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0-decorator/)

- 새로 알게된 사실
    - 클래스형식의 데코레이터는 사실 그렇게 많이 쓰이지는 않는다.
    - 파이썬에는 로그를 쉽게 해주는 라이브러리 `logging`이 있다.(import logging)
        - `logging.basicConfig()`는 로그를 남기게 될 파일의 설정을 할 수 있다.
        - `logging.info`는 로그 레벨의 단위이며 어떤 식으로 로그를 남길지 설정할 수 있다.
    - 하나의 함수에 다수의 `decorator`를 붙일 수 있지만 wrapper 함수가 다른 wrapper 함수를 리턴하면서 로그가 알맞지 않게 생성되는 문제가 있다.
        - 이 문제를 해결하기 위해 `wraps`함수를 사용한다(from functools import wraps)

*******
## generator

[파이썬 제너레이터](http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A0%9C%EB%84%88%EB%A0%88%EC%9D%B4%ED%84%B0-generator/)

- 새로 알게된 사실
    - 제너레이터는 메모리 절약을 위해 많이 쓰임
        - `yield`함수를 이용하면 사용이 가능하다.
        - `next()`함수를 이용하여 필요한 값을 하나씩 출력한다.
        - `list comprehension`을 이용해서 제너레이터를 만들 수 있다.
            - `[ x*10 for i in range(10) ]` > `( x*10 for i in range(10) )`
        - `psutil`은 파이썬 시스템 유틸리티와 실행중인 프로세스의 정보를 얻어오기 위해 사용되는 라이브러리이다.(CPU, memory, disks, network, sensors) 등등
        - python의 `__future__`는 파이썬2를 파이썬3 처럼 사용할 수 있게 해주는 라이브러리이다.
        - `xrange`는 파이썬2에서 지원하는 함수이며 파이썬3에서는 더 이상 지원하지 않는다. xrange의 장점은 데이터의 크기와는 상관없이 memory할당량이 일정하다는 것이다.

*******
## OOP Part 1. 객체 지향 프로그래밍은 무엇인가?

- 새로 알게된 사실
    - `__str__`과 `__repr__`의 차이는 무엇인가?
        - 둘 다 객체를 반환할 때 사용되지만 그 방법이 다르다.

```python

>>>x = 4
>>>repr(x)
'4'
>>>str(x)
'4'

>>>y='pizza'
>>>repr(y)
"'pizza'"
>>>str(y)
'pizza'
```


*******
## OOP Part 2. 클래스와 인스턴스

- 오브젝트란 속성과 같은 여러가지의 데이터와 함수를 포함한 하나의 데이터 구조를 말한다.
    - 데이터를 조금 더 쉽게 다루기 위해 "네임스페이스"라는 것을 이용해 만든 논리적인 집합
- `dir()`은 파이썬의 표준 내장 함수이다. 이 함수는 인자가 없을 경우 모듈 레벨의 지역변수를, 인자가 있을 경우에는 인자의 모든 속성 + 메소드를 보여준다.

*******
## OOP Part 3. 클래스 변수

- 클래스 변수는 클래스 자체에 변수를 지정하여 모든 인스턴스가 공유할 수 있는 변수를 말한다.
    - 파이썬의 오브젝트 참조는 단계에 따라 진행되는데 맨 처음 해당 인스턴스가 갖고 있는 변수를 참조하고, 없다면 해당 클래스의 변수를 참조한다. 여기서도 없다면 수퍼클래스의 인스턴스까지 거슬러 올라가 변수를 참조한다.

*******
## OOP Part 4. 클래스 메도스와 스테틱 메소드

- 클래스 메소드는 모든 인스턴스가 공유하는 데이터를 생성,변경,참초를 위해 존재하는 메소드이다.
- 스테틱 메소드는 클래스나, 인스턴스를 인자로 받지 않는다. 다만 클래스를 통해서도, 인스턴스를 통해서도 호출할 수 있다.
    - 스테틱 메소드는 클래스네임스페이드에 존재는 하지만 일반 함수와 전혀 다를 것이 없다. 호출이 편할 뿐이다.

*******
## OOP Part 5. 상속과 서브 클래스형식의

- 상속은 부모 클래스를 상속받는 하위 클래스를 말한다.
- help()함수는 사용된 함수가 어느 클래스에서 상속되어 온 것인지 확인할 때 쓴다.
- 기존의 부모 클래스에 정의 되어있던 함수의 값들을 중복해서 쓰는 것은 매우 좋지 않다.
```python
 class Parent:
    def __init__(self):
        print("it is paraent")

class SubClass(Parent):
    def __init__(self):
        Parent.__init__(self)

### 다중 상속일 경우
class SubClass2(paraent, SubClass):
    def __init__(self):
        super(SubClass2, self).__init__()
```

*******
## OOP Part 6. 매직 메소드

[메직 매소드](http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-oop-part-6-%EB%A7%A4%EC%A7%81-%EB%A9%94%EC%86%8C%EB%93%9C-magic-method/)

- 더블 언더스코어`__`를 붙여서 불리는 메소드
    - `__str__`, `__add__` 등이 있다.
    - `x + y`를 실행하면 `__add__`메소드가 실행되며 백그라운드에서는 `x.__add__(y)`가 실행되는 상황이 된다.
