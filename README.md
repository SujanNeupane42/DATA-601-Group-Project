# Project Overview

This project includes data analysis, statistical analysis, and training and evaluating linear and polynomial regression models using a Jupyter Notebook. Additionally, it provides a Streamlit-based GUI for easy interaction with the models.

## Files
- **main_notebook.ipynb**: Contains data analysis, statistical analysis, and the training and evaluation of linear and polynomial regression models.
- **streamlit.py**: Contains the code to develop the GUI using Streamlit.

## Setting Up the Environment

### Prerequisites

- Python 3.10+
- `virtualenv` package

### Step-by-Step Instructions

1. **Clone the repository:**
    ```bash
    git clone https://github.com/SujanNeupane42/DATA-601-Group-Project
    cd DATA-601-Group-Project
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - **Windows:**
        ```bash
        venv\Scripts\activate
        ```
    - **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Streamlit app:**
    ```bash
    streamlit run streamlit.py
    ```

## Running the Jupyter Notebook

To open and run the `main_notebook.ipynb`, follow these steps:

1. **Activate the virtual environment (if not already activated):**

    - **Windows:**
        ```bash
        venv\Scripts\activate
        ```
    - **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

2. **Install Jupyter Notebook (if not already installed):**
    ```bash
    pip install jupyter
    ```

3. **Run Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```

4. **Open `main_notebook.ipynb` in the Jupyter interface and run the cells.**
