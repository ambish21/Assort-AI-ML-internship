# Day 20 — README.md

# MongoDB Aggregation Framework

## Overview

This project covers the MongoDB Aggregation Framework and its use in analyzing sales data.

## Topics Covered

* `$match`
* `$group`
* `$project`
* `$sort`
* `$lookup`
* `$unwind`

## Project: Sales Analytics Dashboard Backend

A Python-based CLI application connected to MongoDB for analyzing sales data.

### Features

* Calculate Total Sales and Total Revenue
* Generate Monthly Sales Reports
* Find Top-Selling Products
* Generate Category-wise Revenue Reports

## Collections Used

* `sales`
* `products`

## Technologies Used

* Python
* MongoDB
* PyMongo
* MongoDB Compass
* Python Dotenv

## How to Run

```bash
pip install pymongo python-dotenv
python seed_data.py
python main.py
```

## Result

All aggregation queries were successfully tested using both the Python CLI and MongoDB Compass. The project was pushed to the `my-first-branch` on GitHub.
