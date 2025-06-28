import time

def sync_blocking_task(name):
    print(f"작업 {name} 시작 (대기 시간 2초)")
    time.sleep(2)  
    print(f"작업 {name} 종료")

def main():
    sync_blocking_task(0)  
    sync_blocking_task(1)  
    sync_blocking_task(2)  

if __name__ == "__main__":
    main()
