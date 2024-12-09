import sys
import boto3
import logging
from pyspark.sql import SparkSession
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml import PipelineModel
from pyspark.sql.functions import col

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clean_data(df):
    """Clean and prepare DataFrame by casting all columns to double."""
    logger.info("Cleaning data... Converting all columns to double type.")
    return df.select(*(col(c).cast("double").alias(c.strip("\"")) for c in df.columns))

def load_model(model_path):
    """Load the saved model from the specified path."""
    logger.info(f"Loading model from {model_path}...")
    model = PipelineModel.load(model_path)
    return model

def main():
    # Setup Spark session
    logger.info("Starting Spark session...")
    spark = SparkSession.builder \
        .appName('Wine_Quality_Prediction') \
        .getOrCreate()

    # Input arguments
    test_data_path = sys.argv[1]  # Path to the test data file
    model_path = sys.argv[2]      # Path to the saved model

    # Load test data
    logger.info(f"Loading test data from {test_data_path}...")
    test_df = spark.read.format("csv").option('header', 'true').option("sep", ";").load(test_data_path)
    cleaned_test_df = clean_data(test_df)

    # Load the model
    model = load_model(model_path)

    # Predict with the model
    logger.info("Predicting with the model...")
    predictions = model.transform(cleaned_test_df)

    # Evaluate the model using accuracy
    evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction", metricName="accuracy")
    accuracy = evaluator.evaluate(predictions)
    logger.info(f"Test Accuracy: {accuracy}")

    # Stop Spark session
    spark.stop()

if __name__ == "__main__":
    main()

