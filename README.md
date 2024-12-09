# Wine Quality Prediction with Spark and AWS

# Project Overview

This project focuses on developing a machine learning (ML) model for wine quality prediction using Apache Spark’s MLlib on the AWS cloud platform. The goal is to utilize parallel processing on multiple EC2 instances for training and deploy a Docker container for simplified deployment of the prediction application.

## Features
1.	Parallel model training using Spark on 4 EC2 instances.
2.	Validation and tuning using the validation dataset.
3.	Wine quality prediction application with F1-score performance evaluation.
4.	Dockerized application for easy deployment on a single EC2 instance.

## Requirements

## Software
•	Java: JDK 8 or later <br>
•	Apache Spark: Version compatible with MLlib (e.g., Spark 3.x) <br>
•	Docker: Latest version <br>
•	Ubuntu Linux: Recommended OS for EC2 instances <br>
•	AWS CLI: For managing AWS resources <br>

## AWS Resources
•	4 EC2 Instances: For parallel model training. <br>
•	1 EC2 Instance: For model validation, tuning, and prediction.

## Input Files
1.	TrainingDataset.csv: Used for training the ML model in parallel.
2.	ValidationDataset.csv: Used for validating and optimizing the model.
3.	TestDataset.csv: For testing prediction functionality (not provided).

# Setup and Usage

## Step 1: Configure EC2 Instances
1.	Launch 4 EC2 instances (Ubuntu Linux) for parallel training.
2.	Ensure Java, Spark, and other dependencies are installed on each instance.
3.	Set up an SSH key pair for seamless communication between the instances.
4.	Configure a shared HDFS or S3 bucket to store datasets.

## Step 2: Data Preparation
1.	Upload TrainingDataset.csv and ValidationDataset.csv to HDFS or S3.
2.	Verify that the data files are accessible from all EC2 instances.

## Step 3: Model Training
1.	Clone the repository containing the project code
2.  Run the Spark training application on 4 EC2 instances
3.	The trained model will be saved in HDFS/S3 for future use.

## Step 4: Model Validation
1.	Run the model validation script on the master node
2.	The script outputs the F1 score and suggests parameter tuning options.

## Step 5: Prediction Testing
1.	Deploy the application on a single EC2 instance.
2.	Run the prediction script:
3.	The script outputs predictions and the F1 score.

# Dockerization
1.	Build the Docker container for the application
2.	Run the Docker container: