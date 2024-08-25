"""Python Section"""
"Q1"
"What is decorator , write a decorator?"

"that allows a user to add new functionality to an existing object without modifying its structure."
"""DECORE"""
"""def is_prm(is_prime):
    def even_odd(num):
        if num % 2 == 0:
            return (num, "is even")
        else:
            return is_prime(num)
    return even_odd
@is_prm
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return (num, "not a prime number")
        return (num, "its prime number")
    else:
        return (num, "not a prime number")
print(is_prime(3))
print(is_prime(10))"""


"""Q3"""
"""WAF, S = ‘Hello everyone’, count the occurrence of each char, return those
repetitive character , without using any inbuilt function."""
"""
S = "Hello everyone"
char=""
for i in S:
    char=i
    count = 0
    for j in S:
        if j==char:
            count=count+1
    if count > 1:
        print(char,"=",count)
"""

"Q4"
"""WAF , Reverse a string words.
> Input = ‘hello world’ > output:- ‘world hello’, without using inbuilt function"""

"""
Input = "hello world"
output=""
for i in Input:
    output=i+output
print(output)
"""

"Q5"
"""WAF, input= ‘aaabbaacd’ output= ‘3a2b2a1c1d’"""
"""def compress_string(s):
    if not s:
        return ""
    result=[]
    count=1
    for i in range(1,len(s)):
        if s[i]==s[i - 1]:
            count+=1
        else:
            result.append(f"{count}{s[i - 1]}")
            count = 1
    result.append(f"{count}{s[-1]}")
    return ''.join(result)
input = 'aaabbaacd'
output_string = compress_string(input)
print("Output","=",output_string)"""



"Q6"
"Sort a list integer element without using inbuilt function?"
"""num = [64, 34, 25, 12, 22, 11, 90]
for i in range(len(num)):
    for j in range(0, len(num) - i - 1):
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]
print(f"Sorted list: {num}")"""


"Q7"
"""Li = [1,2,3,4], Li2 = [10,20,30]
Result = {1:10,2:20,3:30}
Take a two list a parameter, return dictionary, look like above result."""
"""def dict_lists(list1, list2):
    result = {}
    length = len(list1) if len(list1)<len(list2) else len(list2)
    for i in range(length):
        result[list1[i]] = list2[i]
    return result
Li = [1, 2, 3, 4]
Li2 = [10, 20, 30]
result = dict_lists(Li, Li2)
print(result)"""

"Q8"
"""Handel a csv file, write first_name , email, phn_no, insert 5 data in this csv, then read
the csv and print in console bar"""

"""import  csv
data_col=["first_name" , "email", "phn_no"]
data_cols=[["Sunil","abc@mail.com",2287887677],["aryan","abc@mail.com",2287887677],["ashok","abc@mail.com",2287887677],["giyan","abc@mail.com",2287887677],["Sunil","abc@mail.com",2287887677]]
with open("output.csv",mode="w") as file:
    csv_writer=csv.writer(file)
    csv_writer.writerow(data_col)
    csv_writer.writerows(data_cols)
with open("output.csv",mode="r") as file:
    csv_reader=csv.reader(file)
    for i in csv_reader:
        print(i)
"""


"Q9"
"""What is exception handling , how handel the exception in python , explain with each
block"""

"""when our program have a error then exception handling without stopping continue the execution is call exeception handling.
there are three block
    1.try
    2.except
    3.fainally
try: block lets you test a block of code for errors.
except: block lets you handle the error.

"""


"Q11"
"""Difference between List vs tuple vs set vs dictionary?"""

"""Lists

It is enclosed with Square Bracket
Elements are stored in a specific order.
Elements can be added, removed, or modified after creation.
Elements can be accessed using their index.
Example: my_list = [1, 2, 3, "treenetra"]

Tuples

It Enclosed with 
Similar to lists, but elements are stored in a specific order.
Elements cannot be modified after creation.
Elements can be accessed using their index.
It is Immutable.
Example: my_tuple = (1, 2, 3, "treenetra")


Sets

Elements are stored without a specific order.
Elements can be added or removed, but not modified.
Sets cannot contain duplicate elements.
removing duplicates, and mathematical operations like union, intersection.
Example: my_set = {7, 8, 9, "treenetra"}


Dictionaries

It is Collection of Key and value pair.
It is enclosed with Curli Bracket.
It is Mutable in nature.
Key must be unic.
Example: my_dict = {"name": "Aryan", "age": 29,}"""


"Q12"
"""What is Garbage Collection?"""

"""It automatically frees up memory
space that has been allocated to objects no longer needed by the program.
It's a form of automatic memory management, relieving programmers from the manual task of deallocating memory."""

"Q15"
"""Explain break, continue, pass with code?"""

"break"
"""for i in range(10):
    if i == 5:
        break
    print(i)"""

"continue"
"""for i in range(10):
    if i % 2 == 0:
        continue
    print(i)"""

"pass"
"""for i in range(10):
    if i % 2 == 0:
        continue
    print(i)"""











"""SQL"""

"""SQL1. Explain about the DML, DDL, TCL, DQL commands?"""
"""
DML (Data Manipulation Language): Used for manage data in  objects
    INSERT
    UPDATE
    DELETE
    MERGE.
DDL (Data Definition Language): Used for defining and managing all database objects.
    CREATE
    ALTER
    DROP
    TRUNCATE
    COMMENT
    RENAME
TCL (Transaction Control Language): Manages changes made by DML statements.
    COMMIT
    ROLLBACK
    SAVEPOINT
    SET
    TRANSACTION.
DQL (Data Query Language): Used to query data from the database.
    SELECT."""
"""Q2"""
""" 2. What is a join? Explain all joins."""

"""Join

A SQL operation that combines rows from two or more tables based on a related column between them.

Inner Join:
Returns records with matching values in both tables.
ON table1.common_column = table2.common_column;

Left Join (Left Outer Join): 
Returns all records from the left table and matched records from the right table; returns NULL for unmatched rows in the right table.

Right Join (Right Outer Join): 
Returns all records from the right table and matched records from the left table; returns NULL for unmatched rows in the left table.

Full Join (Full Outer Join): 
Returns records when there is a match in either left or right table records; returns NULL for unmatched rows in either table.

Cross Join: Returns the Cartesian product of the two tables.
Self Join: A table is joined with itself."""

"""Q3"""
"""Difference between Joins vs Subquery?"""
"""Joins:
    combine data from multiple tables into a single result set by matching columns between them
Subqueries:
    are nested queries executed separately before the outer query uses the result. Subqueries can be used for complex filtering and calculation."""

"""Q4"""
"""Find 3rd Highest Salary Of employee table ?"""
"""select * from emp where salary=>(select max(sal) from salary where salary =>(select max(sal) from salary))
SELECT DISTINCT salary 
FROM employee 
ORDER BY salary DESC 
LIMIT 1 OFFSET 2;

SELECT seller_id, SUM(amount) AS total_sales
FROM sales
WHERE MONTH(sale_date) = MONTH(CURRENT_DATE)
AND YEAR(sale_date) = YEAR(CURRENT_DATE)
GROUP BY seller_id
ORDER BY total_sales DESC;"""

"""Q6"""
"""Difference between Rank vs Dense_rank?"""
"""Rank: Provides ranks with gaps. If two rows are tied, the next rank will have a gap.
Dense_Rank: Provides ranks without gaps. If two rows are tied, the next rank will continue without a gap."""





"Linux"
"""Q2"""
"""2. How do you find the process IF(PID) of a running process."""
"""for finding the PID we use ps command for checking the the pid number after tha we can use
ps -ef | grep process_name."""


"""Q3"""
"""3. Difference between chown vs chmod?"""
"""chown: Changes the ownership of files or directories.
syntax:chown user:group filename
chmod: Changes the file('s permissions (read, write, execute).'
Syntax: chmod w/r/x filename
chown: in this command used for changing the owner ship.
chmod:in this command used for giving the permission who can access the file and modify."""

"""Q6"""
"""How to list directories in Unix?"""
"""ls  -ltr
ls -la
ls -al"""





"""Selenium"""

"""Q1"""
"""what is webdriver?"""
"""a webdriver is a tool that manage automating web browser
it allow to control and manage the web broswer."""

"""Q2"""
"""How to handel selective dropdown, write a snippet for it?"""
"""To handle a selective dropdown , you can use the Select class locater.
        driver.find_elements
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get("full_url_include_https")
driver.find_element(by.id,"dropdown_id")
select = Select(dropdown_element)
select.select_by_visible_text("Option 1")"""


"""Q6"""
"""Explain the wait mechanism, write syntax and snippet for it"""

"""there are two types of wait mechanism

1.   implicit wait
    driver.implicitly_wait(10)

2.   explacit wait
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    driver = webdriver.Chrome()
    driver.get(web_page_link)
    wait = WebDriverWait(driver, 10)  # seconds
    element = wait.until(EC.(element_to_visible(By.ID, 'some_id')))"""

"""Q8"""
"""how many locaters in seleneium?"""
"""there are 8 types of locators
1.id
2.name
3.tagename
4.xpath
    absolute xpath
    relative xpath
5.css selector
6.link text
7.partial link text"""


"Q10"
"""10. Write xpath"""
"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.nseindia.com/")
Action_Chain=ActionChains(driver)
elemen_maket_data=driver.find_element(By.XPATH,"//li/a[text()='Market Data']")
Action_Chain.move_to_element(elemen_maket_data).perform()
driver.find_element(By.XPATH,"//li/a[text()='Pre-Open Market']").click()"""
