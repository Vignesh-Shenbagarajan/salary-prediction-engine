## Salary Prediction Engine: Project Overview

* Created a tool that estimates data science salaries (MAE ~ $ 11K) to help data science job applicants in USA have an understanding of the data science payscale across the country.
* Scraped over 1000 job descriptions from glassdoor using python and selenium
* Extracted new factors from job description to quantify the value companies put on required data science tools like python, excel, aws, and spark. 
* Built regression models to predict the average salary for a data science job based on job description, title, seniority, job state, company age, company size, Industry, etc.
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facing API using flask

## Code and Resources Used

**Python Version**: 3.7<br/>
**Packages**: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle<br/>
**For Web Framework Requirements**: pip install -r requirements.txt<br/>
**Scraper Github**: https://github.com/arapfaik/scraping-glassdoor-selenium<br/>
**Scraper Article**: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905<br/>
**Flask Productionization**: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2<br/>

Web Scraping
Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:

* Job title<br/>
* Salary Estimate<br/>
* Job Description<br/>
* Rating<br/>
* Company<br/>
* Location<br/>
* Company Headquarters<br/>
* Company Size<br/>
* Company Founded Date<br/>
* Type of Ownership<br/>
* Industry<br/>
* Sector<br/>
* Revenue<br/>
* Competitors<br/>

## Data Cleaning<br/>

After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:<br/>

* Parsed numeric data out of salary<br/>
* Made columns for employer provided salary and hourly wages<br/>
* Removed rows without salary<br/>
* Parsed rating out of company text<br/>
* Made a new column for company state<br/>
* Added a column for if the job was at the company’s headquarters<br/>
* Transformed founded date into age of company<br/>
* Made columns for if different skills were listed in the job description:<br/>
        * Python<br/>
        * R<br/>
        * Excel<br/>
        * AWS<br/>
        * Spark<br/>
* Column for simplified job title and Seniority<br/>
* Column for description length<br/>

## Exploratory Data Analysis

I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.<br/>

![alt text](https://github.com/Vignesh-Shenbagarajan/salary-prediction-engine/blob/master/salary_by_job_title.PNG) ![alt text](https://github.com/Vignesh-Shenbagarajan/salary-prediction-engine/blob/master/correlation_visual.png)

![alt text](https://github.com/Vignesh-Shenbagarajan/salary-prediction-engine/blob/master/positions_by_state.png) ![alt text](https://github.com/Vignesh-Shenbagarajan/salary-prediction-engine/blob/master/Industry.png)
## Model Building
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

I tried three different models:

* **Multiple Linear Regression** – Baseline for the model<br/>
* **Lasso Regression** – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.<br/>
* **Random Forest** – Again, with the sparsity associated with the data, I thought that this would be a good fit.<br/>

### Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets.

* **Linear Regression**: MAE = 18.86
* **Lasso Regression**: MAE = 19.67
* **Random Forest** : MAE = 10.87

## Productionization

In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.
