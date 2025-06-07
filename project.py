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
    
    # print(find_types)
    
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
    axs.set_title('Top Stats for Legendaries')
    axs.barh(stat['Name'], stat['Total'])
    axs.tick_params(axis='y', labelsize=10)
    axs.grid(False)
    
def graph_best_stats_non_legendary(axs, stat):
    axs.set_title('Top Stats for Non-Legendaries')
    axs.barh(stat['Name'], stat['Total'])
    axs.tick_params(axis='y', labelsize=10)
    axs.grid(False)
    
def graph_type_distribution(ax, type_counts):
    ax.set_title('Most Common Pokemon Types')
    ax.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')


if __name__ == '__main__':
    main()