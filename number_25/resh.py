def p(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def d_list(x):
    dd = []
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            dd.append(i)
            dd.append(x//i)
    return sorted(dd)

def z_8(x):
    for i in range(2, int(x**0.5)+1):
        if x%i == 0 and not p(x//i):
          return False
    return True




def num1():
    for i in range(345_123, 345_156+1):
        dd = d_list(i)
        if len(dd)==4:
            print(dd)

def num2():
    for i in range(4_567_234, 4_567_322+1):
        if p(i):
            print(i)

def num3():
    mx = 0
    k=0
    for x in range(125697,190234):
        for i in range(2, int(x**0.5)+1):
            if p(i) and p(x//i) and i*(x//i)==x and i != x//i:
                k+=1
                mx=max(mx, x)
    print(k, mx)
def num4():
    for x in range(110_000_000//2, 111_000_000//2+1):
        if p(int(x**0.5)) and (int(x**0.5))**2 == x:
            print(x, int(x**0.5))
                
def num5():
    for xx in range(63_000_000, 75_000_000+1):
        x = xx
        while x % 2 == 0:
            x //=2
        if int(x**0.25)**4 == x and p(int(x**0.25)) and x > 1:
            print(xx, str(x)[-5:], x)

def num6():
    for a in range(0, 20, 2):
        for b in range(1, 21, 2):
            z = 2*(3**a * 6**b)
            if 410_000_000 <= z <= 620_000_000:
                print(z, a*b)
                
def num7():
    for x in range(12_000_000, 12_010_000):
        if len(d_list(x)) >= 4:
            d = d_list(x)
            s = d[-1]+d[-2]+d[-3]+d[-4]
            if str(s).count('9')>=3 and str(s)[-1] == str(s)[-2]:
                print(x, s)

def num8():
    count = 0
    s = 0
    for k in range(1, 100):
        if z_8(650_000_000+k):
            count+=1
            s+=k
            if count==8:
                break
    print(s)
  
def num9():
    
    #34*62*42
    #34
    for i in range(1, 1_000_001):
        if str(i)[:2]=='34' and '62' in str(i)[2:]:
            print(i)



num3()