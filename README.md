![10 Academy](https://static.wixstatic.com/media/081e5b_5553803fdeec4cbb817ed4e85e1899b2~mv2.png/v1/fill/w_246,h_106,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/10%20Academy%20FA-02%20-%20transparent%20background%20-%20cropped.png)

# Pharmaceutical Sales Prediction across multiple stores

**Business Need** <br>

You work at Rossmann Pharmaceuticals as a Machine Learning Engineer. The finance team wants to forecast sales in all their stores across several cities six weeks ahead of time. Managers in individual stores rely on their years of experience as well as their personal judgment to forecast sales. 

The data team identified factors such as promotions, competition, school and state holidays, seasonality, and locality as necessary for predicting the sales across the various stores.

Your job is to build and serve an end-to-end product that delivers this prediction to analysts in the finance team. 

***

**Folder Structure**

In the scripts folder you will find three python scripts: data_cleaner.py, plotter.py, util.py

The name of the files are self explanatory. You should use methods from data_cleaner.py when dealing with data cleaning and preprocessing.

Plotter.py is a python script consisting of various methods that will help you to make plots (graphs)

The util.py script contains helper methods that you will be using more often 
- read df from dvc or a local file

The notbook directory contains two notebooks namely data_exploration and data_preprocessing

The data directory contains the dvc files which are the blueprints of the original dataset

we have versioned our data according to the following tags

>- 'sample-v0' - the original sample_submission dataset
>- 'store-v0' - the original store dataset
>- 'store-v1' - the cleaned store dataset
>- 'test-v0' - the original test dataset
>- 'test-v1' - the cleaned test dataset
>- 'test-v2' - optimized cleaned test dataset
>- 'train-v0' - the original train dataset
>- 'train-v1' - the cleaned train dataset
>- 'train-v2' - optimized cleaned train dataset
___

**Data and Features**

The data for this challenge can be found here: [Rossmann Store Sales | Kaggle](https://www.kaggle.com/competitions/rossmann-store-sales/data)

**Data fields**
 
Most of the fields are self-explanatory. The following are descriptions for those that aren't.

Id - an Id that represents a (Store, Date) duple within the test set

Store - a unique Id for each store

Sales - the turnover for any given day (this is what you are predicting)

Customers - the number of customers on a given day

Open - an indicator for whether the store was open: 0 = closed, 1 = open

StateHoliday - indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None

SchoolHoliday - indicates if the (Store, Date) was affected by the closure of public schools
StoreType - differentiates between 4 different store models: a, b, c, d

Assortment - describes an assortment level: a = basic, b = extra, c = extended. Read more about assortment [here](https://en.wikipedia.org/wiki/Retail_assortment_strategies)

CompetitionDistance - distance in meters to the nearest competitor store

CompetitionOpenSince[Month/Year] - gives the approximate year and month of the time the nearest competitor was opened

Promo - indicates whether a store is running a promo on that day

Promo2 - Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating

Promo2Since[Year/Week] - describes the year and calendar week when the store started participating in Promo2

PromoInterval - describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store



