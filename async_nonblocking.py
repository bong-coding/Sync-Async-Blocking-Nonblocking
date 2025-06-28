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
