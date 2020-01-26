# Real Estate Head Office
## Description

You have been tasked with building a database system for a large franchised real
estate company. This means that the company has many offices located all over
the country. Each office is responsible for selling houses in a particular area.
However an estate agent can be associated with one or more offices.

### Inserting data
1. Whenever a house is listed then the following things need to happen:
 -  All the relevant details of that house need to be captured, ie. at least: seller details, # of bedrooms, # of bathrooms, listing price, zip code, date of listing, the listing estate agent, and the appropriate office.
2. Whenever a house is sold then the following things need to happen:
 - The estate agent commission needs to be calculated. This happens on a sliding scale:
   - For houses sold below $100,000 the commission is 10%
   - For houses between $100,000 and $200,000 the commission is 7.5%
   - For houses between $200,000 and $500,000 the commission is 6%
   - For houses between $500,000 and $1,000,000 the commission is 5%
   - For houses above $1,000,000 the commission is 4%
 - All appropriate details related to the sale must be captured, ie. at least: buyer details, sale price, date of sale, the selling estate agent.
 - The original listing must be marked as sold.

### Querying data
Every month the following reports need to be run:
 - Find the top 5 offices with the most sales for that month.
 - Find the top 5 estate agents who have sold the most (include their contact details and their sales details so that it is easy contact them and congratulate them).
 - Calculate the commission that each estate agent must receive and store the results in a separate table. For all houses that were sold that month, calculate the average number of days that the house was on the market.
 - For all houses that were sold that month, calculate the average selling price

### Testing:
To test your solution you will need to create fictitious data and ensure that
the correct results are calculated from your SQL code.

### Submission:
For this assignment you may write your SQL code directly in the SQLite dialect,
or else you may use SQLAlchemy and write python code. In either case, your
primary submission must be a pdf listing of a `README.md` file followed by the
rest of your code, but you must also submit a zip file containing all the code.
When this code is run then it must clearly print to screen the results of any
SQL queries that are run. As part of your assignment, your must highlight places
where you have appropriately used data normalization, indices, and transactions.
Please draw attention to any areas of your assignment where you have exceeded
the requirements of this assignment.

#### Execution (Python):
In a `README.md` file you must include a series of commands to execute all the
relevant parts of your code:

```python3
python3.6 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 create.py
python3 insert_data.py
python3 query_data.py
```
#### Execution (SQLite):
In a `README.md` file you must include a series of commands to read the various
files your have submitted. For example:

```sqlite3
.read create.sql
.read insert_data.sql
.read query_data.sql
```

## Alternative Assignment
If your contribution to the final project has involved a significant aspect of
database programming then you can submit a pdf containing links to pull
requests where you have used similar techniques and technology as is asked for
in the above assignment. As always your code should include a significant
amount of unit tests and be well documented.

## Focused Outcomes Added

- **#cs162-communication**: Ensure that all code, documentation and commit messages are clearly written with explanations where appropriate.
- **#cs162-sql**: Write fast queries for well-designed SQL tables.
