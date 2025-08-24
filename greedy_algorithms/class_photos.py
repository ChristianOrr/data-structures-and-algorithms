"""
Easy

It's photo day at the local school, and you're the photographer assigned to take class photos.
The class that you'll be photographing has an even number of students,
and all these students are wearing red or blue shirts.
In fact, exactly half of the class is wearing red shirts, and the other half is wearing blue shirts.
You're responsible for arranging the students in two rows before taking the photo.
Each row should contain the same number of the students and should adhere to the following guidelines:
 - All students wearing red shirts must be in the same row.
 - All students wearing blue shirts must be in the same row.
 - Each student in the back row must be strictly taller than the student directly in front of them in the front row.
You're given two input arrays: one containing the heights of all the
students with red shirts and another one containing the heights of all the students with blue shirts.
These arrays will always have the same length, and each height will be a positive integer.
Write a function that returns whether or not a class photo that follows the stated guidelines can be taken.

Note: you can assume that each class has at least 2 students.

Sample Input
redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]
Sample Output
true // Place all students with blue shirts in the back row.

Solution 1
Time Complexity: O(nlog(n)), space complexity: O(n)
Strategy:
Sort both arrays. Compare the first two elements in both arrays to see which array will be the back row.
Loop through the length of the array and check if the back row student is greater or equal to the front row student,
if it isn't then return False.
Return True if the loop completes without finding a failure case.
"""
# Solution 1
def class_photos_1(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if redShirtHeights[0] > blueShirtHeights[0]:
        top_row = redShirtHeights
        bottom_row = blueShirtHeights
    else:
        top_row = blueShirtHeights
        bottom_row = redShirtHeights

    del blueShirtHeights
    del redShirtHeights

    for i in range(len(top_row)):
        if top_row[i] <= bottom_row[i]:
            return False

    return True

