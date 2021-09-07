# python3 -i  original.py
# g = average()
# g.send(None)
# g.send(5)
# g.send(2)
# g.throw(StopIteration)
# g.throw(BlaBlaException)


# from inspect import getgeneratorstate
# g = average()
# getgenerationstate(g)
# g.send(5)
# g.send(6)
# try:
#	g.throw(StopIteration)
# except StopIteration as e:
#	print('Average', e.value)

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


def subgen():
    x = 'Ready to accept message'
    message = yield x
    print('Subgen received:', message)


class BlaBlaException(Exception):
    pass


@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
            break
        except BlaBlaException:
            print('................................')
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)

    return average
