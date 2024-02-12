[中文版](#駕照資格檢測程式)

# Driving Qualification Test Program

This piece of code is used to determine whether a user is qualified to drive, based on whether they have driven before and their age, providing corresponding advice or judgment.

## Feature Introduction
- First, it asks the user whether they have driven before.
- The user needs to answer with `yes` or `no`, other responses are not accepted.
- Then, it asks for the user's age.
- Based on whether the user has driven and their age, it gives one of four different responses.

## Judgment Logic
- **If they have driven and are aged 18 or above**: display `You passed the test`.
- **If they have driven but are under 18**: display `Strange, how could you have driven before?`.
- **If they haven't driven and are aged 18 or above**: display `You can take the driving test now`.
- **If they haven't driven and are under 18**: display `Good, in a few years you can take the driving test`.

## Notes
- The program strictly checks the input, only accepting `yes` or `no` as answers, otherwise, it will remind the user and terminate the program.
- Uses `raise SystemExit` to gracefully end the program if the user's response is not as expected.

This program is a basic practice of conditional judgment, suitable for beginners to learn how to make decisions based on user input.

---

# 駕照資格檢測程式

這段程式碼用於檢測用戶是否符合駕駛資格，根據用戶是否開過車和他們的年齡來給出相應的建議或評判。

## 功能簡介
- 首先詢問用戶是否開過車。
- 需要用戶輸入`有`或`沒有`，不接受其他回答。
- 接著詢問用戶的年齡。
- 根據用戶是否開過車和年齡，給出四種不同的回應。

## 判斷邏輯
- **如果開過車且年齡大於等於18**：顯示`你通過測驗了`。
- **如果開過車但年齡小於18**：顯示`奇怪，你怎麼會開過車`。
- **如果沒開過車且年齡大於等於18**：顯示`你可以考駕照了`。
- **如果沒開過車且年齡小於18**：顯示`很好，再過幾年就可以考駕照了`。

## 注意事項
- 程式中對輸入的檢查很嚴格，只接受`有`或`沒有`作為答案，否則會提醒用戶並終止程式。
- 使用`raise SystemExit`來優雅地結束程式，如果用戶的回答不在預期之內。

此程式為基本的條件判斷練習，適合初學者學習如何根據用戶輸入做出決策。
