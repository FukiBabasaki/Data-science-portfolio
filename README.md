# Data science portfolio by Fuki Babasaki
Hi! I am a 3rd year software engineering student, learning data science practices. My interests include statistics and I hope to improve my data analysis skills and explore more ML algorithms through building this portfolio! Mainly using pandas, matplotlib and seaborn to visualise data and scikit-learn to preprocess data, build, evaluate and hyper-tune models.

## Dependencies
One main source of dataset is kaggle, and kaggle API is used for data extraction. Use the package manager pip to install kaggle. \
For python 3.4 or later

```bash
python -m pip install kaggle
```
For earlier versions
```bash
pip install kaggle
```
Kaggle API token is also needed. See https://www.kaggle.com/docs/api
## Regression problems
### House prices: Advanced Regression Techniques
[GitHub](https://github.com/Fuki-UoA/Data-science-portfolio/blob/main/Notebooks/Supervised/House-price-prediction/House%20price%20prediction.ipynb) 
House prices: Advanced Regression Techniques is a knowledge competition on Kaggle. 

- Created a model that estimates the prices based on the information of houses. 
- Conducted data cleaning as there were some missing data, and categorical values. 
- Selected performance measure is Root Mean Square Error (RMSE) <img src="https://render.githubusercontent.com/render/math?math=RMSE(X,h) = \sqrt{\frac{1}{m} \sum^m_{i=1} \left( h(x^{(i)}) - y^{(i)} \right)^2}">
- Linear Regression, Adaboost and Random Forest regression were considered for a model. Cross-validation was used for evaluation.
- Final model I chose is Random Forest regressor, and GridSearchCV was used for best hyper-parameters.
- The description and data are available [here](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) on Kaggle.
![](Notebooks/Supervised/House-price-prediction/images/OverallQualvsYearBuilt.png)

### Prediction: average number of earthquakes for their magnitudes.

[GitHub](https://github.com/Fuki-UoA/Data-science-portfolio/blob/main/Notebooks/Supervised/earthquake-prediction/earthquake-pred.ipynb) 

- Dataset provided by one of the courses I did at the University of Auckland.
- I tried to build a descriptive model rather than predictive. statsmodels library was used to implement the model.
- Poisson regression model was chosen as the response variable (number of earthquakes) is a count.

![](Notebooks/Supervised/earthquake-prediction/images/download.png) 

## Classification problems

### Titanic - Machine Learning from Disaster 

[GitHub](https://github.com/Fuki-UoA/Data-science-portfolio/blob/main/Notebooks/Supervised/Titanic-classification/titanic-classification.ipynb) 

It is a typical *binary classification problem* where the main goal is to build a binary classifier.

- Built a model predicting whether or not a person can survive the Sinking of the Titanic.
- Exploratory analysis includes conditional density plot.
- My data cleansing pipeline include a custom imputer and Standard Scalier for numeric values, and Simple Imputer and One-hot Encoder for categorical values.
- Models shortlisted: *Stochastic Gradient Descent (SGD)*, *Random Forest Classifier*, *K-Nearest Neighbour*, and *Support Vector Machine (SVM)*
- SVM performed the best and therefore, was hyper-tuned.
- The description and data are available [here](https://www.kaggle.com/c/titanic) on Kaggle.

![](Notebooks/Supervised/Titanic-classification/images/cdp.png)

## Clustering problems
