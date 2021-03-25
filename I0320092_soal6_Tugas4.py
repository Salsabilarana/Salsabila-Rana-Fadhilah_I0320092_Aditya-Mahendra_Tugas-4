a = 4     # 4 = 0000 0100
b = 11    # 13 = 0000 1011


#bitwise OR (|)
c = a | b
print('===========OR==========')
print('nilai :',a,' , biner :', format(a,'08b'))
print('nilai :',b,' , biner :', format(b,'08b'))
print('------------------------------ (|)')
print('nilai :',c,' , biner :', format(c,'08b'))

#bitwise (>>)
c = a >> b
print('===========>>==========')
print('nilai :',a,' , biner :', format(a,'08b'))
print('nilai :',b,' , biner :', format(b,'08b'))
print('------------------------------ (>>)')
print('nilai :',c,' , biner :', format(c,'08b'))

#bitwise XOR(^)
c = a ^ b
print('===========XOR==========')
print('nilai :',a,' , biner :', format(a,'08b'))
print('nilai :',b,' , biner :', format(b,'08b'))
print('------------------------------ (^)')
print('nilai :',c,' , biner :', format(c,'08b'))

#bitwise NOT (~)
c = ~a
print('===========NOT==========')
print('nilai :',a,' , biner :', format(a,'08b'))
print('------------------------------ (~)')
print('nilai :',c,' , biner :', format(c,'08b'))

#bitwise AND (&)
c = b & a
print('===========AND==========')
print('nilai :',a,' , biner :', format(a,'08b'))
print('nilai :',b,' , biner :', format(b,'08b'))
print('------------------------------ (&)')
print('nilai :',c,' , biner :', format(c,'08b'))







