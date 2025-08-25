# RetouchIT-Numpy-Pandas-Assessment
Technical Assessment that ensures candidates demonstrates practical expertise rather than just theoretical knowledge.


### **NumPy & Pandas Technical Assessment Quiz**  
**Time Limit:** 45 minutes  
**Level:** Intermediate  
**Instructions:** Answer all questions. For coding questions, write concise, efficient code. Assume all required libraries are imported (`import numpy as np`, `import pandas as pd`).

---

#### **Section 1: NumPy (5 Questions)**

1. **Broadcasting & Array Operations**  
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
   D) Error (shape mismatch)  

2. **Indexing & Slicing**  
   Given `arr = np.arange(12).reshape(3, 4)`, which code extracts the subarray `[[5, 6], [9, 10]]`?  
   **Options:**  
   A) `arr[1:3, 1:3]`  
   B) `arr[1:, 1:3]`  
   C) `arr[1:3, 1:2]`  
   D) `arr[[1,2], [1,2]]`  

3. **Vectorized Operations**  
   Replace all negative values in `arr = np.array([-2, -1, 0, 1, 2])` with `0` using a **single vectorized operation**.  
   *(Write the code)*  

4. **Aggregation & NaN Handling**  
   Compute the row-wise mean of `matrix` below, ignoring `NaN` values:  
   ```python
   matrix = np.array([[1, np.nan, 3], [4, 5, np.nan]])
   ```  
   *(Write the code)*  

5. **Advanced Indexing**  
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
   D) Error  

---

#### **Section 2: Pandas (5 Questions)**

6. **DataFrame Creation & Basics**  
   Create a DataFrame `df` from this dictionary, ensuring the index is `[100, 101, 102]`:  
   ```python
   data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
   ```  
   *(Write the code)*  

7. **Handling Missing Data**  
   In `df`, replace all `NaN` values in column `'B'` with the **mean of column `'B'`**.  
   ```python
   df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [np.nan, 5, 6]})
   ```  
   *(Write the code)*  

8. **GroupBy & Aggregation**  
   Group `df` by `'Region'`, then compute the **sum of `'Sales'`** and **mean of `'Profit'`** for each group. Reset the index.  
   ```python
   df = pd.DataFrame({
       'Region': ['North', 'South', 'North', 'South'],
       'Sales': [100, 200, 150, 250],
       'Profit': [20, 30, 25, 40]
   })
   ```  
   *(Write the code)*  

9. **Merging DataFrames**  
   Merge `orders` and `customers` on `'cust_id'`, keeping **all orders** (even if no customer match exists).  
   ```python
   orders = pd.DataFrame({'order_id': [1, 2], 'cust_id': [101, 102]})
   customers = pd.DataFrame({'cust_id': [101, 103], 'name': ['Alice', 'Bob']})
   ```  
   *(Write the code)*  

10. **Time Series & Resampling**  
    Convert `'Date'` to datetime, set it as the index, and resample to **monthly frequency**, summing `'Value'`.  
    ```python
    df = pd.DataFrame({
        'Date': ['2023-01-05', '2023-01-15', '2023-02-10'],
        'Value': [10, 20, 30]
    })
    ```  
    *(Write the code)*  



### **Scoring**  
- **9-10 Correct:** Expert (Strong grasp of vectorization, indexing, and advanced operations)  
- **7-8 Correct:** Proficient (Solid foundation; may need refinement on edge cases)  
- **5-6 Correct:** Intermediate (Understands basics but needs practice on aggregation/merging)  
- **<5 Correct:** Beginner (Review core concepts: indexing, missing data, groupby)  

### **Key Concepts Tested**  
- NumPy: Broadcasting, boolean indexing, aggregation with `NaN`.  
- Pandas: `groupby`/`agg`, merging strategies, time-series resampling, avoiding chained indexing.  

>  **Pro Tip:** Always prefer vectorized operations (`np.where`, `pd.Series.str`) over loops. Use `.loc`/`.iloc` for safe indexing to avoid `SettingWithCopyWarning`!  

