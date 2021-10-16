def max_gap(N):
    xs = bin(N)[2:].strip('0').split('1')
    return max([len(x) for x in xs])


def binary_gap(N):
    return len(max(format(N, 'b').strip('0').split('1')))
