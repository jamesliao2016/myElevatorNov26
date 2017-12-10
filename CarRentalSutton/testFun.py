# this program is used for function test
import poisEventFun
tt = 0.0
for jj in range(100):
    cc = poisEventFun.poisProb(3,jj)
    print ('number is: %i'%jj)
    print (cc)
    tt+=cc
print('accumulate probability is: %f'%tt)