data = []
count = 0
length_acc = 0
with open('reviews.txt','r') as f:
    for line in f:
        length = len(line)
        length_acc += length
        data.append(line)
        count += 1
        if count % 10000 == 0:
            print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')
length_ave = length_acc / len(data)
print('每筆資料平均長度：', length_ave, '字')
