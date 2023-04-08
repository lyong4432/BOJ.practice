x, y, w, h = map(int, input().split())
ans = [w-x,h-y,x,y]
ans.sort()
print(ans[0])
