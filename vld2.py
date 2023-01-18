def func1(arg1, arg2):
    var13 = func2(arg2, arg1)
    var18 = func7(arg1, var13)
    var25 = var21(arg1, var18)
    var26 = func13()
    var27 = var25 ^ arg2
    var28 = ((var27 | ((var27 + 903402703) + var13 - (467 ^ var25) | var18 + var27 + ((var25 + var18) - ((var26 | -1783718949 + var18 - var18 + var13) ^ var27 | arg1) | 447192821))) & -138) - 806 - (var13 & var13)
    result = var13 | var28
    return result
def func13():
    func11()
    result = len(xrange(7))
    func12()
    return result
def func12():
    global len
    del len
def func11():
    global len
    len = lambda x : -7
def func10(arg22, arg23):
    var24 = (arg22 | (-448 & (-272604838 - arg22) | arg23 - ((-352 ^ -821548255 ^ arg23) + -775 & arg22) & arg22 + arg23) + -229 ^ -797440001) - (arg22 + (691 | arg22 & 940131969 | 712078859))
    result = -1570504574 - -424118884
    return result
def func9():
    closure = [9]
    def func8(arg19, arg20):
        closure[0] += func10(arg19, arg20)
        return closure[0]
    func = func8
    return func
var21 = func9()
def func7(arg14, arg15):
    var16 = 0
    for var17 in range(49):
        var16 += arg14 + 0 & var16
    return var16
def func2(arg3, arg4):
    if arg4 < arg4:
        var9 = class3()
    else:
        var9 = class5()
    for var10 in range(28):
        var9.func4(arg4, arg4)
    var11 = arg4 + (1579899761 ^ 371) ^ arg3 & arg3 - arg4 | 1705225277
    var12 = arg4 & 706
    result = var12 & var12 + ((var11 ^ (arg3 ^ 372)) | var11) & arg3 & -406 ^ var11 - var12
    return result
class class5(object):
    def func4(self, arg7, arg8):
        result = (arg8 + -543290021) & (-1 + arg8) + arg8
        return result
class class3(object):
    def func4(self, arg5, arg6):
        result = -1 + (-960848875 & arg5 + arg6)
        return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 14'
    print 'arg_number: 29'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
