import math
import sys


# ����������
def cos_similarity(vec1, vec2):
    AB = 0
    A2 = 0
    B2 = 0
    for a, b in zip(vec1, vec2):
        AB += a * b
        A2 += a**2
        B2 += b**2
    return AB / (math.sqrt(A2) * math.sqrt(B2))
    
# ŷʽ����
def norm2_distance(vec1, vec2):
    sum = 0
    for a, b in zip(vec1, vec2):
        sum += (a - b)**2
    return math.sqrt(sum)
    
    
# ����̶�
# ��ʽ��abs(a+b) / ((a+b)/2 + epsilon)
def divergence(vec1, vec2):
    sum = 0
    for a, b in zip(vec1, vec2):   
        sum += abs(a - b) / ((a + b)/2 + sys.float_info.epsilon)
    return sum / len(vec1)