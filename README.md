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


