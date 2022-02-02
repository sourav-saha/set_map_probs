'''
https://codeforces.com/problemset/problem/1520/D?csrf_token=c386bd52b9199a240ab25179841f51e0

You are given an array 𝑎 of 𝑛 integers. Count the number of pairs of indices (𝑖,𝑗) such that 𝑖<𝑗 and 𝑎𝑗−𝑎𝑖=𝑗−𝑖.

Input
The first line contains one integer 𝑡 (1≤𝑡≤104). Then 𝑡 test cases follow.

The first line of each test case contains one integer 𝑛 (1≤𝑛≤2⋅105).

The second line of each test case contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤𝑛) — array 𝑎.

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 2⋅105.

Output
For each test case output the number of pairs of indices (𝑖,𝑗) such that 𝑖<𝑗 and 𝑎𝑗−𝑎𝑖=𝑗−𝑖.

Example
inputCopy
4
6
3 5 1 4 6 6
3
1 2 3
4
1 3 3 4
6
1 6 3 4 5 6
outputCopy
1
3
3
10
'''


def find_pairs(arr, n):
  my_dict = {}
  count = 0
  
  for i in range(n):
    if (arr[i]-i) in my_dict:
      count += my_dict[(arr[i]-i)]
      my_dict[arr[i]-i] += 1 
    else:
      my_dict[arr[i]-i] = 1 
      
  return count 

if __name__ == "__main__":
  T = int(input().strip())
  for ti in range(T):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(find_pairs(arr, n))
    

#explain: https://www.youtube.com/watch?v=LURJnB0vuvs
