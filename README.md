# Build Your Own GPT

This repository contains the materials for the 2024 AMLD workshop titled "At the cutting edge of Generative AI - Unravel the Secrets of GPT and Build Your Own Model".
As stated during the workshop, the project as a whole is inspired by the **Zero To Hero** course from Andrej Karpathy, which you can find [here](https://karpathy.ai/zero-to-hero.html). 

## Project Structure

Under the `notebooks` directory you can find both the live coding notebook, `build_your_own_gpt.ipynb`, and the working demo `demo_text_generation.ipynb`.

Under the `src` directory you will find some functions and classes extracted from the live coding notebook and used in the demo one.

Both data and models generated during live coding are versioned under respective directories, in order to make the demo immediately available. 

## Project Setup

Project dependencies are specified in the `pyproject.toml` file and can be installed using the [Poetry](https://python-poetry.org/) package manager. 
To install the dependencies using Poetry, you would first need to ensure that Poetry is installed on your system.
If it's not, you can install it using the following command in your terminal:
```curl -sSL https://install.python-poetry.org | python3 -```

Once Poetry is installed, navigate to the project directory where the pyproject.toml file is located.
Then, you can install the dependencies using the following command:
```poetry install```

This command will read the pyproject.toml file and install the specified dependencies in a new virtual environment.
If you want to use the virtual environment for your project, you can activate it using:
```poetry shell```

Now, you should be able to use the installed dependencies in your project.

## Running the Notebooks

To run the notebooks, you can use [Jupyter Lab](https://jupyterlab.readthedocs.io/en/latest/).
If you have installed the project dependencies using Poetry, you can run Jupyter Lab from the virtual environment using the following command:
```poetry run jupyter lab```

## Author
The project is authored by Gabriele Orlandi. For any queries, you can reach out at gabriele.orlandi@xtreamers.io. 