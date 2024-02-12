[中文版](#評論數據處理---python-文字檔案操作與數據分析)

# Comment Data Processing - Python Text File Manipulation and Data Analysis

This code snippet demonstrates how to use Python for processing text files (such as comment data) and conducting basic data analysis, including calculating the average length of comments, filtering comments under specific conditions, and more.

## Feature Overview
1. **Read Comment File**: Read all comment data from `reviews.txt`.
2. **Basic Data Analysis**:
   - Calculate the total number of comments.
   - Calculate the average length of all comments.
   - Filter out comments that are less than 100 characters long.
   - Filter comments that contain the keyword "good".
3. **High-Frequency Vocabulary Analysis**:
   - Count the frequency of each word.
   - Allow users to query the frequency of a specific word.

## Technical Points
- Use `open` for file reading.
- Utilize list comprehension for efficient data filtering.
- Apply dictionaries for calculating word frequencies.
- Use loops and conditional statements to meet data analysis requirements.

## Code Example
- **Read and Analyze Comments**:
  ```python
  data = []
  with open('reviews.txt', 'r') as f:
      for line in f:
          data.append(line)
  print(len(data)) # Print the number of comments

---

# 評論數據處理 - Python 文字檔案操作與數據分析

這段程式碼展示了如何使用Python處理文字檔案（如評論資料），並進行基本的數據分析，包括計算評論的平均長度、篩選特定條件的評論等。

## 功能概述
1. **讀取評論檔案**: 從`reviews.txt`中讀取所有評論數據。
2. **基本數據分析**:
   - 計算所有評論的總數量。
   - 計算所有評論的平均長度。
   - 篩選出長度小於100字的評論。
   - 篩選包含"good"關鍵字的評論。
3. **高頻詞彙分析**:
   - 計算每個單詞出現的次數。
   - 允許使用者查詢特定單詞的出現次數。

## 技術要點
- 使用`open`進行檔案讀取。
- 利用列表推導式（List Comprehension）進行快速數據過濾。
- 字典（Dictionary）應用於計算單詞頻率。
- 迴圈與條件判斷來處理數據分析的需求。

## 程式碼示例
- **讀取評論並分析**:
  ```python
  data = []
  with open('reviews.txt', 'r') as f:
      for line in f:
          data.append(line)
  print(len(data)) # 印出評論數量
