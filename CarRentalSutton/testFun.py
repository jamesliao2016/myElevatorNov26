# this program is used for function test
import poisEventFun
tt = 0.0
for jj in range(100):
    cc = poisEventFun.poisProb(3,jj)
    print ('number is: %i'%jj)
    print (cc)
    tt+=cc
print('accumulate probability is: %f'%tt)


'''
--- 24.45144510269165 seconds ---
--- 25.427542448043823 seconds ---
--- 9.68396806716919 seconds ---
--- 9.375937461853027 seconds ---


Policy for 19 states changed
Policy improvement 4
Policy for 0 states changed
--- 138.3159999847412 seconds ---



'''