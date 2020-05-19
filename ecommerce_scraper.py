from companion import *

CREATE_STATEMENT = '''CREATE TABLE mobile_data \
    (ID SERIAL NOT NULL,
    MODEL_NAME TEXT NOT NULL,\
    RATING FLOAT,\
    PRICE FLOAT);
'''
INSERT_STATEMENT = 'INSERT INTO mobile_data (MODEL_NAME,RATING,PRICE) VALUES (%s,%s,%s)'

URL = "https://www.flipkart.com/search?q=mobiles"

''' Checking response and generating html'''
response = check_n_response(URL)
# generate_html(response)

# '''Extracting Data & Cleaning Data'''
name_data = extraction(response, 'div', 'class', '_3wU53n')
price_data = extraction(response, 'div', 'class', '_1vC4OE _2rQ-NK')
ratings_data = extraction(response, 'div', 'class', 'hGSR34',24)

combined_data = tuple(zip(name_data,  ratings_data, price_data))

# for i, d in enumerate(combined_data):
#     print(i, ' --> ', d)

func = lambda x: float(x[1:].replace(',', ''))

''' Calling Cleaning Functions & checking'''
cleaned_mobile_prices = cleaning(func, price_data)
cleaned_mobile_rating = cleaning(float, ratings_data)


'''Data Preparation and database Functionality'''
#
# data = list(zip(name_data, cleaned_mobile_rating, cleaned_mobile_prices))
# conn = database_connect('test_db', 'postgres', '12345678')
# # database_operation(conn, CREATE_STATEMENT)
# database_operation(conn, INSERT_STATEMENT, data)


data = {'mobile_names': name_data,
        'mobile_rating': cleaned_mobile_rating,
        'mobile_price': cleaned_mobile_prices}

dataframe = pd.DataFrame(data)
dataframe.to_csv('Mobile_data.csv')
