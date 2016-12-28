# python3
import sys

def InverseBWT(bwt):
    # write your code here
    list1 = list(bwt)
    cnt_map = {}
    map1 = {}
    for i in range(len(bwt)):
    	if not bwt[i] in cnt_map:
    		cnt_map[bwt[i]] = 1
    	else:
    		cnt_map[bwt[i]] += 1
    	list1[i] += str(cnt_map[bwt[i]])
    	map1[list1[i]] = None
    keys = list(cnt_map.keys())
    keys.sort()
    index = 0
    for i in keys:
    	count = cnt_map[i]
    	for j in range(count):
    		map1[i+str(j+1)] = index
    		index += 1
    rev = "$"
    i = 0
    while 1:
    	rev += list1[i][0]
    	i = map1[list1[i]]
    	if list1[i][0] == '$':
    		break
    return rev[::-1]


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
