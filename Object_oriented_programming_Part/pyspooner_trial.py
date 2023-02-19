import pysnooper

@pysnooper.snoop(prefix="funcTwo ")
def function():
    a=[]
    for i in range(10):
        if i % 2 == 0:
            i += 1
        else:
            i = i **2
        a.append(i)
        print('finish a round')
function()