#!/bin/bash
# title: genq
# date created: "2023-05-06"

for i in {1..160}; do
  filename=$(printf "%03d-q.html" $i)
  touch $filename
  echo "<p>Question $i:<br />" > $filename
  echo "<p>題幹<br />" >> $filename
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
  echo "<br />" >> $filename
  echo "詳解在這裡</p>" >> $filename
done

exit 0


