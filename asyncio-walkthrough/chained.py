#!/usr/env/bin python3
# chained.py

import asyncio
import random
import time

async def randint(a, b):
    return random.randint(a, b)

async def part1(n):
    i = await randint(0, 10)
    print(f'part1({n}) sleeping for {i} seconds.')
    await asyncio.sleep(i)
    result = f'result{n}-1'
    print(f'Returning part1({n}) == {result}.')
    return result

async def part2(n, arg):
    i = await randint(0, 10)
    print(f'part2{n, arg} sleeping for {i} seconds.')
    await asyncio.sleep(i)
    result = f'result{n}-2 derived from {arg}'
    print(f'Returning part2{n, arg} == {result}.')
    return result

async def chain(n):
    start = time.monotonic()
    p1 = await part1(n)
    p2 = await part2(n, p1)
    end = time.monotonic() - start
    print(f'-->Chained result{n} => {p2} (took {end:0.2f} seconds).')

async def main(*ns):
    await asyncio.gather(*(chain(n) for n in ns))

if __name__ == '__main__':
    import sys
    random.seed(444)
    ns = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.monotonic()
    asyncio.run(main(*ns))
    end = time.monotonic() - start
    print(f'Program finished in {end:0.2f} seconds.')
