import math 
def check_invalid(triangle):
    test_case=(1,2,3)
    
    if type(triangle)!=type(test_case):
        return True
    
    for i in triangle :
        if type(i)!=type(1):
            return True
            
    if(((triangle[0]+triangle[1])<triangle[2]) or ((triangle[1]+triangle[2])<triangle[0]) or ((triangle[0]+triangle[2])<triangle[1])):
        return True
    return False

def is_right_triangle(triangle):
    if ((triangle[0]**2+triangle[1]**2==triangle[2]**2) or (triangle[0]**2+triangle[2]**2==triangle[1]**2) or (triangle[2]**2+triangle[1]**2==triangle[0]**2)):
        return True
    else:
        return False

def area(triangle):
    #s=(triangle[0]+triangle[1]+triangle[2])/2.0
    s=perimeter(triangle)/2
    ans= math.sqrt(s*(s-triangle[0])*(s-triangle[1])*(s-triangle[2]))
    return ans

def perimeter(triangle):
    ans=triangle[0]+triangle[1]+triangle[2]
    return ans