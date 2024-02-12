[中文版](#bmi計算及分類程式)

# BMI Calculation and Classification Program

This Python program is designed to calculate the user's BMI (Body Mass Index) and classify the weight status based on the calculation result.

## Feature Description
- Requests the user to input height (cm) and weight (kg).
- Converts height to meters (m).
- Calculates the BMI value: `BMI = weight(kg) / (height(m) * height(m))`.
- Provides weight classification based on the BMI value.

## BMI Classification Standards
- `BMI < 18.5`: Underweight
- `18.5 <= BMI < 24`: Normal range
- `24 <= BMI < 27`: Overweight
- `27 <= BMI < 30`: Moderately obese
- `30 <= BMI < 35`: Severely obese
- `BMI >= 35`: Very severely obese

## Program Flow
1. First, obtain the input values of height and weight from the user.
2. Convert the input height from centimeters to meters.
3. Calculate the BMI value and convert it to a float type for accuracy.
4. Classify the user's weight status through a series of `if-elif-else` conditional statements based on the BMI value.
5. Output the user's BMI value and its corresponding weight status classification.

This program offers an easy way to understand one's weight status and provides health advice based on the BMI value.

---

# BMI計算及分類程式

此Python程式用於計算用戶的BMI（Body Mass Index，身體質量指數），並根據計算結果將用戶的體重狀態分類。

## 功能說明
- 要求用戶輸入身高（cm）和體重（kg）。
- 將身高轉換成米（m）。
- 計算BMI值：`BMI = 體重(kg) / (身高(m) * 身高(m))`。
- 根據BMI值，給出體重分類。

## BMI分類標準
- `BMI < 18.5`：體重過輕
- `18.5 <= BMI < 24`：正常範圍
- `24 <= BMI < 27`：過重
- `27 <= BMI < 30`：輕度肥胖
- `30 <= BMI < 35`：中度肥胖
- `BMI >= 35`：重度肥胖

## 程式碼流程
1. 首先，從用戶處獲取身高和體重的輸入值。
2. 將輸入的身高從厘米轉換為米。
3. 計算BMI值，並轉換為浮點數型態以提高準確性。
4. 通過一系列`if-elif-else`條件判斷，根據BMI值將用戶的體重狀態分類。
5. 輸出用戶的BMI值及其對應的體重狀態分類。

這個程式提供了一個簡便的方式來了解自己的體重狀態，並能夠根據BMI值獲得相應的健康建議。
