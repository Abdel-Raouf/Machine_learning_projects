# Churn Prediction for a Telecom Company (Binary Classification): 
  1. using Logistic Regression and Scikit-Learn. While, applying EDA, Feature importance analysis(Risk Ratio and mutual information) ,  one-hot encoding(transforming all categorical variables to numeric features).
  2. Evaluating model accuracy, first, by using inferential statistics(frequentism statistics(p-value)) to make our confusion table, which we will use for more evaluating using precision and recall, ROC and AUC.
  3. Parameter Tuning: by selecting the best parameter "C" using cross-validation.
  4. Saving the state of the model by Pickling it, to be able to use it as a service.
  5. Deployment: Pipenv(to lock dependencies), Flask(to expose the model as a web service), Docker(Making a service self-contained), Deploying model to the cloud using AWS Elastic Beanstalk (EB CLI).

**Deployment To AWS Using EB CLI:**
![App look](https://github.com/Abdel-Raouf/Machine_learning_projects/blob/main/Churn_prediction_project/images/Screenshot%20from%202021-02-27%2003-42-54.png)

**Testing Restful Web-Service (by passing a customer to the model)**:
![App look](https://github.com/Abdel-Raouf/Machine_learning_projects/blob/main/Churn_prediction_project/images/Screenshot%20from%202021-02-27%2003-52-38.png)

**Note: Model code is commented and Explained, hope to enjoy.**
