# python3
import sys

def InverseBWT(bwt):
    # write your code here
    bwt_list = list(bwt)
    cnt_map = {}
    index_map = {}
    for i in range(len(bwt)):
    	if not bwt[i] in cnt_map:
    		cnt_map[bwt[i]] = 1
    	else:
    		cnt_map[bwt[i]] += 1
    	bwt_list[i] += str(cnt_map[bwt[i]])
    	index_map[bwt_list[i]] = None
    keys = list(cnt_map.keys())
    keys.sort()
    index = 0
    for i in keys:
    	count = cnt_map[i]
    	for j in range(count):
    		index_map[i+str(j+1)] = index
    		index += 1
    rev = "$"
    i = 0
    while 1:
    	rev += bwt_list[i][0]
    	i = index_map[bwt_list[i]]
    	if bwt_list[i][0] == '$':
    		break
    return rev[::-1]


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
