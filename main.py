import pandas as pd
import numpy as np

"""1. **Broadcasting & Array Operations**  
   What is the output of the following code?  
   ```python
   a = np.array([1, 2, 3])
   b = np.array([[1], [2], [3]])
   print(a + b)
   ```
   **Options:**  
   A) `[[2, 3, 4], [3, 4, 5], [4, 5, 6]]`  
   B) `[2, 4, 6]`  
   C) `[[2], [4], [6]]`  
   D) Error (shape mismatch) """


a = np.array([1, 2, 3])
b = np.array([[1], [2], [3]])
print(a + b)

# Ans: A) `[[2, 3, 4], [3, 4, 5], [4, 5, 6]]`

"""** 2. Indexing & Slicing**  
   Given `arr = np.arange(12).reshape(3, 4)`, which code extracts the subarray `[[5, 6], [9, 10]]`?  
   **Options:**  
   A) `arr[1:3, 1:3]`  
   B) `arr[1:, 1:3]`  
   C) `arr[1:3, 1:2]`  
   D) `arr[[1,2], [1,2]]`  
"""

arr = np.arange(12).reshape(3, 4)
print(arr)
print(arr[1:3, 1:3])

# output:
# [[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]]
# [[5 6] [9 10]]


# Ans: A) `arr[1:3, 1:3]`

# 3. **Vectorized Operations**

arr = np.array([-2, -1, 0, 1, 2])

arr = np.where(arr < 0, 0, arr)

print(arr)

#  output: [0 0 0 1 2]

# 4. **Aggregation & NaN Handling**

matrix = np.array([[1, np.nan, 3], [4, 5, np.nan]])
row_means = np.nanmean(matrix, axis=1)

print(row_means)

#  Output: [2.  4.5]


"""5. **Advanced Indexing**

What does this code return?  
   ```python
   data = np.array([10, 20, 30, 40])
   idx = np.array([True, False, True, False])
   print(data[idx])
   ```  
   **Options:**  
   A) `[10, 30]`  
   B) `[True, False, True, False]`  
   C) `[20, 40]`  
   D) Error """

data = np.array([10, 20, 30, 40])
idx = np.array([True, False, True, False])
print(data[idx])


#   Ans: A) `[10, 30]`
#  Output: [10 30]


"""6. **DataFrame Creation & Basics**  
   Create a DataFrame `df` from this dictionary, ensuring the index is `[100, 101, 102]`:  
   ```python
   data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}"""


data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data, index=[100, 101, 102])

print(df)

"""Output: 
                  Name  Age
            100    Alice   25
            101      Bob   30
            102  Charlie   35 """

"""7. **Handling Missing Data**  
   In `df`, replace all `NaN` values in column `'B'` with the **mean of column `'B'`**.  
   ```python
   df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [np.nan, 5, 6]})"""

#  Ans: df['B'] = df['B'].fillna(df['B'].mean())


"""8. **GroupBy & Aggregation**  
   Group `df` by `'Region'`, then compute the **sum of `'Sales'`** and **mean of `'Profit'`** for each group. Reset the index.  
   ```python
   df = pd.DataFrame({
       'Region': ['North', 'South', 'North', 'South'],
       'Sales': [100, 200, 150, 250],
       'Profit': [20, 30, 25, 40]
   })
   ``` """


df = pd.DataFrame({
    'Region': ['North', 'South', 'North', 'South'],
    'Sales': [100, 200, 150, 250],
    'Profit': [20, 30, 25, 40]
})


result = df.groupby('Region').agg({
    'Sales': 'sum',
             'Profit': 'mean'
}).reset_index()

print(result)

""" Output:

            Region  Sales  Profit
         0  North    250    22.5
         1  South    450    35.0"""


"""9. **Merging DataFrames**  
   Merge `orders` and `customers` on `'cust_id'`, keeping **all orders** (even if no customer match exists).  
   ```python
   orders = pd.DataFrame({'order_id': [1, 2], 'cust_id': [101, 102]})
   customers = pd.DataFrame({'cust_id': [101, 103], 'name': ['Alice', 'Bob']})
   ```  """


orders = pd.DataFrame({'order_id': [1, 2], 'cust_id': [101, 102]})
customers = pd.DataFrame({'cust_id': [101, 103], 'name': ['Alice', 'Bob']})

df = pd.merge(orders, customers, on='cust_id', how='left')

print(df)


""" Output:
             order_id  cust_id   name
         0         1      101  Alice
         1         2      102    NaN"""


"""10. **Time Series & Resampling**  
    Convert `'Date'` to datetime, set it as the index, and resample to **monthly frequency**, summing `'Value'`.  
    ```python
    df = pd.DataFrame({
        'Date': ['2023-01-05', '2023-01-15', '2023-02-10'],
        'Value': [10, 20, 30]
    })
    ```  """


df = pd.DataFrame({
    'Date': ['2023-01-05', '2023-01-15', '2023-02-10'],
    'Value': [10, 20, 30]
})

df['Date'] = pd.to_datetime(df['Date'])

df.set_index('Date', inplace=True)

monthly = df.resample('ME').sum()

print(monthly)


""" Output:   
         Date          Value    
         2023-01-31     30
         2023-02-28     30"""
