import threading, queue, time

def reader(q):
    q.put(input())         

q = queue.Queue()
threading.Thread(target=reader, args=(q,), daemon=True).start()
print("숫자를 입력하세요: ", end='', flush=True)

while True:
    try:
        num = int(q.get_nowait())
        print(f"\n제곱 결과 : {num ** 2}")
        break
    except queue.Empty:
        print(".", end='', flush=True)
        time.sleep(0.5)
