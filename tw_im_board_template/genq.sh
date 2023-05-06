#!/bin/bash
# title: genq
# date created: "2023-05-06"

for i in {1..160}; do
  filename=$(printf "%03d-q.html" $i)
  touch $filename
  echo "<p>Question $1:</p>" > $filename
  echo "<br />" >> $filename
  echo "<p>Content</p>" >> $filename
  echo "<br />" >> $filename
  echo "<img src='./001-img-1.jpg'><br />" >> $filename
  echo "<!--圖片的範例如上-->" >> $filename
  echo "<br />" >> $filename
  echo "<p><strong>A. 。</strong></p>" >> $filename
  echo "<p><strong>B. 。</strong></p>" >> $filename
  echo "<p><strong>C. 。</strong></p>" >> $filename
  echo "<p><strong>D. 。</strong></p>" >> $filename
  echo "<p><strong>E. 。</strong></p>" >> $filename
done

for i in {1..160}; do
  filename=$(printf "%03d-s.html" $i)
  touch $filename
  echo "<p>Correct Answer: A - blablabla </p><br />" > $filename
  echo "<!--↑↑↑↑↑正確選項一定要長這樣↑↑↑↑↑-->" >> $filename
  echo "<p>詳解如下</p>" >> $filename
  echo "<img src='./001-img-1.jpg'><br />" >> $filename
  echo "<!--圖片的範例如上-->" >> $filename
done

exit 0


