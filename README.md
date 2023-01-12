# Amazon Product Recommendation from Reviews Dataset


__Introduction__:

In the current digital landscape of burgeoning data and the possibility to shop from the comfort of your home, the product catalogs on e-commerce websites are imploding. While this presents a good business opportunity for these companies, this can quickly turn into a disaster if each customer finds themselves lost in this online marketplace, unable to get the product that they are looking to buy. 

To mitigate this problem, we propose to design a recommendation system - personalized to the taste of each customer - old or new! Such a recommendation system that caters to each the needs of each user and provides them with the promised shopping experience, leading to improved numbers for customer retention and satisfaction. 

To build this recommendation engine, we have carefully cherry-picked the components - from the datastore to be used to how the models will be trained and deployed to make the system scalable and robust. 

__DOMAIN:__ E-Commerce<br>

__DATASET USED:__

https://nijianmo.github.io/amazon/index.html#complete-data

__Data Description__:

Structure of a Review
reviewerID - ID of the reviewer, e.g. A2SUAM1J3GNN3B<br>
asin - ID of the product, e.g. 0000013714<br>
reviewerName - name of the reviewer<br>
helpful - helpfulness rating of the review, e.g. 2/3<br>
reviewText - text of the review<br>
overall - rating of the product<br>
summary - summary of the review<br>
unixReviewTime - time of the review (unix time)<br>
reviewTime - time of the review (raw)<br>

Structure of metadata
asin - ID of the product, e.g. 0000031852<br>
title - name of the product<br>
price - price in US dollars (at time of crawl)<br>
imUrl - url of the product image<br>
related - related products (also bought, also viewed, bought together, buy after viewing)<br>
salesRank - sales rank information<br>
brand - brand name<br>
categories - list of categories the product belongs to<br>

__Methodology__:


__Storage__- The idea is to download and store the dataset in mongoDB and use ElasticSearch storage for scalability.


__Data Preprocessing__- We would use Spark to preprocess the data which would entail all the processes from cleaning to evaluating useful features on which the recommendation model would be trained.


__Training the model__- Using sparkML, we would train the embeddings from data stored on ElasticSearch.


__Recommendation__- Using Elasticsearch queries, we will generate some example recommendations.


__FrontEnd__- We will display the results using a frontend application which would cover some  recommendations of the product for a particular user.

__Implementation Details (Milestone Submission)__ <br>

The Collections.py file present under Database folder, contains a Python script which loads the collections-"DigitalMusic" , "MoviesAndTv" ,"VinylAndCD" from the Amazon Reviews Dataset into MongoDB server.


__Steps to run the code__:

__Connection  to MongoDB__:
Create a mongoDB account and follow the installation instructions (make sure to whitelist your IP)
Install mongo shell and pymongo on your system (you may want to either install directly or execution binaries for successful installation of components)

![MongoDB cluster web UI](https://github.com/cs532-Fall22/project-team_11/blob/main/images/mongoConnectCluster.png)


On the online free tier version: This is what the interface would look like once you click on connect.


Follow the processes to copy the connection string and create a client node as show in the code below.
Code:
usr = os.getenv("USR")
password = os.getenv("PASS")

client=pymongo.MongoClient(f'mongodb+srv://{usr}:{password}@project.fq5sh6t.mongodb.net/?retryWrites=true&w=majority')


Once successfully connected, you should be able to connect to the project you create and read the database.

db = client["reviews"] is the database reviews fetched from the client request.


Note: You would need to create a .env file in your project of the format:

USR: <your mongodb username in the string>
PASS: <your cluster password>
LOCAL: <path to the datasets>

We need to create a .env file hosting the path variables and the usr and password variables that you will create while signing onto the MongoDB cluster.

__Creating a database__:

Once the connection is successful. In the project terminal, run the script:
python collection.py

If the path to the datasets in the env is set correctly, you will be able to see the database being pushed onto the MongoDB cluster which can be later fetched for data processing for spark.

Test:

Run showcollection.py file to check if the connection to the database is successful.

This is the output which you might expect to see if things run smoothly.

![dataframe example](https://github.com/cs532-Fall22/project-team_11/blob/main/images/dataframe.png)

Cleaning the data for spark:

Run script.py to generate 2 files metaVinyAndCD.txt and VinylAndCD.txt as inputs to the spark query processing file and mention the correct paths.

Execute Command: python script.py

These are the first 20+ records that you might expect after cleaning the data using the above command in the file VinyAndCD.txt

![dataset](https://github.com/cs532-Fall22/project-team_11/blob/main/images/dataVinylAndCD.png)

__Data Processing in Spark__:

The File: P2PRecommendations.ipynb contains the data processing component using Spark for product to product recommendations.

Here 2 types of reading mechanisms are implemented, one slightly more complicated than the other.

Method 1: (Easy)
Reading from the text files and that were generated by script.py file by giving correct paths.

We used google collab for this project which reads the data using standard spark.read.json command with a path to the file.

Ex: 
![Schema definition](https://github.com/cs532-Fall22/project-team_11/blob/main/images/schema.png)

Make sure to give the correct path to your cleaned data using the command
df = spark.read.json(“<path>”)

Method 2: (Complicated) and might cause connection timeout errors if using collab since it recalibrates runtime when requesting large data over the network.

![Connecting to MongoDB](https://github.com/cs532-Fall22/project-team_11/blob/main/images/colabMongoDB.png)



__Components__:
Uri:  is the mongo string that is a unique identifier to your database. Add your connection string if you want to run the code through MongoDB else it won’t work. This field is deliberately hidden because of security and privacy issues of the database.

The spark.read.format(“mongo”): part of the script assumes that you are running your pyspark-mongo shell from the terminal on which you hosted your notebook.
(Read the documentation to set that up before initializing the notebook)

Collab requires separate configuration based on the relative access given.

__Query processing__:
Run each cell to generate the most optimized query processing models for generating product to product based recommendation.


