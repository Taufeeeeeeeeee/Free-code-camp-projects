# Demographic Data Analyzer

This is the boilerplate for the Demographic Data Analyzer project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer


In this challenge you must analyze demographic data using Pandas. You are given a dataset of demographic data that was extracted from the 1994 Census database.

You must use Pandas to answer the following questions:

How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
What is the average age of men?
What is the percentage of people who have a Bachelor's degree?
What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
What percentage of people without advanced education make more than 50K?
What is the minimum number of hours a person works per week?
What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
What country has the highest percentage of people that earn >50K and what is that percentage?
Identify the most popular occupation for those who earn >50K in India.

Use the starter code in the file demographic_data_analyzer. Update the code so all variables set to "None" are set to the appropriate calculation or code. Round all decimals to the nearest tenth.

Unit tests are written for you under test_module.py.

Development
For development, you can use main.py to test your functions. Click the "run" button and main.py will run.

Testing
We imported the tests from test_module.py to main.py for your convenience. The tests will run automatically whenever you hit the "run" button.

Output:

 race
White                 27816
Black                  3124
Asian-Pac-Islander     1039
Amer-Indian-Eskimo      311
Other                   271
Name: count, dtype: int64
Average age of men: 39.4
Percentage with Bachelors degrees: 16.4%
Percentage with higher education that earn >50K: 46.5%
Percentage without higher education that earn >50K: 17.4%
Min work time: 1 hours/week
Percentage of rich among those who work fewest hours: 10.0%
Country with highest percentage of rich: Iran
Highest percentage of rich people in country: 41.9%
Top occupations in India: Prof-specialty
..........
----------------------------------------------------------------------
Ran 10 tests in 0.301s

OK