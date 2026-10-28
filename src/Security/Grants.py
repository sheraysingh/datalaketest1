# Databricks notebook source
dbutils.widgets.text("catalog", "ce_ctg_dev")
catalog = dbutils.widgets.get("catalog")

spark.sql(f"GRANT USE CATALOG ON CATALOG {catalog} TO `account users`")
spark.sql(f"GRANT USE SCHEMA, SELECT ON SCHEMA {catalog}.ce_gold TO `account users`")