# python3 -i  original.py
# sg = subgen()
# g = delegator(sg)
# g.send('OK')
# g.send(123)
# g.throw(BlaBlaException)




def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class BlaBlaException(Exception):
    pass



def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            # print('Ku-ku!!!')
            break
        else:
            print('........', message)

    return 'Returned from subgen()'


@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)
    result = yield from g
    print(result)
