def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    a=n
    while k>1:
          a=a*(n-1)
          k=k-1
          n=n-1
    else:
        if k<1:
            a=1
    return a
    "*** YOUR CODE HERE ***"



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    S=0
    while y!=0:
        n=y%10
        S+=n
        y=y//10
    return S
    "*** YOUR CODE HERE ***"



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    '''
    a=String(n)
    b=len(a)
    c=0
    while c<b:
        if str[c]==str[c+1]'''

    while n!=0:
         if n%100==88:
            return True
         else: n=n//10
    return False
    "*** YOUR CODE HERE ***"


