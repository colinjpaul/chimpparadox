from dec_append import foo, bar, fn

def test_append():
    foo()
    bar()

    f = open(fn, 'rt')
    assert f.read() == 'function calledfunction calledfunction calledfunction calledfunction calledfunction calledfunction calledfunction calledfunction called'
