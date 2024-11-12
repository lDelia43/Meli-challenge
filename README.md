# Mutant Detector API

This Django-based API detects whether a DNA sequence belongs to a mutant or a human. It also provides statistics on the analyzed sequences.

## Table of Contents
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
5. [Usage](#usage)
7. [Running Tests](#running-tests)
8. [Cloud URL](#url)
8. [Curl Examples](#curls)

## Features
- Detect if a given DNA sequence is mutant or human.
- Store DNA sequences and detection results in the database.
- Provide statistics on the number of mutant and human sequences.

## Prerequisites
- Python 3.8+
- Django 3.2+
- PostgreSQL (or another compatible database)

## Installation

1. **Clone the repository**
- git clone https://github.com/yourusername/mutant-detector.git
- cd mutant-detector

2. **Install depedencies**
- pip install -r requirements.txt

3. **Migrations**
- python3 manage.py migrate
- python3 manage.py collectstatic

## Usage
- python3 manage.py runserver

## Running Tests
- python3 manage.py test dna

## Endpoints
- mutant
- stats
- admin

## URL (CLOUD)
"For inactivity the requests which can delay requests by 50 seconds or more, because is a free instance on Render."
- https://meli-challenge-lb0x.onrender.com/

## Curls Examples
    curl --location '{{protocol}}://{{hostname}}/mutant/' \
    --header 'Content-Type: application/json' \
    --data '{"dna": ["GTCGGA", "GAGTGC", "TTATGT", "AGAAGG", "CTTCTA", "TCACTG"]}'

    curl --location --request GET '{{protocol}}://{{hostname}}/stats/' \
    --header 'Content-Type: application/json' \