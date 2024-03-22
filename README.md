# Build Your Own GPT

This repository contains the live-coding part of the 2024 AMLD workshop "At the cutting edge of Generative AI - Unravel the Secrets of GPT and Build Your Own Model". 
You can find the accompanying slides [here](https://speakerdeck.com/donlelef/amld-2024-build-your-own-gpt).

As stated during the workshop, the project as a whole is inspired by the excellent [Zero To Hero](https://karpathy.ai/zero-to-hero.html) course from Andrej Karpathy.
## Project Structure

Under the `notebooks` directory you can find both the live coding notebook, `build_your_own_gpt.ipynb`, and the working demo `demo_text_generation.ipynb`.

Under the `src` directory you will find some functions and classes extracted from the live coding notebook and used in the demo one.

Both data and models generated during live coding are versioned under respective directories, in order to make the demo immediately available. 

## Project Setup in a local environment

Project dependencies are specified in the `pyproject.toml` file and can be installed using the [Poetry](https://python-poetry.org/) package manager. 

To install the dependencies using Poetry, you would first need to ensure that Poetry is installed on your system.
If it's not, you can install it using the following command in your terminal:
```curl -sSL https://install.python-poetry.org | python3 -```

Once Poetry is installed, navigate to the project directory where the pyproject.toml file is located.
Then, you can install the dependencies using the following command:
```poetry install --no-root```

To run the notebooks, you can use [Jupyter Lab](https://jupyterlab.readthedocs.io/en/latest/).
If you have installed the project dependencies using Poetry, you can run Jupyter Lab from the virtual environment using the following command:
```poetry run jupyter lab```

## Project Setup on Google Colab

Alternatively, you can open and run the live coding notebook `build_your_own_gpt.ipynb` on Google Colab by simply clicking here:
<a target="_blank" href="https://colab.research.google.com/github/xtreamsrl/build-your-own-gpt/blob/master/build_your_own_gpt.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
