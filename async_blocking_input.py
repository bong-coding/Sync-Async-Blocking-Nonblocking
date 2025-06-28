import asyncio

async def process_input():
    num = int(input("숫자를 입력 : "))   # (1) 여전히 블로킹!
    result = num ** 2
    print(f"제곱 결과 : {result}")

asyncio.run(process_input())