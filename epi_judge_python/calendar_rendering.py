import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))
Endpoint = collections.namedtuple('Endpoint', ('hour', 'is_start'))

def find_max_simultaneous_events(A: List[Event]) -> int:
    the_hours = []
    the_max= -1
    max_concurrent = 0
    for event in A:
        the_hours.append(Endpoint(event.start, True))
        the_hours.append(Endpoint(event.finish, False))
    
    # [...(4, True), (4, True), (4, False)...]
    the_hours.sort(key=lambda endpoint: (endpoint.hour, not endpoint.is_start))

    for hour in the_hours:
        # iterate and when endpoint.is_start add to max 
        if hour.is_start:
            max_concurrent += 1
            the_max = max(max_concurrent, the_max)
        else:
            max_concurrent -= 1

    return the_max


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
