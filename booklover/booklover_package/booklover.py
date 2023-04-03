import pandas as pd
import numpy as np
import sys
# -*- coding: utf-8 -*-

class BookLover:
    '''A class to build a directory of books read by book lovers.'''
    
    #INITIALIZER
    def __init__(self, name, email, fav_genre, num_books=0,book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
              
    # METHOD 1
    def add_book(self, book_name, book_rating):
        '''This function takes a book name as a string and rating as an integer from 0 to 5'''
        if book_name in self.book_list:
                print(f'{book_name} already exists in your list of read books!')
        else:
            new_book = pd.DataFrame({
                'book_name':[book_name],
                'book_rating':[book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            print(f'Congrats on reading another book! {book_name} has been added to your list of read books!')
            self.num_books+=1
        print()
        
    # METHOD 2
    def has_read(self, book_name):
        if book_name in self.book_list:
            return True
        else:
            return False
            
    # METHOD 3
    def num_books_read(self):
        return self.num_books
    
    # METHOD 4
    def fav_books(self):
        fav_book_df = self.book_list[self.book_list['book_rating']>3]
        if fav_book_df.empty:
            return "Sorry, there are no books in your list with a rating above 3."
        else:
            return fav_book_df