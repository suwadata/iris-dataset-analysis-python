import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("iris.csv")

print(data.head())

print(data.shape)

print(data.columns)

print(data.info())

print(data.describe())

print(data["Species"])

print(data[["SepalLengthCm", "Species"]])

print(len(data))

print(data["Species"].value_counts())

#Filtering

setosa = data[data["Species"] == "Iris-setosa"]

print(setosa)

virginica = data[data["Species"] == "Iris-virginica"]

print(virginica)

#Average

print(data["SepalLengthCm"].mean())

print(data["PetalLengthCm"].mean())

#Max_and_Min

print(data["SepalLengthCm"].max())

print(data["SepalLengthCm"].min())

#Sorting_Data

print(data.sort_values("SepalLengthCm"))

print(data.sort_values("SepalLengthCm", ascending=False))

#checking species

print(data["Species"].unique())

#species count

print(data["Species"].value_counts())

#average petal width

print(data["PetalWidthCm"].mean())

#Petal Length Largest & Smallest Value

print(data["PetalLengthCm"].max())

print(data["PetalLengthCm"].min())

#Filtering

setosa = data[data["Species"] == "Iris-setosa"]
print(setosa)
print(len(setosa))

virginica = data[data["Species"] == "Iris-virginica"]
print(virginica)
print(len(setosa))

versicolor = data[data["Species"] == "Iris-versicolor"]
print(versicolor)
print(len(versicolor))

#Average petal length for each species

setosa = data[data["Species"] == "Iris-setosa"]
print(setosa["PetalLengthCm"].mean())

virginica = data[data["Species"] == "Iris-virginica"]
print(virginica["PetalLengthCm"].mean())

versicolor = data[data["Species"] == "Iris-versicolor"]
print(versicolor["PetalLengthCm"].mean())

#Grouping data according to species using groupby

grouped = data.groupby("Species")
print(grouped["PetalLengthCm"].mean())

print(data.groupby("Species")["PetalLengthCm"].mean())

print(data.isnull().sum())
print(data.duplicated().sum())
print(data.dtypes)

print(data.describe())

#EDA
#Difference in species measurement

print(data.groupby("Species")[[
    "SepalLengthCm",
    "SepalWidthCm",
    "PetalLengthCm",
    "PetalWidthCm"
]].mean())

#Smallest and Largest Species by PetalLength

petal_average = data.groupby("Species")["PetalLengthCm"].mean()

print(petal_average)

print("Species with the largest average petal length:")
print(petal_average.idxmax())

print("Species with the smallest average petal length:")
print(petal_average.idxmin())

petal_average.plot(kind="bar")

plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.xticks(rotation=0)
plt.show()

#Distribution of Sepal Length

plt.hist(data["SepalLengthCm"], bins=10)

plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Number of Flowers")

plt.show()

#distribution of petal length across the 3 species

data.boxplot(column ="PetalLengthCm", by="Species")
plt.title("Petal Length Distribution by Species")
plt.suptitle("")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")

plt.show()

#calculating correlations

correlation = data[
    ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
    ].corr()

print(correlation)


plt.figure(figsize=(8, 6))

sns.heatmap(correlation, annot=True, cmap="coolwarm")

plt.title("Correlation Between Iris Measurements")

plt.show()

                 



