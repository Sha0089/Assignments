import numpy as np


# 1. How do you create a NumPy array from the list [1, 2, 3, 4, 5]?
print("1. How do you create a NumPy array from the list [1, 2, 3, 4, 5]?")
arr = np.array([1, 2, 3, 4, 5])
print(arr)


# 2. What is the output of np.array([10, 20, 30, 40])[2]?
print("\n2. What is the output of np.array([10, 20, 30, 40])[2]?")
print(np.array([10, 20, 30, 40])[2])


# 3. Create a NumPy array containing integers from 1 to 10.
print("\n3. Create a NumPy array containing integers from 1 to 10.")
arr = np.arange(1, 11)
print(arr)


# 4. Create a NumPy array containing five zeros.
print("\n4. Create a NumPy array containing five zeros.")
arr = np.zeros(5)
print(arr)


# 5. Create a 3 x 3 NumPy array containing only ones.
print("\n5. Create a 3 x 3 NumPy array containing only ones.")
arr = np.ones((3, 3))
print(arr)


# 6. What is the shape of np.array([[1, 2, 3], [4, 5, 6]])?
print("\n6. What is the shape of np.array([[1, 2, 3], [4, 5, 6]])?")
print(np.array([[1, 2, 3], [4, 5, 6]]).shape)


# 7. What is the number of dimensions of np.array([[1, 2], [3, 4], [5, 6]])?
print("\n7. What is the number of dimensions of np.array([[1, 2], [3, 4], [5, 6]])?")
print(np.array([[1, 2], [3, 4], [5, 6]]).ndim)


# 8. Given arr = np.array([10, 20, 30, 40, 50]), extract the elements from index 1 to index 3.
print("\n8. Given arr = np.array([10, 20, 30, 40, 50]), extract the elements from index 1 to index 3.")
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])


# 9. Given arr = np.array([1, 2, 3, 4, 5]), multiply every element by 10.
print("\n9. Given arr = np.array([1, 2, 3, 4, 5]), multiply every element by 10.")
arr = np.array([1, 2, 3, 4, 5])
print(arr * 10)


# 10. Find the sum, mean, maximum, and minimum of np.array([12, 5, 8, 20, 15]).
print("\n10. Find the sum, mean, maximum, and minimum of np.array([12, 5, 8, 20, 15]).")
arr = np.array([12, 5, 8, 20, 15])
print("Sum:", arr.sum(), "| Mean:", arr.mean(), "| Max:", arr.max(), "| Min:", arr.min())


# 11. Given arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), extract only the even numbers.
print("\n11. Given arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), extract only the even numbers.")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr[arr % 2 == 0])


# 12. Sort np.array([5, 2, 8, 1, 9, 3]) in ascending order.
print("\n12. Sort np.array([5, 2, 8, 1, 9, 3]) in ascending order.")
arr = np.array([5, 2, 8, 1, 9, 3])
print(np.sort(arr))


# 13. Find the indices of elements greater than 50 in np.array([10, 60, 30, 80, 45, 90]).
print("\n13. Find the indices of elements greater than 50 in np.array([10, 60, 30, 80, 45, 90]).")
arr = np.array([10, 60, 30, 80, 45, 90])
print(np.where(arr > 50)[0])


# 14. Reshape np.array([1, 2, 3, 4, 5, 6]) into a 2 x 3 array.
print("\n14. Reshape np.array([1, 2, 3, 4, 5, 6]) into a 2 x 3 array.")
arr = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
print(arr)


# 15. Given two arrays [1, 2, 3] and [4, 5, 6], perform element-wise addition, subtraction, multiplication, and division.
print("\n15. Given two arrays [1, 2, 3] and [4, 5, 6], perform element-wise addition, subtraction, multiplication, and division.")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Add:", a + b, "| Sub:", a - b, "| Mul:", a * b, "| Div:", a / b)


# 16. Perform matrix multiplication on [[1, 2], [3, 4]] and [[5, 6], [7, 8]].
print("\n16. Perform matrix multiplication on [[1, 2], [3, 4]] and [[5, 6], [7, 8]].")
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print(m1 @ m2)


# 17. Find the transpose of [[1, 2, 3], [4, 5, 6]].
print("\n17. Find the transpose of [[1, 2, 3], [4, 5, 6]].")
mat = np.array([[1, 2, 3], [4, 5, 6]])
print(mat.T)


# 18. Replace all values greater than 3 with 100 in np.array([1, 2, 3, 4, 5]).
print("\n18. Replace all values greater than 3 with 100 in np.array([1, 2, 3, 4, 5]).")
arr = np.array([1, 2, 3, 4, 5])
arr[arr > 3] = 100
print(arr)


# 19. Create a 5 x 5 array containing numbers from 1 to 25 and extract the second row and third column.
print("\n19. Create a 5 x 5 array containing numbers from 1 to 25 and extract the second row and third column.")
arr = np.arange(1, 26).reshape(5, 5)
print("Second row:", arr[1, :])
print("Third column:", arr[:, 2])


# 20. Given [[10, 20, 30], [40, 50, 60], [70, 80, 90]], find the row sums, column sums, overall mean, and elements greater than 45.
print("\n20. Given [[10, 20, 30], [40, 50, 60], [70, 80, 90]], find the row sums, column sums, overall mean, and elements greater than 45.")
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Row sums:", arr.sum(axis=1))
print("Column sums:", arr.sum(axis=0))
print("Overall mean:", arr.mean())
print("Elements > 45:", arr[arr > 45])


# 21. Create a NumPy array containing all even numbers from 2 to 20.
print("\n21. Create a NumPy array containing all even numbers from 2 to 20.")
print(np.arange(2, 21, 2))


# 22. Create a NumPy array containing 10 equally spaced values between 0 and 1.
print("\n22. Create a NumPy array containing 10 equally spaced values between 0 and 1.")
print(np.linspace(0, 1, 10))


# 23. Given arr = np.array([3, 7, 2, 9, 4, 8]), find the index of the maximum value.
print("\n23. Given arr = np.array([3, 7, 2, 9, 4, 8]), find the index of the maximum value.")
arr = np.array([3, 7, 2, 9, 4, 8])
print(np.argmax(arr))


# 24. Given arr = np.array([10, 20, 30, 40, 50]), reverse the array.
print("\n24. Given arr = np.array([10, 20, 30, 40, 50]), reverse the array.")
arr = np.array([10, 20, 30, 40, 50])
print(arr[::-1])


# 25. Find the unique values in np.array([1, 2, 2, 3, 4, 4, 5]).
print("\n25. Find the unique values in np.array([1, 2, 2, 3, 4, 4, 5]).")
arr = np.array([1, 2, 2, 3, 4, 4, 5])
print(np.unique(arr))


# 26. Count how many elements are greater than 25 in np.array([10, 30, 15, 40, 25, 50]).
print("\n26. Count how many elements are greater than 25 in np.array([10, 30, 15, 40, 25, 50]).")
arr = np.array([10, 30, 15, 40, 25, 50])
print(np.sum(arr > 25))


# 27. Convert the following 1D array into a 3 x 3 array: np.array([1,2,3,4,5,6,7,8,9]).
print("\n27. Convert the following 1D array into a 3 x 3 array: np.array([1,2,3,4,5,6,7,8,9]).")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(3, 3)
print(arr)


# 28. Flatten the array [[1, 2], [3, 4], [5, 6]] into a 1D array.
print("\n28. Flatten the array [[1, 2], [3, 4], [5, 6]] into a 1D array.")
arr = np.array([[1, 2], [3, 4], [5, 6]])
print(arr.flatten())


# 29. Concatenate np.array([1,2,3]) and np.array([4,5,6]).
print("\n29. Concatenate np.array([1,2,3]) and np.array([4,5,6]).")
print(np.concatenate((np.array([1, 2, 3]), np.array([4, 5, 6]))))


# 30. Split np.array([1,2,3,4,5,6]) into three equal parts.
print("\n30. Split np.array([1,2,3,4,5,6]) into three equal parts.")
print(np.split(np.array([1, 2, 3, 4, 5, 6]), 3))


# 31. Find the standard deviation of np.array([10, 20, 30, 40, 50]).
print("\n31. Find the standard deviation of np.array([10, 20, 30, 40, 50]).")
print(np.std(np.array([10, 20, 30, 40, 50])))


# 32. Find the variance of np.array([2, 4, 6, 8, 10]).
print("\n32. Find the variance of np.array([2, 4, 6, 8, 10]).")
print(np.var(np.array([2, 4, 6, 8, 10])))


# 33. Given arr = np.array([1, 2, 3, 4, 5]), calculate the cumulative sum.
print("\n33. Given arr = np.array([1, 2, 3, 4, 5]), calculate the cumulative sum.")
arr = np.array([1, 2, 3, 4, 5])
print(np.cumsum(arr))


# 34. Given arr = np.array([1, 2, 3, 4, 5]), calculate the cumulative product.
print("\n34. Given arr = np.array([1, 2, 3, 4, 5]), calculate the cumulative product.")
arr = np.array([1, 2, 3, 4, 5])
print(np.cumprod(arr))


# 35. Replace all odd numbers with -1 in np.array([1,2,3,4,5,6,7]).
print("\n35. Replace all odd numbers with -1 in np.array([1,2,3,4,5,6,7]).")
arr = np.array([1, 2, 3, 4, 5, 6, 7])
arr[arr % 2 != 0] = -1
print(arr)


# 36. Find the maximum value in each row of [[1,5,3],[8,2,6],[4,9,7]].
print("\n36. Find the maximum value in each row of [[1,5,3],[8,2,6],[4,9,7]].")
arr = np.array([[1, 5, 3], [8, 2, 6], [4, 9, 7]])
print(arr.max(axis=1))


# 37. Find the minimum value in each column of [[5,2,8],[1,7,3],[6,4,9]].
print("\n37. Find the minimum value in each column of [[5,2,8],[1,7,3],[6,4,9]].")
arr = np.array([[5, 2, 8], [1, 7, 3], [6, 4, 9]])
print(arr.min(axis=0))


# 38. Create a 4 x 4 identity matrix using NumPy.
print("\n38. Create a 4 x 4 identity matrix using NumPy.")
print(np.eye(4))


# 39. Generate a 3 x 3 matrix of random integers between 1 and 20.
print("\n39. Generate a 3 x 3 matrix of random integers between 1 and 20.")
rng = np.random.default_rng(42)
print(rng.integers(1, 21, size=(3, 3)))


# 40. Given two NumPy arrays, find the elements that are common to both arrays.
print("\n40. Given two NumPy arrays, find the elements that are common to both arrays.")
a = np.array([1, 2, 3, 4, 5])
b = np.array([3, 4, 5, 6, 7])
print(np.intersect1d(a, b))
students = np.array([
    [18, 85, 78],
    [19, 92, 88],
    [17, 76, 70],
    [20, 81, 84],
    [18, 95, 72],
])

# Exercise 1. Get the shape of the matrix.
print("\nExercise 1. Get the shape of the matrix.")
print(students.shape)


# Exercise 2. Find the average age of students.
print("\nExercise 2. Find the average age of students.")
print(students[:, 0].mean())


# Exercise 3. Extract the Math marks of all students.
print("\nExercise 3. Extract the Math marks of all students.")
print(students[:, 1])


# Exercise 4. Find the highest Science mark.
print("\nExercise 4. Find the highest Science mark.")
print(students[:, 2].max())


# Exercise 5. Get the details of the student who scored more than 90 in Math.
print("\nExercise 5. Get the details of the student who scored more than 90 in Math.")
print(students[students[:, 1] > 90])


# Exercise 6. Increase the Math marks of all students by 5.
print("\nExercise 6. Increase the Math marks of all students by 5.")
updated_math = students.copy()
updated_math[:, 1] += 5
print(updated_math)


# Exercise 7. Find how many students are younger than 19.
print("\nExercise 7. Find how many students are younger than 19.")
print(np.sum(students[:, 0] < 19))


# Exercise 8. Calculate the average marks in each subject (column-wise mean).
print("\nExercise 8. Calculate the average marks in each subject (column-wise mean).")
print("Mean [Math, Science]:", students[:, 1:].mean(axis=0))


# Exercise 9. Get the data of students who scored at least 80 in both subjects.
print("\nExercise 9. Get the data of students who scored at least 80 in both subjects.")
print(students[(students[:, 1] >= 80) & (students[:, 2] >= 80)])


# Exercise 10. Replace all Science marks below 75 with 0.
print("\nExercise 10. Replace all Science marks below 75 with 0.")
updated_sci = students.copy()
updated_sci[updated_sci[:, 2] < 75, 2] = 0
print(updated_sci)
