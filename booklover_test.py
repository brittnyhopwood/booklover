import unittest
from booklover import BookLover
import sys

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self):
        #Add a book and test if it is in `book_list`.
        test1=BookLover('Regina','Regina@gmail.com','Sci-Fi')
        test1.add_book('Charlie', 5)
        self.assertTrue(test1.add_book, ('Charlie', 5))
                  
    def test_2_add_book(self):
        #Add the same book twice. Test if it's in `book_list` only once.
        test2=BookLover('Samantha','Samantha@gmail.com','Sci-Fi')
        test2.add_book(("Dog Man",5), ("Dog Man",5))
        self.assertEqual(len(test2.book_list),1)
    def test_3_has_read(self):
        #Pass a book in the list and test the answer is `True`.
        test3=BookLover('Jacob','jacob@gmail.com','Autobiographies')
        test3.add_book("Shiloh",3)
        expected = True
        self.assertTrue(test3.has_read, expected)
    def test_4_has_read(self):
        #pass a book not in the list and use assert False to test the answer is True.
        test4=BookLover("Pamela",'Pamela@gmail.com','Fiction')
        test4.add_book("Matilda",5)
        self.assertFalse(test4.has_read("BFG"))
    def test_5_num_books_read(self):
        #add some books to the list, and test num_books matches.
        test5=BookLover('Roger','Roger@gmail.com','English Literature')
        test5.add_book('Rescue',1)
        test5.add_book('Plan',1)
        test5.add_book('Friends',3)
        self.assertEqual(test5.num_books_read(),3)
    def test_6_fav_books(self):
        test6=BookLover('Arnold',"Arnold@gmail.com",'Recipe Books')
        test6.add_book("James and The Giant Peach",5)
        test6.add_book("Rise Sister Rise",2)
        test6.add_book("How to Win The Bachelor",3)
        test6.add_book("The Bible",5)
        fav_books=test6.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))   
        
# Run unittest as the main module
if __name__ == '__main__':
    
    unittest.main(verbosity=3)