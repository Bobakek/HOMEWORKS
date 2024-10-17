import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    for i in range(1, 6):  # 5 шаров для каждого силача
        await asyncio.sleep(1 / power)  # Задержка, обратно пропорциональная силе
        print(f'Силач {name} поднял {i} шар.')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    # Создание задач для 3 силачей
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 6))


    await task1
    await task2
    await task3


asyncio.run(start_tournament())
