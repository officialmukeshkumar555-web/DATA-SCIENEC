# 03-rainwater.py
# Topic: Left tallest bars, Right tallest bars, Rainwater trapped

def rainwater(n):
    bars = [0, n, 0, n, 0]
    return min(max(bars[:3]), max(bars[2:])) - bars[2]

input("rainwater(n) traps water between two bars of height n.  Press Enter ")
print("  rainwater(3) =", rainwater(3))
print("  rainwater(4) =", rainwater(4))
n = int(input("Enter bar height (try 5 or 6): "))
guess = input("What is rainwater(" + str(n) + ")? ")
input("water = min(left tallest, right tallest) - bar height at the gap.  Press Enter ")
print("  rainwater(" + str(n) + ") =", rainwater(n), "  your guess:", guess)# ============================================================
# Seaborn Library in Python
# Activity: World Animals Explorer
# ============================================================

import seaborn as sns
import matplotlib.pyplot as plt

# ---- PART 1: What is Seaborn — Import and Load Data ----

df = sns.load_dataset('penguins')
df = df.dropna()

print("First 5 rows:")
print(df.head())
print()
print(df.info())
print()
print(df.describe())
print()
print("Species:", df['species'].unique())
print("Islands:", df['island'].unique())


# ---- PART 2: Histogram ----

sns.histplot(data=df, x='body_mass_g', bins=20, color='steelblue')
plt.title('Distribution of Penguin Body Mass')
plt.xlabel('Body Mass (grams)')
plt.ylabel('Count')
plt.show()


# ---- PART 3: KDE Plot and Fitting Distribution ----

sns.kdeplot(data=df, x='flipper_length_mm', hue='species', fill=True)
plt.title('Flipper Length Shape by Species (KDE)')
plt.xlabel('Flipper Length (mm)')
plt.show()

sns.histplot(data=df, x='flipper_length_mm', kde=True, color='coral')
plt.title('Flipper Length — Histogram with KDE Curve')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Count')
plt.show()


# ---- PART 4: Scatter Plot ----

sns.scatterplot(data=df, x='flipper_length_mm', y='body_mass_g', hue='species')
plt.title('Flipper Length vs Body Mass by Species')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (grams)')
plt.show()


# ---- PART 5: Heatmap ----

corr = df.corr(numeric_only=True)
print("Correlation table:")
print(corr)
print()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap — Penguin Measurements')
plt.show()
