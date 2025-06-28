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
