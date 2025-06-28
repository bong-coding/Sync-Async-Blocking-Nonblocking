import asyncio

async def process_input():
    loop = asyncio.get_event_loop()                            # (1) 현재 이벤트 루프
    num = await loop.run_in_executor(None, input,"숫자를 입력하세요: ") # (2) input()을 스레드풀에 던지고
   # 그 사이 루프는 자유
    num = int(num)
    result = num ** 2
    print(f"제곱 결과 : {result}")

asyncio.run(process_input())