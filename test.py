def consumer():
    r = ''
    print("44444444")
    while True:
        print("55555")
        print(r)
        n = yield r#
        print("aaaaaaaa")
        print(n)
        if not n:
            return
        print("11111111")
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        print("33333333")
        r = c.send(n)
        print("bbbbbbbb")
        print(r)
        print("22222222222")
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
print("9999999999")
print(c)
produce(c)
print("88888888888")