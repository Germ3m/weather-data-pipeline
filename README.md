# weather-data-pipeline

An end-to-end ETL (Extract, Transform, Load) pipeline that extracts raw weather data from the Open-Meteo API, transforms and cleans it, and loads it into a PostgreSQL database. This project demonstrates core data engineering concepts using Python and PostgreSQL for scalable, maintainable data pipelines.

---

## Table of Contents

- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Project Structure](#project-structure)  
- [Setup](#setup)  
- [Usage](#usage)  
- [ETL Workflow](#etl-workflow)  
- [Getting Raw Data Example](#getting-raw-data-example)  
- [Contributing](#contributing)  

---

## Features

- Extracts hourly weather data (temperature, humidity, wind speed) from the Open-Meteo public API  
- Transforms nested JSON into structured rows  
- Loads cleaned data into a PostgreSQL database  
- Designed for scalability and maintainability  
- Demonstrates core data engineering concepts: API ingestion, data transformation, normalization, and relational database storage  

## Tech Stack

- **Python 3.10+** — Programming language  
- **Requests** — API interaction  
- **PostgreSQL** — Relational database  
## Project Structure

    weather-data-pipeline/
│
├── app.py # Main entry point, orchestrates ETL pipeline
├── extract.py # Handles API data extraction
├── transform.py # Cleans and transforms raw data
├── load.py # Loads processed data into PostgreSQL
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── .gitignore # Files/folders to ignore in Git
└── venv/ # Virtual environment (ignored in Git)


---

## Setup

1. Clone the repository:

- bash
- git clone git@github.com:your-username/- - - -  -weather-data-pipeline.git
- cd weather-data-pipeline

2. Create and activate a virtual environment:

- bash
- python3 -m venv venv
- source venv/bin/activate

3. Install dependencies:

- bash
- pip install -r requirements.txt

# Usage

- bash
- python app.py



