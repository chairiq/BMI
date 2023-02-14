

data = '''Nikos,Papadopoulos,30,Teacher-Eleni,Elenidou,25,Danser-Maria,Marinou,45,Teacher-Dimitris,Dimitriou,55,Student-Eleni,Marinou,25,Doctor-George,Georgiou,45,Doctor'''
print("\n1) Print the content of the dictionary. Example (key,[name, surname, age, occupation]) ")
def print_data(data):
    for x in data:
        print(X)


print("\n2) Convert the <data> string to a dictionary where the key is an auto increment number and tha value a list contening the personal info")
person = data.split(",")
personel_data = ()
for x,y in (person):
    personel_data[x] = y.split(" ") 


print("\n3) Print the content of dictionary.")



import pickle
print("\n4) Save the dictionary into a binary file")
f = open('/Users/chairiq/personel_data','rb')
pickle.dump(personeldata, f)
f.close()


print("\n5) Load the data from the binary file and print it.")
f2 = open("/Users/chairiq/personel_data.txt", 'w')
pd = pickle.load(f)
print_data(pd)


print("\n6) Update the third element of the <t> tuple.")
t = ('a', 'b', 'c', 'd', 'e')
print(t)
val = input("Give a chracter: ")
t[6] = val
print(t)


import matplotlib.pyplot as plt
print("\n7) Print the following data as scatter. Check the example.")
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.plot(x, y)
plt.show()


print("\n8) Store the book in the BookStore.") 
class BookStore:
    def __init__(self):
        self.my_books = []

    def addBook(self, *args):
        book = Book(*args)
        # append the books one by one to the my_books list
        print(str(book)+". (Επιτυχής προσθήκη !)")

    def __repr__(self): 
        my_str = "Αριθμός βιβλίων: {}. \n".format(len(self.my_books))
        for x in self.my_books:
            my_str += str(x)+"\n" 
        return my_str

class Book:
    def __init__(self, title, author, isbn):
        self.title =  title
        self.author = author
        self.isbn = isbn
    
    def __repr__(self):
        return f" " 

bs = BookStore()
print("\n Καταχώρηση Βιβλίων\n =========================================")
bs.addBook("Python Crash Course", "Eric Matthews", "1593279280")
bs.addBook("Learning Python ", "Mark Lutz", "1449355730")
bs.addBook("Head First Python", "Paul Barry", "7519813630")
bs.addBook("Introduction to Machine Learning with Python", "Andreas C. Mulle", "1449369413")
bs.addBook("Python for Data Analysis","Wes McKinney", "1098104032", )
bs.addBook("Deep Learning with Python", "Francois Chollet", "1617284433")

print("\n 9) Show the content of the BookStore without using the print() function, also show the number if the available books.")
print(bs)# Dont change this code. Work inside the class.



print("\n 10) Άσκηση.")
'''
Να μετρήσετε το πλήθος εμφάνισης χαρακτήρων στο παρακάτω απόσπασμα από τον Ύμνο στην ελευθερία.​
'''
ymnos = '''και σαν πρώτα ανδρειωμένη, χαίρε, ω χαίρε, Ἐλευθεριά!'''
freq = {}

print(freq)