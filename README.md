# Cifar10RestAPIBackendService
 Creating Machine Learning or Deep Learning models is valuable, but their true impact is realized when they are made accessible to the real world. Deploying machine learning models using Flask Rest API on Azure cloud is one of the powerful approach to make machine learning models accessible as web services.
 This repo contains code of Deep learning Model based Rest API made using Flask deployed on Azure Cloud. The code implementation is for the assignment given by CDS Lab, IIsc where I was tasked to create a full stack machine learning project for the same. In this repo you would fine a jupyter notebook file where basic image classifcation code for Cifar-10 Dataset where I experimented the dataset using transfer learning on various model like VGG16, MobileNetV2 and a custom model consisting of pooling layers and a custom CNN.
| Model          | Accuracy |
|----------------|----------|
| MobileNetV2    | 58%      |
| Vgg16          | 68%      |
| Custom Model   | 97%      |


The weights for the custom model was saved in .h5 format which could be used in Flask RestAPI service. 

Demo Video - https://drive.google.com/file/d/1KvEs9nL_FqHusKTmLfkkh24rbRB1_DRr/view?usp=sharing

The app.py contains the flask server and is deployed to Azure Web App service (Hosted **URL **- https://deeplearningrestapi.azurewebsites.net/predict)

The flask server is deployed to Azure ML service where I have used its student explore program pack which consists of 100$ free Azure credits for the same. (Note- Please use the tutorial service before the azure credits gets used up). 

To know how you can deploy a Machine learning model using Flask Rest API service to Azure ML, you can refer to** my medium article** - https://medium.com/@deepuadak/unlocking-ml-potential-deploying-flask-rest-api-for-machine-learning-models-on-microsoft-azure-bc5235a81261

Frontend is hosted on vercel on the respective link where you can use the service. **Url:** - https://cifar10-frontend-service.vercel.app/

**The Frontservice github - ** https://github.com/mr-prometheus/Cifar10FrontendService

Go Ahead and make use of this repository to deploy your machine learning models using Flask to Azure Cloud. 

To clone this Git repository that contains Python files and a `requirements.txt` file, follow these steps:

1. Open your terminal or command prompt.

2. Navigate to the directory where you want to clone the repository. For example, if you want to clone it into a folder named `my-project`, use the following command:

   ```bash
   cd /path/to/my-project
3. Clone the repository using the git clone command followed by the repository URL. For example:
   ```bash
   git clone https://github.com/mr-prometheus/Cifar10RestAPIService
 4. After the repository is cloned, navigate into the repository folder:
	 ```bash
	 cd Cifar10RestAPIService
5. Now, you need to install the Python dependencies specified in the `requirements.txt` file. Run the following command:
	```bash 
	pip install -r requirements.txt
 This command will read the `requirements.txt` file and install all the necessary Python packages and dependencies.
 6. Once the installation is complete, you can explore and work with the Python files in the cloned repository.

That's it! You have successfully cloned the Git repository and installed the required Python dependencies using `pip`.

Unleash the transformative potential of your machine learning models by ensuring their real-world impact
