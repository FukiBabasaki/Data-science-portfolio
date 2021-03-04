# Data science portfolio by Fuki Babasaki
Hi!! I am a 3rd software engineering student, learning data science practices. My interests include statistics and I hope to improve my data analysis skills and explore ML algoriithms through building this portfolio! Mainly, Python with Scikit-Learn is used. I'd like to learn how to use Keras, TensorFlow, AWS and REST API in the future.

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
[GitHub](https://github.com/Fuki-UoA/Data-science-portfolio/blob/main/Notebooks/Supervised/House-price-prediction/House%20price%20prediction.ipynb) \
House prices: Advanced Regression Techniques is a knowledge competition on Kaggle. 
- Created a model that estimates the prices based on the information of houses. 
- Conducted data cleaning as there were some missing data, and categorical values. 
- Selected perfomance measure is Root Mean Square Error (RMSE) <img src="https://render.githubusercontent.com/render/math?math=RMSE(X,h) = \sqrt{\frac{1}{m} \sum^m_{i=1} \left( h(x^{(i)}) - y^{(i)} \right)^2}">
- Linear Regression, Adaboost and Random Forest regression were considered for a model. Cross-validation was used for evaluation.
- Final model I chose is Random Forest regressor, and GridSearchCV was used for best hyperparameters.
- The description and data are available [here](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) on Kaggle.
![](https://github.com/Fuki-UoA/Data-science-portfolio/blob/main/Notebooks/Supervised/House-price-prediction/images/OverallQualvsYearBuilt.png)
## Classification problems


