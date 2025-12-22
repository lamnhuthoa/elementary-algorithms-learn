# Bai 6
# Student Sort
# There are N different students having their own student codes and grades. 
# Please find k students having the highest grades in N students
#
# Output:
# k lines are k student codes of k students having the highest grades.
# In case two grades are equal, the priority is for the student with a smaller student code.
# Given that every student code is different.
def compare(student1, student2):
    if student1[1] != student2[1]:
        return student1[1] > student2[1]
    return student1[0] < student2[0]

def merge(L, n1, R, n2, a):
    i = j = k = 0
    while i < n1 and j < n2:
        if compare(L[i], R[j]):
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1

def merge_sort(a, n):
    if n > 1:
        n1 = n // 2
        n2 = n - n1
        L = a[:n1]
        R = a[n1:]
        merge_sort(L, n1)
        merge_sort(R, n2)
        merge(L, n1, R, n2, a)

def sort_student():
    num, num_highest = map(int, input().split())
    a = []

    for i in range(num):
        code, grade = input().split()
        a.append([int(code), float(grade)])
        
    merge_sort(a, num)
    for i in range(num_highest):
        print(a[i][0])

sort_student()