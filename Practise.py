pos = []
neg = []
with open(r'D:\One Drive Daily\OneDrive\FreeLancer\Caglar Project\Text-Sentiment-by-CNN\train.csv', "rb") as f:
    for line in f:
        if line.decode().split(",")[1]=='1':
            pos.append(line.decode().split(",")[2].split('\n')[0])
        if line.decode().split(",")[1] == '0':
            neg.append(line.decode().split(",")[2].split('\n')[0])


with open(r'D:\One Drive Daily\OneDrive\FreeLancer\Caglar Project\Text-Sentiment-by-CNN\train_pos.txt', "w") as f:
    for item in pos:
        f.write("%s\n" % item)

with open(r'D:\One Drive Daily\OneDrive\FreeLancer\Caglar Project\Text-Sentiment-by-CNN\train_neg.txt', "w") as f:
    for item in neg:
        f.write("%s\n" % item)
