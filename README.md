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
- 要加圖片的話，可以通過 `<img src="./001-img-1.png">` 這樣的語法嵌入到 `001-q.html`中。
	- 即html語法：`<img src="圖片地址">`，'./'表示目前的資料夾
- 這個圖片要放在同一個資料夾裡，並取好名字
- 在問題檔案中，如果答案選項具有以下特徵，Quail 將自動被辨識：
	1. 由單個大寫字母（A、B、C 等）組成，
	2. 接在`<br />`後面，以及 
	3. 後面接著 ')' 或 '.' 例如
	```
	A. Quail
	B. Cockatoo
	C. Parakeet
	D. Magpie
	```

- 可以用chrome/safari/edge打開這個html檔，預覽一下編輯效果

## 題目標籤

- 標籤和子標籤允許在多個軸上對問題進行分類。
- 編輯 `index.json`，調整每個題目的次專科。

