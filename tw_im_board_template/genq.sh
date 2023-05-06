#!/bin/bash
# title: genq
# date created: "2023-05-06"

for i in {1..160}; do
  filename=$(printf "%03d-q.html" $i)
  touch $filename
  echo "<p>Question $i:<br />" > $filename
  echo "<p>題幹<br />" >> $filename
  echo "<br />" >> $filename
  echo "<img src='./001-img-1.jpg'><br />" >> $filename
  echo "<!--圖片的範例如上-->" >> $filename
  echo "<br />" >> $filename
  echo "A. Answer <br />" >> $filename
  echo "B. Answer <br />" >> $filename
  echo "C. Answer <br />" >> $filename
  echo "D. Answer <br />" >> $filename
  echo "E. Answer <br />" >> $filename
done

for i in {1..160}; do
  filename=$(printf "%03d-s.html" $i)
  touch $filename
  echo "<p>Correct Answer: A - blablabla <br />" > $filename
  echo "<!--↑↑↑↑↑正確選項一定要長這樣↑↑↑↑↑-->" >> $filename
  echo "<br />" >> $filename
  echo "<!--斷行一定要加一個<br /> 不然會糊成一大段-->" >> $filename
  echo "<img src='./001-img-1.jpg'><br />" >> $filename
  echo "<!--圖片的範例如上-->" >> $filename
  echo "<br />" >> $filename
  echo "詳解在這裡" >> $filename
  echo "</p>" >> $filename
  echo "<!--最後要有一個/p表示這段結束-->" >> $filename
done

exit 0


