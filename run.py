import itertools
import json
import timeit

from schema import schema

def build_query(heritage, subquery='{ value }'):
    if heritage:
        branchingFactor = heritage[-1]
        return build_query(heritage[:-1], f'{{ children(branchingFactor: {branchingFactor}) {subquery}value }} ')
    else:
        return f'{{ root {subquery}}}'

def fixed_sum_sequences(N):
    if N == 0:
        yield []
    else:
        for M in range(N):
            for s in fixed_sum_sequences(M):
                yield [N-M] + s

def sequences():
    for N in itertools.count():
        for s in fixed_sum_sequences(N):
            yield s

max_query_time = None
for s in ([2**(s_i-1) for s_i in s] for s in sequences()):
    query = build_query(s)
    query_time = timeit.timeit(lambda: schema.execute(query), number=1)
    if max_query_time is None or max_query_time < query_time:
        max_query_time = query_time
        print(query_time, s)
