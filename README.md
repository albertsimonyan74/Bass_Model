# Bass Model Implementation

This repository contains an implementation of the **Bass Model for Innovation Diffusion**, a mathematical model that describes the adoption of new products or technologies over time.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Introduction
The **Bass Diffusion Model** predicts the rate of adoption of a new product based on two key factors:
- **Innovators** (coefficient of innovation, denoted as `p`)
- **Imitators** (coefficient of imitation, denoted as `q`)

This implementation provides a Python-based simulation, visualization, and parameter estimation for the Bass Model.

## Installation
To set up the project, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Bass-Model.git
   cd Bass-Model
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the model:
```bash
python main.py
```
This will execute the simulation and display the adoption curve.

## Project Structure
```
Bass-Model/
│── .git/                  # Git repository files
│── .venv/                 # Python virtual environment
│── data/                  # Sample datasets
│── scripts/
│   ├── bass_model.ipynb      # Bass Model implementation
│   ├── utility_functions.py           # Helper functions
│── report /
│── requirements.txt       # List of dependencies
│── README.md              # Project documentation
```




