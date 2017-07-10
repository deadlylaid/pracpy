# pracpy
=============
*******
python version 3.6.1

## decorator
==============

[파이썬 데코레이터](http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0-decorator/)

- 새로 알게된 사실
    - 클래스형식의 데코레이터는 사실 그렇게 많이 쓰이지는 않는다.
    - 파이썬에는 로그를 쉽게 해주는 라이브러리 `logging`이 있다.(import logging)
        - `logging.basicConfig()`는 로그를 남기게 될 파일의 설정을 할 수 있다.
        - `logging.info`는 로그 레벨의 단위이며 어떤 식으로 로그를 남길지 설정할 수 있다.
    - 하나의 함수에 다수의 `decorator`를 붙일 수 있지만 wrapper 함수가 다른 wrapper 함수를 리턴하면서 로그가 알맞지 않게 생성되는 문제가 있다.
        - 이 문제를 해결하기 위해 `wraps`함수를 사용한다(from functools import wraps)
