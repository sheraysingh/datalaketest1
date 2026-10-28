# Databricks notebook source
from pyspark.sql import functions as F
dbutils.widgets.text("catalog", "ce_ctg_dev")
catalog = dbutils.widgets.get("catalog")

df = (spark.table(f"{catalog}.ce_silver.sales")
      .groupBy("region")
      .agg(F.count("*").alias("orders"), F.sum("amount").alias("total_amount")))
df.write.mode("overwrite").saveAsTable(f"{catalog}.ce_gold.sales_by_region")