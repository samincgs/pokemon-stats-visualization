import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

def main(): 
    
    fig, axs = plt.subplots(2, 2, figsize=(8, 5), num='Pokemon Stats Distribution Visualization')
    
    df = pd.read_csv('data/Pokemon.csv', index_col=0)
    
    top_base_stats_legendary = find_best_stats_legendary(df)
    top_base_stats_non_legendary = find_best_stats_non_legendary(df)
    
    graph_best_stats_legendary(axs[0, 0], top_base_stats_legendary)
    graph_best_stats_non_legendary(axs[0, 1], top_base_stats_non_legendary)

  
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

def find_total_stats_per_type(df):
    pass


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


if __name__ == '__main__':
    main()