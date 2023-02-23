def out(fn):
    def inner(arg):
        print('id_inner:{}'.format(id(inner)))
        return '呵呵{}'.format(fn(arg))
    return inner

@out
def fn(arg):
    arg += 10
    return arg**2

fn(1)

print('id_fn:',id(fn))
print("fn(1)", fn(1))
print('id_fn(1):',id(fn(1)))
