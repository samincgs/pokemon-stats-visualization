import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


GRAPH_TITLE_COLORS = {
    
}
TYPE_COLORS = {
        'Water': '#3399FF',     
        'Fire': '#FF4422',      
        'Grass': '#77CC55',     
        'Electric': '#FFCC33',  
        'Flying': '#A890F0',   
        'Psychic': '#FF5599',   
        'Bug': '#A8B820',      
        'Normal': '#AAA',       
        'Poison': '#A040A0',    
        'Ground': '#E2BF65',    
        'Rock': '#B8A038',      
        'Dark': '#705848',      
        'Ghost': '#705898',     
        'Steel': '#B8B8D0',     
        'Ice': '#98D8D8',       
        'Fairy': '#EE99AC',     
        'Fighting': '#C03028'   
    }

plt.style.use('fivethirtyeight')

def main(): 
    
    fig, axs = plt.subplots(2, 2, figsize=(12, 7), num='Pokemon Stats Distribution Visualization')
    
    df = pd.read_csv('data/Pokemon.csv', index_col=0) # data already cleaned (source: kaggle)
    
    
    top_base_stats_legendary = find_best_stats_legendary(df)
    top_base_stats_non_legendary = find_best_stats_non_legendary(df)
    common_types = find_most_common_types(df)
    common_stats = find_most_common_stat(df)

    graph_best_stats_legendary(axs[0, 0], top_base_stats_legendary)
    graph_best_stats_non_legendary(axs[0, 1], top_base_stats_non_legendary)
    graph_type_distribution(axs[1, 0], common_types)

    plt.tight_layout()
    
    # plt.show()

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
    df = pd.concat([df['Type 1'], df['Type 2']])
    df = df.dropna(axis=0).value_counts()
    df = df.head(10)
    return df

def find_most_common_stat(df):
    df = df.loc[:, ['HP', 'Attack', 'Defense', 'Sp. Atk' ,'Sp. Def', 'Speed']]
    # print(df.sum())

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
    
    
def graph_type_distribution(axs, stat):
    axs.set_title('Most Common Pokemon Types Throughout all Generations', fontsize=12, weight='bold', pad=15)
    
    colors = [TYPE_COLORS[c] for c in stat.index]
                
    wedges, texts, autotexts = axs.pie(
        stat,
        labels=stat.index,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        textprops={'fontsize': 9}
    )
    
    for i, text in enumerate(texts):
        if i < 3:  # top 3 most common
            text.set_fontsize(10)
            text.set_weight('bold')
        else:
            text.set_fontsize(9)

    for i, autotext in enumerate(autotexts):
        if i < 3:
            autotext.set_fontsize(9)
            autotext.set_weight('bold')
        else:
            autotext.set_fontsize(8)

    


if __name__ == '__main__':
    main()