#  동기 / 비동기 & 블로킹 / 논블로킹 정리

## ✨ 개요

**동기(Synchronous) vs 비동기(Asynchronous)**, **블로킹(Blocking) vs 논블로킹(Non-blocking)** 개념을 정리하고, 각 조합에 대한 Python 으로 확인하였고 시스템 성능/UX 측면에서의 차이점을 확인함

---

## 1. 개념 정의

### 동기 (Synchronous)
- 작업이 **순차적으로** 실행되며, 이전 작업이 완료될 때까지 다음 작업을 기다림
- 예: 함수 A가 함수 B를 호출 → B가 끝날 때까지 A는 대기

### 비동기 (Asynchronous)
- 작업이 **병렬 또는 이벤트 기반**으로 진행되며, 호출자는 작업 완료 여부에 상관없이 다음 작업 수행

### 블로킹 (Blocking)
- 호출된 함수가 완료될 때까지 **제어권이 함수에 있음** → 호출자는 대기

### 논블로킹 (Non-blocking)
- 호출자가 **제어권을 유지**하며, 작업이 바로 반환되어 다른 일을 계속할 수 있음


----
### 사용자 경헝 & 성능비교

```bash
| 조합                  | 사용자 경험                       | 시스템 성능                                     |
|-----------------------|-----------------------------------|--------------------------------------------------|
| **동기 + 블로킹**     | 응답 느림, 프로그램 멈춤            | CPU 사용 적지만 전체 자원 비효율                  |
| **비동기 + 논블로킹** | 즉각 반응, 병렬 처리 가능           | 고성능, 확장성 우수 (단, 복잡도 ↑)                |
| **동기 + 논블로킹**   | 일부 병렬 가능, CPU 점유 ↑         | 효율적이나 구현 제한 있음                         |
| **비동기 + 블로킹**   | 전체 이벤트 루프 멈춤               | 최악의 조합 – 비효율 및 이벤트 루프 전체 정지 위험 |
```


##  2. 개념 비교

동기 + 블로킹      =>  순차 실행 + 대기       =>  구조 단순, 예측 쉬움  
비동기 + 논블로킹  => 병렬 실행 + 제어권 유지  =>  성능/확장성 뛰어남  
동기 + 논블로킹    => 순서 유지 + 일부 대기 없이 진행 =>  효율성 개선, 흐름 직관적
비동기 + 블로킹    => 비동기 흐름 안에 블로킹 호출 (안티패턴)   =>   특정 작업 완료 보장   

---

## 3. 코드 예제 (Python)

### 비동기 + 논블로킹
- 시작 → 입력 요청 → (다른 작업 가능) → 입력 완료 시 계산 → 출력 → 종료

```python

import asyncio

async def async_non_blocking_task(name):
    print(f"작업 {name} 시작 (대기 시간 2초)")
    await asyncio.sleep(2)
    print(f"작업 {name} 종료")

async def main():
    tasks = [async_non_blocking_task(i) for i in range(3)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
```
### 비동기 + 블로킹 (안티패턴)
- 이벤트 루프 시작 → 블로킹 호출로 정지 → 계산 → 출력 → 종료

```python
import asyncio

async def async_blocking_task(name):
    print(f"작업 {name} 시작 (대기 시간 2초)")
    await asyncio.sleep(2)
    print(f"작업 {name} 종료")

async def main():
    await async_blocking_task(0)
    await async_blocking_task(1)
    await async_blocking_task(2)

if __name__ == "__main__":
    asyncio.run(main())
```
### 동기 + 블로킹

- 시작 → 입력 대기 → 계산 → 출력 → 종료

```python
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
```

### 동기 + 논블로킹 (threading)
- 시작 → 입력 여부 확인 → 대기 중 다른 작업 → 입력 완료 시 계산 → 종료

```python
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
```


