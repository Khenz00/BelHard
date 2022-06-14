import calcc



def test_add():
    if calcc.add(5,9)==14:
        print('add ok')
    else:
        print('add fail')

def test_sub():
    if calcc.sub(9,5)==4:
        print('sub ok')
    else:
        print('sub fail')
def test_mul():
    if calcc.mul(3,4)==12:
        print('mul ok')
    else:
        print('mul fail')

def test_div():
    if calcc.div(10,5)==2:
        print('div ok')
    else:
        print('div fail')

test_add()
test_sub()
test_mul()
test_div()