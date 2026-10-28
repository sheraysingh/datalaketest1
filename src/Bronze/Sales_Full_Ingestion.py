# Databricks notebook source
dbutils.widgets.text("catalog", "ce_ctg_dev")
catalog = dbutils.widgets.get("catalog")

df = spark.read.option("header", "true").csv(f"/Volumes/{catalog}/ce_landing/raw/sales.csv")
df.write.mode("overwrite").saveAsTable(f"{catalog}.ce_bronze.sales_raw")