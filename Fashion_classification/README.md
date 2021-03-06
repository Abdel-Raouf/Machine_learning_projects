# Clothes Classification (Deep Learning):
**Description:**

*Model Training:*
 - Train a Deep Neural Network Using a pre-trained model(Xception), which provide us with the costy convolutional neural network, While, trained the Dense Layer only(Transfer Learning). Also Adjusting the learning rate, adding more layers to increase accuracy, used Regularization and Dropout Technique to handle overfitting which increases significantly as we add more Dense layers, generated more data using Data-Augmentation(shear, rotation, zooming) to improve model accuracy, used an optimizer, which adjusts the weights of a network to make it better at doing its task and saving the model, cehckpointing whenever it improves(Reaches 90% Accuracy) to Classify Fashion Based on 10 categories:
 
![App look](https://github.com/Abdel-Raouf/Machine_learning_projects/blob/main/Fashion_classification/images/Screenshot%20from%202021-03-06%2006-32-36.png)

*MLops:*
1. Packeage model to a Docker Container.

2. Pushing Conatiner to AWS Elastic Container Registery (AWS ECR).

3. Deploy to AWS Lambda Successfully.

![App look](https://github.com/Abdel-Raouf/Machine_learning_projects/blob/main/Fashion_classification/images/Screenshot%20from%202021-03-06%2003-08-23.png)

4. Created the API Gateway, To be able to Expose the Model as a Web-Service and Communticating using Post-Method (Restful-API).

![App_look](https://github.com/Abdel-Raouf/Machine_learning_projects/blob/main/Fashion_classification/images/Screenshot%20from%202021-03-06%2003-27-20.png)

5. Testing the Endpoint.

![App look](https://github.com/Abdel-Raouf/Machine_learning_projects/blob/main/Fashion_classification/images/Screenshot%20from%202021-03-06%2003-29-06.png)

6. Testing the Web-Service (getting our Prediction for different images of clothes).

![App look](https://github.com/Abdel-Raouf/Machine_learning_projects/blob/main/Fashion_classification/images/Screenshot%20from%202021-03-06%2004-35-04.png)

**Development Stack:**
- Tensorflow (Low level API for Machine Learning).
- Tensorflow-lite (For inference only).
- Keras (High level API on top of tensorflow).
- Xception (As a pre-trained model from ImageNet).

**Deployment Stack:**
- Docker (making the service self-contained).
- AWS Elastic Container Registry (ECR) (Hosting Docker container on Cloud).
- AWS Lambda (an event-driven, serverless computing platform provided by AWS).
- AWS API Gateway (To access a Web-Service and send requests over HTTP)
