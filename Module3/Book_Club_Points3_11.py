# Book_Club_Points3_11
# Booksellers has a book club that awards points
# to its customers based on the number of books purchased each month.
# The points are awarded as follows:
# If a customer purchases 0 books, he or she earns 0 points.
# If a customer purchases 2 books, he or she earns 5 points.
# If a customer purchases 4 books, he or she earns 15 points.
# If a customer purchases 6 books, he or she earns 30 points.
# If a customer purchases 8 or more books, he or she earns 60 points.
# Write a program that asks the user to enter the number of books
# that he or she has purchased this month,
# then displays the number of points awarded.

def main():
    books_purchased=int(input('Enter the number of book that you purchased this month: '))
    if books_purchased<=1:
        points=0
        print('Number of points awarded:',points)
    elif books_purchased>=2 and books_purchased<=3:
        points=5
        print('Number of points awarded:',points)
    elif books_purchased>=4 and books_purchased<=5:
        points=15
        print('Number of points awarded:',points)
    elif books_purchased>=6 and books_purchased<=7:
        points=30
        print('Number of points awarded:',points)
    else:
        points=60
        print('Number of points awarded:',points)    
main()
