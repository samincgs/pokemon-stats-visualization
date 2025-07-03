# Pokémon Stats Distribution Visualization

![graph](https://github.com/user-attachments/assets/a96bee84-44b1-454f-ab8f-7fe8aaa7808b)

## Description

This project is a data visualization program designed to explore and present insights from a Pokémon dataset. Since Pokemon is a game that has a special place in my heart, I wanted to create a fun little visualization that displays some interesting statistics that other's might not know. This program leverages Python's `pandas` and `matplotlib` libraries to showcase patterns and comparisons across different Pokémon categories, such as Legendary status, type distribution, and dual-typing effects on total base stats.

<!--add video demo here, fill out the form -->

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

The dataset is publicly available on Kaggle and can be accessed [here](https://www.kaggle.com/datasets/abcsds/pokemon?resource=download).
Credits to Alberto Barradas for the dataset.

### Project Files

This project consists of two main Python files:

#### `project.py`

This file contains all the **data analysis and visualization logic**.
