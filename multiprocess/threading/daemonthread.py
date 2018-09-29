import threading, requests, time


def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars')


t1 = threading.Thread(target=getHtml, args=('http://google.com',))
# daemon thread는 main thread가 종료되면 끝이난다.
# threading.Thread 가 실행되는 동안 print("### End ###")를 끝으로
# main thread가 종료되면 subthread가 실행되다가 멈춰버린다.
t1.daemon = True
t1.start()

print("### End ###")
