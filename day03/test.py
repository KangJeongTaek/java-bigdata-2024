
f  = open('test.text',mode='w')
f.write('Life is too short\nyou need java')

f.close

f = open('test.text',mode='r')
body = f.read()
f.close

body = body.replace('java','python')

f = open('test.text',mode='w')
f.write(body)


f.close


f = open('test.text',mode='r')
for line in f.readlines():
    if line.find('python') > -1:
        print(line)


def is_odd(number):
    if number % 2 ==0:
        return True
    else:
        return False
    
def avg_numbers(*numbers):
    result = 0
    for i in numbers:
        result += i
    return result / len(numbers)

print(f'{avg_numbers(1,2)}')
print(avg_numbers(1,2,3,4,5))

