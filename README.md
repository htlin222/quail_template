# README

# 說明

- 本地的考古題做題軟體推薦: Quail
- 軟體首頁： [Quail - Question bank browser](https://thedabblingduck.github.io/quail/)

- 下載連結 [Release 0.1.14 · TheDabblingDuck/quail](https://github.com/TheDabblingDuck/quail/releases/tag/v0.1.14)

- Mac第一次打開會遇到「無法辨識開發者，你應該要把它丟到垃圾桶」，解決方法：
	- [打開來自未識別開發者的 Mac App - Apple 支援 (台灣)](https://support.apple.com/zh-tw/guide/mac-help/mh40616/mac)
	- 如下圖，選擇「強制打開」就好


![強制打開](https://i.imgur.com/BnTzIKu.png)


## 編輯題目

- 下載整個repo，按右上角的`<>Code🔽` -> `🤐 Download ZIP`
- 解壓縮後**複製** `tw_im_board_template` 這個資料夾，重新命名為 `內專1xx年`
- 題庫由 HTML 檔案組成，這些檔案可以在文字處理器中創建，推薦用[VSCode](https://code.visualstudio.com/download)。
	- 選擇`檔案` -> `開啟資料夾` -> `內專1xx年`
- 每個題目以“-q.html”結尾，詳解以“-s.html”結尾
- 為問題 #1 和詳解 #1 創建一個包含檔案 `001-q.html` 和 `001-s.html` ，下一個問題/詳解對將命名為 `002-q.html` 和 `002-s.html` ，依此類推。
- 要加圖片的話，可以通過 `<img src="./001-img-1.jpg"><br />` 這樣的語法嵌入到 `001-q.html`中。
	- 即html語法：`<img src="圖片地址">`，'./'表示目前的資料夾
- 這個圖片要放在同一個資料夾裡，並取好名字
- 在問題檔案中，如果答案選項具有以下特徵，Quail 將自動被辨識：
	1. 由單個大寫字母（A、B、C 等）組成
	2. 在這行的第一個字
	3. 後面接著 ')' 或 '.' 例如
	```
	<p>A. Quail</p>
	<p>B. Cockatoo</p>
	<p>C. Parakeet</p>
	<p>D. Magpie</p>
	```

- 在vscode裡安裝[HTML Preview](https://marketplace.visualstudio.com/items?itemName=george-alisson.html-preview-vscode) 這樣可以即時預覽編輯效果
![HTML preview](https://i.imgur.com/K44uGYK.png)
![demo](https://i.imgur.com/fARqflr.png)

## 如果說，窩不會用html...

- 可以用ChatGPT幫你:
	```
	formatting the <text> in html as the same format like  example, include <p> <br />
	export in a code box, no explanation
	here is an example:
	'''
	<p>Question $Number:<br />
	<p>content<br />
	<br />
	<p><strong>A. 。</strong></p>
	<p><strong>B. 。</strong></p>
	<p><strong>C. 。</strong></p>
	<p><strong>D. 。</strong></p>
	<p><strong>E. 。</strong></p>
	'''
	now, the text is:
	<題目>

	```
### 詳解的部分: 
```
formating in easily reading html 
'''
內容
'''
```

## 題目標籤

- 標籤和子標籤允許在多個軸上對問題進行分類。
- 編輯 `index.json`，調整每個題目的次專科。
- 可以用ChatGPT幫你 prompt如下去修改對應的題號，因為字會很多，所以每次卡住的時候，就跟他說`go on`就可以了：

```
create a json file looks like, complete the list from "001"~"160" with consecutive numbers, 
e.g. 001~019 will be 心臟科, all the same 

'''
{
    "001": {"0":"General","1":"心臟科"}, 
    ...
    "020": {"0":"General","1":"胸腔科"},
    ...
    "030": {"0":"General","1":"肝膽腸胃科"},
    ...
    "040": {"0":"General","1":"腎臟科"},
    ...
    "050": {"0":"General","1":"感染科"},
    ...
    "060": {"0":"General","1":"內分泌科"},
    ...
    "070": {"0":"General","1":"風濕免疫科"},
    ....
    "080": {"0":"General","1":"血液腫瘤科"},
    ....
    "090": {"0":"General","1":"神經科"},
    ....
    "100": {"0":"General","1":"神經科"}, 
    ....
    "150": {"0":"General","1":"精神科"},
    ....
    "152": {"0":"General","1":"皮膚科"},
    ....
    "156": {"0":"General","1":"其他科"},
    ....
    "160": {"0":"General","1":"其他科"},
}
'''
```

- 將產生好的結果貼到`index.json`裡

