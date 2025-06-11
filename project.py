import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

def main(): 
    
    fig, axs = plt.subplots(2, 2, figsize=(12, 7), num='Pokemon Stats Distribution Visualization')
    
    df = pd.read_csv('data/Pokemon.csv', index_col=0)
    
    top_base_stats_legendary = find_best_stats_legendary(df)
    top_base_stats_non_legendary = find_best_stats_non_legendary(df)
    common_types = find_most_common_types(df)

    graph_best_stats_legendary(axs[0, 0], top_base_stats_legendary)
    graph_best_stats_non_legendary(axs[0, 1], top_base_stats_non_legendary)
    graph_type_distribution(axs[1, 0], common_types)

    plt.tight_layout()
    
    plt.show()


def find_best_stats_legendary(df):
    df = df.sort_values('Total', ascending=False).head(10)
    df = df.sort_values('Total', ascending=True)[['Name', 'Total']]
    return df

def find_best_stats_non_legendary(df):
    df = df[df['Legendary'] == False]
    df = df.sort_values('Total', ascending=False).head(10)
    df = df.sort_values('Total', ascending=True)[['Name', 'Total']]
    return df

def find_most_common_types(df):
    all_types = pd.concat([df['Type 1'], df['Type 2']])
    type_counts = all_types.dropna().value_counts()
    return type_counts

def graph_best_stats_legendary(axs, stat):
    axs.set_title('Top Stats for Legendaries', fontsize=12, weight='bold', color='skyblue')
    axs.barh(stat['Name'], stat['Total'])
    axs.tick_params(axis='y', labelsize=10)
    axs.grid(axis='x', linestyle='--', alpha=0.4)
    
    yticklabels = axs.get_yticklabels()
    yticklabels[-1].set_fontweight('bold')
    
def graph_best_stats_non_legendary(axs, stat):
    axs.set_title('Top Stats for Non-Legendaries', fontsize=12, weight='bold')
    axs.barh(stat['Name'], stat['Total'])
    axs.tick_params(axis='y', labelsize=10)
    axs.grid(axis='x', linestyle='--', alpha=0.4)
    
    yticklabels = axs.get_yticklabels()
    yticklabels[-1].set_fontweight('bold')
    
    
def graph_type_distribution(ax, type_counts):
    
    ax.set_title('Most Common Pokemon Types (Top 8)', fontsize=12, weight='bold', pad=15)

    # Take top 8 types
    top_types = type_counts.head(8)
    
    type_colors = {
        'Water': '#3399FF',     # Blue
        'Fire': '#FF4422',      # Red-orange
        'Grass': '#77CC55',     # Green
        'Electric': '#FFCC33',  # Yellow
        'Flying': '#A890F0',    # Light purple
        'Psychic': '#FF5599',   # Pinkish red
        'Bug': '#A8B820',       # Olive green
        'Normal': '#AAA',       # Gray
        'Poison': '#A040A0',    # Purple
        'Ground': '#E2BF65',    # Sandy brown
        'Rock': '#B8A038',      # Tan
        'Dark': '#705848',      # Dark brown
        'Ghost': '#705898',     # Purple-gray
        'Dragon': '#7038F8',    # Blue-purple
        'Steel': '#B8B8D0',     # Silver-blue
        'Ice': '#98D8D8',       # Light teal
        'Fairy': '#EE99AC',     # Light pink
        'Fighting': '#C03028'   # Red-brown
    }
    
    colors = [type_colors.get(t, '#888888') for t in top_types.index]  # default gray
    
    wedges, texts, autotexts = ax.pie(
        top_types,
        labels=top_types.index,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        textprops={'fontsize': 9}
    )
    
    for i, text in enumerate(texts):
        if i < 3:  # Top 3 most common
            text.set_fontsize(10)
            text.set_weight('bold')
        else:
            text.set_fontsize(8)

    for i, autotext in enumerate(autotexts):
        if i < 3:
            autotext.set_fontsize(9)
            autotext.set_weight('bold')
        else:
            autotext.set_fontsize(8)

    
    ax.axis('equal')


if __name__ == '__main__':
    main()