data = []
count = 0
count_less100 = 0
length_acc = 0
with open('reviews.txt','r') as f:
    for line in f:

        length_acc += len(line) # 計算累積字數

        if len(line) < 100: # 篩選<100字的留言
            count_less100 += 1

        data.append(line)
        
        count += 1 # 計算累積留言數
        if count % 100000 == 0:
            print(len(data))

print('檔案讀取完了，總共有', len(data), '筆留言')
length_ave = length_acc / len(data)
print('每筆留言平均長度：', length_ave, '字')
print('有', count_less100, '比留言長度小於100字')

# 老師教的寫法_計算累積字數(另外寫for loop)
length_acc = 0
for d in data:
    length_acc += len(d)
print('每筆留言平均長度：', length_acc/len(data), '字')

# 老師教的寫法_篩選<100字的留言(創造一個新的list)
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('有', len(new), '比留言長度小於100字')
print(new[0])
print(new[1])
