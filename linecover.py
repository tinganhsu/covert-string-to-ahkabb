import os
if os.path.isfile("list.txt"):
	route = "list.txt"
else:
	route = input("Enter list location :")

file = open( route, "r", encoding = 'utf8')
count = 0;
wordlist = [];
while True:
	#讀檔案
	line = file.readline();
	#如果已經讀到底就離開
	if not line:
		break;
	#第一個字為:才處理
	if(line[0] == ':'):
		#print ("Line{}: {}".format(count, line.strip())) 
		#利用:當作分割符號
		wordlist.append(line.split(':'))
		#刪除除了最後三個以外的東西   一定都是最後三個會是 '縮寫' '空白' '原始字串'
		del wordlist[count][:-3]
		#把空白那個刪掉
		wordlist[count] = list(filter(None, wordlist[count]))
		#把縮寫的控制.移除
		wordlist[count][0]=wordlist[count][0].replace('.','')
		#把原始字串後方的換行符號刪除
		wordlist[count][1]=wordlist[count][1].replace("\n",'')
		#print(wordlist[count])
		count=count+1
file.close();
#print(wordlist)
#print("lens: }".format(len(wordlist);i++))
paragraph = input("Enter a string :")
for i in range(len(wordlist)):
	#print(wordlist[i][1])
	paragraph=paragraph.replace(wordlist[i][1],wordlist[i][0])

print('After covert: \n {}'.format(paragraph))

os.system("pause")