import math
import timeit
import random



def collinearPoints(points):
    lines = []
    def delta(a, b):
        if b[0] == a[0]:
            d = float('inf')
        else:
            d = (b[1]-a[1])/(b[0]-a[0])
            d = math.floor(d*1000000)/1000000
        return d

    def sim_test(a, b):
        is_in = []
        not_in = []
        in_flag = 0
        for i in a:
            if i in b:
                is_in.append(i)
                in_flag = 1
            else:
                not_in.append(i)
        for j in b:
            if j not in a:
                not_in.append(j)
        if in_flag == 1:
            res_list = sorted(is_in+not_in, key = lambda n:(n[0], n[1]))
            return res_list, 1
        else:
            return a, 0

    for point in points:
        stan_p = point
        points_with_l = []
        for p in points:
            l = delta(stan_p, p)
            points_with_l.append((p[0], p[1], l))
        sorted_by_l = sorted(points_with_l,key = lambda n:n[2])
        find_key = sorted_by_l[0]
        count = 0
        line = [find_key]
        for i in sorted_by_l:
            if i[2] == find_key[2]:
                count += 1
                line[0] = find_key
                line.append(i)
            else:
                if count >=3:
                    sorted_line = sorted(line, key = lambda  n:(n[0], n[1]))
                    flag = 0
                    for ind in range(len(lines)):
                        exist = lines[ind]
                        put_line, flag = sim_test(exist, sorted_line)
                        lines[ind] = put_line
                    if flag ==0:
                        lines.append(sorted_line)
                find_key = i
                count = 1
    result = []
    for lll in lines:
        res = (lll[0][0], lll[0][1], lll[len(lll)-1][0], lll[len(lll)-1][1])
        result.append(res)
    return result



def correctnessTest(input, expected_output, correct):
    output = collinearPoints(input)
    print(f"collinearPoints({input})\n{output}")
    if output == expected_output: print("Pass")
    else:        
        print(f"Fail - expected output: {expected_output}")
        correct = False
    print()    

    return correct


def simulateNSquareLogN(points):
    points = sorted(points, key=lambda p:(p[1], -p[0]))
    for i in range(0, len(points)):
        slopes = []
        for j in range(i+1, len(points)):
            if points[i][0] == points[j][0]: slopes.append((points[j][0], points[j][1], float('inf')))
            else: slopes.append((points[j][0], points[j][1], (points[j][1]-points[i][1])/(points[j][0]-points[i][0])))
        slopes.sort(key=lambda p:(p[1], p[2], p[0]))
        
        for j in range(1, len(slopes)):
            if slopes[j][2] == slopes[j-1][2]:
                for k in range(5): pass



#Unit Test

if __name__ == "__main__":

    print("Correctness test for collinearPoints()")
    print("For each test case, if your answer does not appear within 5 seconds, then consider that you failed the case")
    print()
    correct = True

    # No collinear sets found, thus return the empty list []
    input = [(0,0),(1,1)]
    expected_output = []
    correct = correctnessTest(input, expected_output, correct)


    input = [(0,0), (1,1), (3,3), (4,4), (6,6), (7,7), (9,9)]
    expected_output = [(0,0,9,9)]    
    correct = correctnessTest(input, expected_output, correct)

    input = [(1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (8,0)]
    expected_output = [(1,0,8,0)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(7,0), (14,0), (22,0), (27,0), (31,0), (42,0)]
    expected_output = [(7,0,42,0)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,-2), (0,-53)]
    expected_output = [(0, -53, 0, 5)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(19000,10000), (18000,10000), (32000,10000), (21000,10000), (1234,5678), (14000,10000)]
    expected_output = [(14000,10000,32000,10000)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(12446,18993), (12798,19345), (12834,19381), (12870,19417), (12906,19453), (12942,19489)]
    expected_output = [(12446,18993,12942,19489)]
    correct = correctnessTest(input, expected_output, correct)


    input = [(0,0), (0,1), (0,2), (0,3), (1,0), (1,1), (1,2), (1,3)]
    expected_output = [(0,0,0,3), (1,0,1,3)]
    correct = correctnessTest(input, expected_output, correct)

    input = [(10000,0), (0,10000), (3000,7000), (7000,3000), (20000,21000), (3000,4000), (14000,15000), (6000,7000)]
    expected_output = [(0, 10000, 10000, 0), (3000, 4000, 20000, 21000)]    
    correct = correctnessTest(input, expected_output, correct)    


    # Case where the same point appears multiple times
    input = [(1,1), (2,2), (3,3), (4,4), (2,0), (3,-1), (4,-2), (0,1), (-1,1), (-2,1), (-3,1), (2,1), (3,1), (4,1), (5,1)]
    expected_output = [(-3, 1, 5, 1), (1, 1, 4, -2), (1, 1, 4, 4)]
    correct = correctnessTest(input, expected_output, correct)    


    print()
    print("Speed test for collinearPoints()")
    if not correct: print("Fail (since the algorithm is not correct)")
    else:
        repeat = 10
        inputLength = 100
        minC, maxC = -1000000, 1000000
        points = [(random.randint(minC, maxC), random.randint(minC, maxC)) for _ in range(inputLength)]
        tCodeToCompare = timeit.timeit(lambda: simulateNSquareLogN(points), number=repeat) / repeat
        tSubmittedCode = timeit.timeit(lambda: collinearPoints(points), number=repeat) / repeat        
        print(f"Average running time of collinearPoints() and simulateNSquareLogN() with {inputLength} points: {tSubmittedCode:.10f} and {tCodeToCompare:.10f}")
        #print(f"{tSubmittedCode / tCodeToCompare}")
        if tSubmittedCode < tCodeToCompare * 3: print("Pass")
        else:
            print("Fail")
        print()
        
