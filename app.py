#%%
import pandas as pd
import matplotlib.pyplot as plt

#%%
# Read Csv
df = pd.read_csv('sample_data/VNL2023.csv')

print(df.head(10))

# %%
# Get info csv
print(df.info()) 

# %%
# Dataframe to string
new_df = df.to_string()
print(new_df)
# %%
# Get all player by country
filter_player_by_country = df.loc[df["Country"] == "Slovenia"]

print(filter_player_by_country)

# %%
# Get all by position
filter_player_by_position = df.loc[df["Position"] == "OH"]

print(filter_player_by_position)

# %%
# Get best 5 OH
def get_five_best_oh(df, position_column, attack_column):
    # filter data frame 
    filtered_df = df[df[position_column] == "OH"]

    sorted_df = filtered_df.sort_values(by=attack_column,ascending=False)

    top_five  = sorted_df.head(5)
    return top_five


df = pd.read_csv('sample_data/VNL2023.csv')
best_oh = get_five_best_oh(df,"Position", "Attack")

print(best_oh)
# %%
def get_five_best_digger(df, position_column, column):
    filter_dataframe = df[df[position_column] == "OH"]
    sorted_df = filter_dataframe.sort_values(by=column,ascending=False)

    top_five = sorted_df.head(5)

    return top_five


df = pd.read_csv('sample_data/VNL2023.csv')
best_libero = get_five_best_digger(df, "Position", "Dig")
print(best_libero)

# %%
# Data visualization

df.groupby("Position")["Attack"].mean().plot(kind="bar", title="Average Attack by Position")
plt.xlabel("Position")
plt.ylabel("Average attack")
plt.show()
# %%
