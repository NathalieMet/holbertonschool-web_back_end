#!/usr/bin/env python3
"""def wait_n"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that waits for a random delay and returns it."""
    delays = []

    async def helper():
        """Helper function to gather the results."""
        nonlocal delays
        delay = await wait_random(max_delay)
        delays.append(delay)

    await asyncio.gather(*[helper() for _ in range(n)])

    return sorted(delays)
