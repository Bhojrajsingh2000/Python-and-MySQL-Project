import pymysql as sq
from datetime import datetime
import pandas as pd
conn=sq.connect(
    host='localhost',
    user='root',
    password='',
    database='library'
)
mycursor=conn.cursor()
def add_book():
    try:
        book_name = input("Book Name : ")
        author_name = input("Author Name : ")
        book_code = input("Book Code : ")
        total_book = int(input("Total Book : "))
        
        cust = (book_code, book_name, author_name, total_book)
        sql = '''
            INSERT INTO book (book_code, book_name, author_name, total_book)
            VALUES (%s, %s, %s, %s);
            '''
        mycursor.execute(sql, cust)
        conn.commit()
        print('''
              **************************
              Book added successfully
              **************************
              ''')
        input('Press enter to continue...')
    except ValueError:
        print('''
              ****************************
              Enter the correct value
              *******************************
              ''')
def delete_book():
    book_code = input('Enter The Book Code: ')
    sql = 'DELETE FROM book WHERE book_code = %s'
    try:
        mycursor.execute(sql, (book_code,))
        conn.commit()
        if mycursor.rowcount > 0:
            print('''
                  ***************************
                  Book deleted successfully
                  *****************************
                  ''')
        else:
            print('''
                  *****************************
                  No book found with that code.
                  *********************************
                  ''')
    except sq.Error as err:
        print(f"Error: {err}")
    finally:
        input('Press enter to continue...')
def view_book():
    try:
        sql = 'SELECT * FROM book'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        df = pd.DataFrame(result, columns=['Book Code', 'Book Name', 'Author Name', 'Total Book'])
        print(df)
    except sq.Error as err:
        print(f"Error: {err}")
    finally:
        input('Press enter to continue...')
def issue_book():
    try:
        student_name = input('Student Name: ')
        reg_no = input('Registration Number: ')
        book_code = input('Book Code: ')
        issue_date = datetime.now().strftime('%Y-%m-%d')
        
        check_sql = '''
            SELECT total_book FROM book WHERE book_code = %s
        '''
        mycursor.execute(check_sql, (book_code,))
        result = mycursor.fetchone()
        
        if result is None:
            print('''
                  ***********************************
                  Error: Book code does not exist.
                  ***********************************
                  ''')
            return
        
        total_book = result[0]
        
        if total_book <= 0:
            print('''
                  ********************************************
                  Error: No copies of the book are available.
                  ********************************************
                  ''')
            return
        
        cust = (student_name, reg_no, book_code, issue_date)
        
        issue_sql = '''
            INSERT INTO issue (student_name, reg_no, book_code, issue_date)
            VALUES (%s, %s, %s, %s)
        '''
        mycursor.execute(issue_sql, cust)
        conn.commit()
        
        update_sql = '''
            UPDATE book SET total_book = total_book - 1 WHERE book_code = %s
        '''
        mycursor.execute(update_sql, (book_code,))
        conn.commit()
        
        print('''
              *************************
              Book Issued Successfully
              *************************
              ''')
        
    except ValueError:
        print('****** Enter the correct value *******')
    except sq.Error as e:
        conn.rollback()
        print(f'An error occurred: {e}')
    finally:
        input('Press enter to continue...')
def return_book():
    try:
        student_name = input('Student Name: ')
        reg_no = input('Reg Number: ')
        book_code = input('Book Code: ')
        return_date = datetime.now().strftime('%Y-%m-%d')
        
        cust = (student_name, reg_no, book_code, return_date)
        return_sql = '''
            INSERT INTO return_book (student_name, reg_no, book_code, return_date)
            VALUES (%s, %s, %s, %s)
            '''
        mycursor.execute(return_sql, cust)
        conn.commit()
        
        update_sql = '''
            UPDATE book SET total_book = total_book + 1 WHERE book_code = %s
            '''
        mycursor.execute(update_sql, (book_code,))
        conn.commit()
        
        delete_issue_sql = '''
            DELETE FROM issue WHERE student_name = %s AND reg_no = %s AND book_code = %s
        '''
        mycursor.execute(delete_issue_sql, (student_name, reg_no, book_code))
        conn.commit()
        
        print('''
              ***************************
              Book Returned Successfully
              ***************************
              ''')
    except ValueError:
        print('********Enter the correct value*********')
    except sq.Error as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        input('Press enter to continue...')
def report():
    while True:
        print('''
                ========Report========
                
                1. Issue Book Report
                2. Return Book Report
                3. Go Back to Main Menu
                ''')
        try:
            ch = int(input('Enter your choice: '))
            
            if ch == 1:
                sql = 'SELECT * FROM issue'
                mycursor.execute(sql)
                result = mycursor.fetchall()
                if result:
                    df = pd.DataFrame(result, columns=['Student Name', 'Reg No', 'Book Code', 'Issue Date'])
                    print(df)
                else:
                    print("=======No records found in issue table.========")
            elif ch == 2:
                sql = 'SELECT * FROM return_book'
                mycursor.execute(sql)
                result = mycursor.fetchall()
                if result:
                    df = pd.DataFrame(result, columns=['Student Name', 'Reg No', 'Book Code', 'Return Date'])
                    print(df)
                else:
                    print("========No records found in return_book table.=========")
            elif ch == 3:
                break
            else:
                print("======Invalid choice. Please enter a number between 1 and 4.=======")
        except ValueError:
            print("==========Invalid input. Please enter a valid number.===========")
        except sq.Error as e:
            print(f"An error occurred: {e}")
        finally:
            input('Press enter to continue...')

def main():
    while True:
        print('''
            =============== Welcome to LMS =================
            1. Add Book to LMS
            2. Delete Book from LMS
            3. View Book from LMS
            4. Issue Book from LMS
            5. Return Book from LMS
            6. Report Book/Student from LMS
            7. Exit LMS
            ''')
        try:
            ch = int(input('Enter your choice: '))
            if ch == 1:
                add_book()
            elif ch == 2:
                delete_book()
            elif ch == 3:
                view_book()
            elif ch == 4:
                issue_book()
            elif ch == 5:
                return_book()
            elif ch == 6:
                report()
            elif ch == 7:
                break
            else:
                print('Enter the correct choice')
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 7.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
      
        
