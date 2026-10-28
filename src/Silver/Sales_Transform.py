# Databricks notebook source
from pyspark.sql import functions as F
dbutils.widgets.text("catalog", "ce_ctg_dev")
catalog = dbutils.widgets.get("catalog")

df = (spark.table(f"{catalog}.ce_bronze.sales_raw")
      .withColumn("order_id", F.col("order_id").cast("int"))
      .withColumn("order_date", F.to_date("order_date"))
      .withColumn("amount", F.col("amount").cast("decimal(10,2)"))
      .filter(F.col("amount").isNotNull()))
df.write.mode("overwrite").saveAsTable(f"{catalog}.ce_silver.sales")