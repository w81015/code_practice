[中文版](#簡易記帳程式)

# Simple Accounting Program

## Phase 1: Basic Accounting Function
### Features:
- Input product names.
- Enter `q` to end the program.
- Print all entered products.

### Key Points of the Code:
- Use a `while` loop to wait for user input.
- Use `if` condition to decide when to exit the loop.
- Store product names in a `products` list.

## Phase 2: Adding Price Input
### Features:
- In addition to the product name, the user is also asked to input the product price.
- Print each product and its price.

### Key Points of the Code:
- Create a mini list (name and price) for each product.
- Add the mini list to the larger list `products`.

## Phase 3: Price Type Conversion and Saving
### Features:
- Convert the input price from string to integer.
- Store product names and prices in the `products.csv` file.

### Key Points of the Code:
- Use `int()` to convert the price type.
- Use the `open()` function and `write()` method to write data to a CSV file.

## Phase 4: File Encoding Adjustment and Adding Titles
### Features:
- Add a title row in the CSV file.
- Adjust file encoding to `utf-8-sig` to solve encoding issues.

### Key Points of the Code:
- Write the title row at the beginning of the file writing process.
- Specify the file encoding format.

## Phase 5: Reading Existing Files
### Features:
- Read and display the existing product list before inputting new products.
- Skip the title row of the CSV file.

### Key Points of the Code:
- Use the `open()` function and `read()` method to read the file.
- Handle each line of data with `strip()` and `split()`.

## Phase 6: Checking File Existence
### Features:
- Check if the `products.csv` file exists before starting to input products.
- If it exists, read the file; if not, display a message.

### Key Points of the Code:
- Use `os.path.isfile()` to check if the file exists.
- Decide whether to read the file based on the check result.

---

# 簡易記帳程式

## 第一階段：基本記帳功能
### 功能：
- 輸入商品名稱。
- 輸入`q`結束程式。
- 印出所有輸入的商品。

### 程式碼要點：
- 使用`while`迴圈等待用戶輸入。
- 利用`if`條件判斷來決定何時退出迴圈。
- 將商品名稱存儲在`products`列表中。

## 第二階段：增加價格輸入
### 功能：
- 除了商品名稱，還要求用戶輸入商品價格。
- 印出每個商品及其價格。

### 程式碼要點：
- 為每個商品創建一個小清單（名稱和價格）。
- 將小清單加入到大清單`products`中。

## 第三階段：價格類型轉換與存檔
### 功能：
- 將輸入的價格從字串轉換為整數。
- 將商品名稱和價格存儲到`products.csv`文件中。

### 程式碼要點：
- 使用`int()`轉換價格類型。
- 使用`open()`函數與`write()`方法將資料寫入CSV文件。

## 第四階段：檔案編碼調整與標題加入
### 功能：
- 在CSV文件中加入標題行。
- 調整檔案編碼為`utf-8-sig`以解決編碼問題。

### 程式碼要點：
- 文件寫入時首先寫入標題行。
- 指定文件編碼格式。

## 第五階段：讀取現有檔案
### 功能：
- 在輸入新商品前，先讀取並顯示現有的商品清單。
- 跳過CSV檔案的標題行。

### 程式碼要點：
- 使用`open()`函數與`read()`方法讀取文件。
- 用`strip()`和`split()`處理每行數據。

## 第六階段：檢查檔案存在
### 功能：
- 在開始輸入商品之前，檢查`products.csv`文件是否存在。
- 如果存在，則讀取文件；如果不存在，則顯示提示信息。

### 程式碼要點：
- 使用`os.path.isfile()`檢查文件是否存在。
- 根據檢查結果決定是否讀取文件。
