# Databricks notebook source
dbutils.widgets.text("catalog", "ce_ctg_dev")
catalog = dbutils.widgets.get("catalog")
path = f"/Volumes/{catalog}/ce_landing/raw/sales.csv"

rows = [
    "order_id,order_date,region,product,amount",
    "1,2026-10-01,Ontario,Widget,120.50",
    "2,2026-10-01,Quebec,Gadget,80.00",
    "3,2026-10-02,Ontario,Gadget,45.25",
    "4,2026-10-02,Alberta,Widget,200.00",
    "5,2026-10-03,Quebec,Widget,",
]
dbutils.fs.put(path, "\n".join(rows), overwrite=True)