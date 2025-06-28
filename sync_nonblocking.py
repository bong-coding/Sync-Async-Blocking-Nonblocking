import threading
import time

def sync_non_blocking_task(name):
    print(f"작업 {name} 시작 (대기 시간 2초)")
    time.sleep(2)  
    print(f"작업 {name} 종료")

def main():
    threads = [threading.Thread(target=sync_non_blocking_task, args=(i,)) for i in range(3)]
    for thread in threads:
        thread.start()  
    for thread in threads:
        thread.join()  

if __name__ == "__main__":
    main()
