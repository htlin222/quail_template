# README

> [📺 影片介紹](https://youtu.be/FIP1UqfCgOc)

- 本地的考古題做題軟體推薦: Quail (鵪鶉) 似台語發音`過喔`
- 軟體首頁： [Quail - Question bank browser](https://thedabblingduck.github.io/quail/)
- 下載連結 [Release 0.1.14 · TheDabblingDuck/quail](https://github.com/TheDabblingDuck/quail/releases/tag/v0.1.14)

- Mac 第一次打開會遇到「無法辨識開發者，你應該要把它丟到垃圾桶」，解決方法：
  - [打開來自未識別開發者的 Mac App - Apple 支援 (台灣)](https://support.apple.com/zh-tw/guide/mac-help/mh40616/mac)
  - 如下圖，選擇「強制打開」就好

![強制打開](https://i.imgur.com/BnTzIKu.png)

## 編輯題目

- 以 Markdown 編輯題目，按照以下格式:

  - 每題以`## Question 1:`開頭，
  - 選項用`- A.`，記得大寫，後面有一個`.` 前後都要空一行，如圖
  - 答案用`### Correct Answer: A - blabla` 注意字母要大寫
  - 後接詳解

![Result](https://i.imgur.com/cQtuFIi.png)

- 推薦使用 HackMD 來編輯，想貼上圖片的話，只要 ctrl/cmd + C 複製圖片，用截圖的方式，最後 ctrl/cmd + V 貼上，就會自動幫忙上傳圖片到圖床，可以參考
  - [160 題的範例](https://hackmd.io/@htlin222/template/edit)
  - [200 題的範例](https://hackmd.io/@htlin222/template200x/edit)
- 最後下載成 markdown 檔，命名為`內專1xx年.md`

## 次專科考古資料庫

- 每題有三個屬性，一是次專、二是考古題否、三是年份

![編目](https://i.imgur.com/YqvyAx9.png)

- 次專的順序如下：

1. 心臟科
2. 胸腔科
3. 肝膽腸胃科
4. 腎臟科
5. 感染科
6. 考古題
7. 內分泌科
8. 風濕免疫科
9. 血液腫瘤科
10. 神經科
11. 精神科
12. 皮膚科

- 這個列表的範例[GoogleSheet](https://docs.google.com/spreadsheets/d/18ger0mucsSThUfUGwvPBaB106OMgAkDidY1fyW_h-ug/edit?usp=sharing)
- 複製一份，將這年的資料以`csv`的格式下載，並命名為`內專1xx年.csv`

## 魔法 🧚🪄

- 下載整個 repo，按右上角的`<>Code🔽` -> `🤐 Download ZIP`
- 解壓縮後**複製** `template` 這個資料夾，重新命名為 `內專1xx年`
- 將寫好的`內專1xx年.md`檔案放進這個資料夾
- 將編輯好的`內專1xx年.csv`的`csv`檔案放進這個資料夾
- 在這個資料夾裡執行:

```sh
# 第一次執行
make
# 單純重新生成題庫，不再重下載圖片
make again
# 產生範本
make new
```

- 所有的題目對都生成完
- 最後再用quail開啟這個資料夾就可以
