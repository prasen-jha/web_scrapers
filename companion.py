import requests
from bs4 import BeautifulSoup as bs
import psycopg2 as pg
import pandas as pd


def check_n_response(url, parser='html.parser'):
    # TODO Add functionality for generating response
    """ this function uses three functions, 2 from requests and 1 from beautiful soup to create
    a beautiful object
        1. page = requests.get(url) ---> to fetch the response
        2. page.status_code ---> to check the status code for response
        3. page.text --->The text attribute returns the content as a normal UTF-8 encoded Python string
        4. bs(page.text,parser)
        :param url:
        :param parser: """
    page = requests.get(url)

    if page.status_code in range(200,300):
        print('Request was successful')
        return bs(page.text, parser)
    else:
        print(f'Request was denied the error code is {page.status_code}')


def generate_html(soup_obj):
    # TODO Add functionality gor generating html
    """This function will use context processor for file handling to create a html file from the response
    object it will use following functions
        1. with statement ---> python
        2. file handling ---> python
        3. soup.prettify() ---> beautiful soup
        :param soup_obj: """
    with open('temp.html', 'w+', encoding='utf-8') as fp:
        fp.write(soup_obj.prettify())


def extraction(soup_object, tag, _class, attr, index=None, single=False):
    # TODO generate iterable of different lengths with clean text
    """ This function creates a clean list of data i.e without any tag inside quotes
    it uses the following functions
        1.find_all() ---> beautiful soup
        2.get_text ---> beautiful soup
        3.list_comprehension  ---> python
        :param soup_object:
        :param tag:
        :param _class:
        :param attr:
        :param index:
        :param single: """
    data = [i.get_text() for i in soup_object.find_all(tag,{_class:attr})]
    if single:
        return data[0]
    elif index:
        return data[:index]
    return data


def cleaning(format, iterable):
    # TODO apply list(map())
    """This function uses inbuilt functionality of python to generate the list of data
        1. Explicit conversion
        2. Map function
        :param format:
        :param iterable:
    """
    return list(map(format, iterable))


def database_connect(name, user, password):
    # TODO return an open connection
    """This function uses psycopg2 for making connections with database and return an open connection
        1. try/except ---> python
        2. psycopg2.connect() ---> method of psycopg2
        3. psycopg2.DatabaseError ---> to handle the database related error
        :param name:
        :param user:
        :param password:
    """
    try :
        db_connection = pg.connect(dbname=name,user=user,password=password,host='127.0.0.1',port='5432')
        print('That connection was successful')
        return db_connection
    except pg.DatabaseError as e:
        print(f'error happened {e}')


def database_operation(connection, statement, data=None):
    # TODO execute statement and commit to database and close the connection
    """ here we are going to use the open connection returned from above and following functions
        1. creating cursor object
        2. execute function on cursor
        3. using commit to save the transaction to the database
        4.closing the connection
        :param connection:
        :param statement:
        :param data:
    """
    try :
        cursor = connection.cursor()
        if data:
            for d in data:
                cursor.execute(statement,d)
        else:
            cursor.execute(statement)
        connection.commit()
        print('The transaction was successful')
    except pg.DatabaseError as e:
        print(f'error happened {e}')
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('Connection was closed successfully')



