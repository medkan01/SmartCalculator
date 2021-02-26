from speechReco import *

def mulDiv(f):
    """
        Calculate multiplications and divisions of a mathematical operation.
        
    Args:
    
        - f (str): Mathematical operation.

    Returns:
    
        - str: Mathematical operation where multiplications and divisions are calculated.
    """
    mulDivOk = False
    i = 0

    while mulDivOk == False:
        if(f.count("x") or f.count("/")):
            if(f[i] == "x"):
                val = float(f.pop(i-1)) * float(f.pop(i))
                f[i-1] = str(val)
                i = 0
            if(f[i] == "/"):
                val = float(f.pop(i-1)) / float(f.pop(i))
                f[i-1] = str(val)
                i = 0
        else:
            mulDivOk = True
        i += 1
    return f

def addSub(f):
    """
        Calculate additions and substractions of a mathematical operation.

    Args:
    
        - f (str): Mathematical operation

    Returns:
    
        - str: Mathematical operation where additions and substractions are calculated.
    """
    addSubOk = False
    i = 0

    while addSubOk == False:
        if(f.count("+") or f.count("-")):
            if(f[i] == "+"):
                val = float(f.pop(i-1)) + float(f.pop(i))
                f[i-1] = str(val)
                i = 0
            if(f[i] == "-"):
                val = float(f.pop(i-1)) - float(f.pop(i))
                f[i-1] = str(val)
                i = 0
        else:
            addSubOk = True
        i += 1
    return f


def calculation(f):
    """
        Calculate a mathematical operation. Multiplications and divisions are calculated first, then additions
        and divisions.

    Args:
        
        - f (str): Mathematical operation.

    Returns:
        
        - float: Result of the mathematical operation.
    """
    try:
        f = mulDiv(f)
        f = addSub(f)
        res = float(f[0])
        return res
    except Exception as e:
        print("Attention! Le calcul est incorrect ou impossible.")