import pandas as pd

# Load the dataset
df = pd.read_csv("workload_data.csv")
print("Dataset loaded:")
print(df)
print("\n" + "=" * 60)

# Attributes (excluding the target class)
attributes = df.columns[:-1].tolist()
print(f"Attributes: {attributes}\n")

# Initialize hypothesis to None (will be set by first positive example)
hypothesis = None

print("Find-S Algorithm Execution Trace")
print("=" * 60)

for idx, row in df.iterrows():
    instance = row[attributes].tolist()
    target = row["High-Performance Edge"]

    print(f"\nProcessing Workload W{idx + 1}: {instance} -> Target: {target}")

    if target == "Yes":  # Positive instance
        if hypothesis is None:
            # First positive example becomes the initial hypothesis
            hypothesis = instance.copy()
            print(f"  First positive example. Initialize h = {hypothesis}")
        else:
            # Generalize hypothesis where it doesn't match the instance
            for i in range(len(hypothesis)):
                if hypothesis[i] != instance[i]:
                    hypothesis[i] = "?"
            print(f"  Positive example. Updated h = {hypothesis}")
    else:
        # Ignore negative instances
        print(f"  Negative example. Hypothesis unchanged: {hypothesis}")

print("\n" + "=" * 60)
print(f"Final Specific Hypothesis (h): {hypothesis}")
print("=" * 60)

# Pretty print the hypothesis with attribute names
print("\nFinal Hypothesis in attribute-constraint form:")
for attr, val in zip(attributes, hypothesis):
    print(f"  {attr}: {val}")
