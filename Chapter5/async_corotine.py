import asyncio
import time
from random import randint

# Coroutine for start_state
async def start_state():
    print('Start State called\n')
    input_value = randint(0, 1)
    await asyncio.sleep(1)
    if input_value == 0:
        result = await state2(input_value)
    else:
        result = await state1(input_value)
    print('Resume of the Transition:\nStart State calling' + result)

# Coroutine for state1
async def state1(transition_value):
    output_value = 'State 1 with transition value = %s\n' % transition_value
    input_value = randint(0, 1)
    await asyncio.sleep(1)
    print('...evaluating...')
    if input_value == 0:
        result = await state3(input_value)
    else:
        result = await state2(input_value)
    return output_value + 'State 1 calling %s' % result

# Coroutine for state2
async def state2(transition_value):
    output_value = 'State 2 with transition value = %s\n' % transition_value
    input_value = randint(0, 1)
    await asyncio.sleep(1)
    print('...evaluating...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await state3(input_value)
    return output_value + 'State 2 calling %s' % result

# Coroutine for state3
async def state3(transition_value):
    output_value = 'State 3 with transition value = %s\n' % transition_value
    input_value = randint(0, 1)
    await asyncio.sleep(1)
    print('...evaluating...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await end_state(input_value)
    return output_value + 'State 3 calling %s' % result

# Coroutine for end_state
async def end_state(transition_value):
    output_value = 'End State with transition value = %s\n' % transition_value
    print('...stop computation...')
    return output_value

# Main function to simulate the finite state machine
if __name__ == '__main__':
    print('Finite State Machine simulation with Asyncio Coroutine')
    asyncio.run(start_state())
