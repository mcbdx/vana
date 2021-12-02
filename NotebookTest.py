# Databricks notebook source
df = spark.read.parquet("/databricks-datasets/amazon/test4K")
display(df)

# COMMAND ----------

import os 

os.getcwd()

# COMMAND ----------

print(os.getcwd() + "/demo.csv")

# COMMAND ----------

import csv
with open(os.getcwd() + "/demo.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# COMMAND ----------

import databricks.koalas as kd

df_koalas = kd.read_csv(f"file:{os.getcwd()}/demo.csv")
display(df_koalas)

# COMMAND ----------

csv_df = spark.read.csv(f"file:{os.getcwd()}/demo.csv", header=True) # "file:" prefix and absolute file path are required for PySpark
display(csv_df)

# COMMAND ----------

from reader import csv_reader

df = csv_reader("demo.csv")
print(df.head())

# COMMAND ----------

# MAGIC %md 
# MAGIC Hello this is a test

# COMMAND ----------

print("hello world")

# COMMAND ----------


