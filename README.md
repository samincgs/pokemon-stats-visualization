# Pokémon Stats Distribution Visualization

![graph](https://github.com/user-attachments/assets/a96bee84-44b1-454f-ab8f-7fe8aaa7808b)

## Description

This project is a data visualization program designed to explore and present insights from a Pokémon dataset. Since Pokemon is a game that has a special place in my heart, I wanted to create a fun little visualization that displays some interesting statistics that other's might not know. This program leverages `Excel` and Python's `pandas` and `matplotlib` libraries to showcase patterns and comparisons across different Pokémon categories, such as Legendary status, type distribution, and dual-typing effects on total base stats.

Video Link: [https://www.youtube.com/watch?v=nSa-Su_FPX4](https://www.youtube.com/watch?v=nSa-Su_FPX4)

### Dataset

The dataset used in this project is a cleaned version of the original `Pokemon.csv` file, sourced from Kaggle. It contains detailed information on 721 Pokémon across multiple generations, including their base stats, types, and whether they are classified as Legendary.

#### Key Features

- **#**: Pokémon ID number
- **Name**: Pokémon name
- **Type 1**: Primary Pokémon type (e.g., Water, Fire)
- **Type 2**: Secondary Pokémon type (if applicable)
- **HP**: Hit Points (health)
- **Attack**: Physical attack stat
- **Defense**: Physical defense stat
- **Sp. Atk**: Special attack stat
- **Sp. Def**: Special defense stat
- **Speed**: Speed stat
- **Generation**: Generation number (1 to 6)
- **Legendary**: Boolean flag indicating if the Pokémon is Legendary

#### Source

The dataset is publicly available on Kaggle and can be accessed [here](https://www.kaggle.com/datasets/abcsds/pokemon?resource=download). </br>
Credits to Alberto Barradas for the dataset.

### Project Files

This project consists of two main Python files:

#### `project.py`

This is the core of the application. The file contains all the **data analysis and visualization logic**. It is responsible for reading the dataset, performing transformation steps, and generating insights. All of this is accomplished using Python’s data analysis libraries, including **pandas** and **matplotlib**. The code is written using a modular approach. I have functions that take the DataFrame and extract or transform the necessary data, and separate functions that take that data and generate the four visualizations. By keeping data processing and visualization logic separate, the code is easier to read, test, maintain, and debug.

#### `test_project.py`

This file contains all the unit tests for the core functions in the main script. It uses the **pytest** framework to test each function responsible for extracting and transforming the data. For each of the four main extraction functions, I wrote two tests: one where the input DataFrame contains fewer than 10 entries, and one where it contains more than 10. This is important because most of the extraction functions are designed to return the top 8 or 10 items, depending on the specific logic. By testing both edge cases, I ensured that the functions behave correctly regardless of the size of the input data.

## Conclusion

The visualization reveals clear trends in Pokémon design across generations. Legendary Pokémon consistently have the highest total base stats, reinforcing their role as powerful and rare figures in the game. Among non legendaries, a few standouts like Slaking and Garchomp approach legendary level strength, particularly among pseudo-legendaries. Water-type Pokémon are the most common overall, reflecting their frequent presence in each generation and their importance to game balance. Additionally, dual-type Pokémon tend to have higher average stats compared to single-type ones, suggesting that versatility often comes with a statistical advantage.
