#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: gen_temp
# date: "2023-05-06"

with open('text.md', 'w') as f:
    f.write('# title\n\n')
    for i in range(1, 161):
        text = f'''## Question {i}:

題幹

---

- A.
- B.
- C.
- D.
- E.

### Correct Answer: A

詳解如下…

'''
        f.write(text)
