# Design Assumptions and Considerations
1. Assume 100 users using the service.<br>
2. Assume that the qps of the service is 60 requests per second.<br> 
3. Accumulate enough 1024 samples, and then retrain the model.<br> 

# System Design
The overall architecture of the system includes 4 parts: client, webserver, model API, database.<br>
In order to develop the system quickly, we use flask to process web requests and sqlite to store data.<br>
To reduce model complexity, we use mobilenet for image prediction.<br>
The system architecture diagram is as follows.<br>
![image](https://github.com/yjfdl123/image_classify/blob/main/data/images/architecture_of_image_classify.png)

# System implementation details
## Webserver API
We use flask as webserver and provide 5 routes.<br>
1. /metadata route that
Returns the versioned model informations that are available on the server.
2. /train route that
a. Re-train the model with new labeled dataset from the request. To keep it simple,
ignore any previous learnings, re-train the model with new data only. ML model
performance and accuracy are not part of this task.
3. /predict route that
a. Accepts a single valid image file in the request to be analyzed.
b. Returns the output from running the image against the latest trained model from
previous /train route, and saves a copy of model output and metrics in database.
4. /history route that
a. Returns all predictions history saved in the database.
5. /upload_image route thant 
a. upload image with label to train the model

## Code Structure
1. The service api related code is in the file server.py.
2. Model training related code is in the file model.py.
3. The database operation related code is in the file db_wrap.py. 
4. The code related to the client api operation is in the file clien.py. 
5. External control variables in file config.py.


## Dababase API
We use sqlite as a lightweight database.<br>
We created 2 data tables.<br>
The schema of the table is as follows. <br>
`
                create table if not exists model_version (
                    model_name text, 
                    model_version text
                )
`
`
                create table if not exists predict_score (
                    imagename text, 
                    model_name text, 
                    score real
                )
`
1. create_table is used to create a data table
2. insert_model_version is used to record the version information of the model
3. insert_image_score is used to record the historical score of the image
4. select_model_version is used to query all model version information
5. select_image_score is used to query the historical score of the image

## Model API 
We use lightweight mobilenet to classify images.
1. load_model is used to initialize the model. 
2. predict_image is used to classify uploaded images. 
3. finetune_model is used to fine-tune the model.
