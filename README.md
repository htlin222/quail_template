# README

- 本地的考古題做題軟體推薦: Quail (鵪鶉) 似台語發音`過喔`
- 軟體首頁： [Quail - Question bank browser](https://thedabblingduck.github.io/quail/)

- 下載連結 [Release 0.1.14 · TheDabblingDuck/quail](https://github.com/TheDabblingDuck/quail/releases/tag/v0.1.14)

- Mac第一次打開會遇到「無法辨識開發者，你應該要把它丟到垃圾桶」，解決方法：
	- [打開來自未識別開發者的 Mac App - Apple 支援 (台灣)](https://support.apple.com/zh-tw/guide/mac-help/mh40616/mac)
	- 如下圖，選擇「強制打開」就好


![強制打開](https://i.imgur.com/BnTzIKu.png)


## 編輯題目

- 以Markdown編輯題目，按照以下格式:

	- 每題以`## Question 1:`開頭，
	- 選項用`- A. `，記得大寫，後面有一個`.` 前後都要空一行，如圖
	- 答案用`### Correct Answer: A - blabla` 注意字母要大寫
	- 後接詳解
	
![Result](https://i.imgur.com/cQtuFIi.png)
- 推薦使用 [Hackmd](https://hackmd.io/@htlin222/template/edit)來編輯，想貼上圖片的話，只要ctrl/cmd + C 複製圖片，用截圖的方式，最後ctrl/cmd + V 貼上，就會自動幫忙上傳圖片到圖床

- 下載整個repo，按右上角的`<>Code🔽` -> `🤐 Download ZIP`
- 解壓縮後**複製** `tw_im_board_template` 這個資料夾，重新命名為 `內專1xx年`
- 將寫好的Markdown檔案放進這個資料夾
- 在這個資料夾裡執行以下程式
	```
	python magic.py
	```
- 所有的題目對都生成完了 

## 按次專科分類

- 編輯 `index.yaml`檔案，按照題號寫start、end
- 執行 `python index.py`，就會自動產生 `index.json`

```
- sub: "心臟科"
  start: 001
  end: 020

- sub: "胸腔科"
  start: 021
  end: 040

- sub: "肝膽腸胃科"
  start: 041
  end: 060

- sub: "腎臟科"
  start: 061
  end: 070

- sub: "感染科"
  start: 071
  end: 080

- sub: "內分泌科"
  start: 081
  end: 090

- sub: "風濕免疫科"
  start: 091
  end: 100

- sub: "血液腫瘤科"
  start: 101
  end: 120

- sub: "神經科"
  start: 121
  end: 130

- sub: "精神科"
  start: 131
  end: 140

- sub: "皮膚科"
  start: 141
  end: 150

- sub: "其他科"
  start: 151
  end: 160
```
