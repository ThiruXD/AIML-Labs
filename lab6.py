import math
from collections import Counter

# 1. Dataset definition
data = [
    {"Outlook": "Sunny", "Temperature": "Hot", "Humidity": "High", "Wind": "Weak", "Play Tennis": "No"},
    {"Outlook": "Sunny", "Temperature": "Hot", "Humidity": "High", "Wind": "Strong", "Play Tennis": "No"},
    {"Outlook": "Overcast", "Temperature": "Hot", "Humidity": "High", "Wind": "Weak", "Play Tennis": "Yes"},
    {"Outlook": "Rain", "Temperature": "Mild", "Humidity": "High", "Wind": "Weak", "Play Tennis": "Yes"},
    {"Outlook": "Rain", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Weak", "Play Tennis": "Yes"},
    {"Outlook": "Rain", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Strong", "Play Tennis": "No"},
    {"Outlook": "Overcast", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Strong", "Play Tennis": "Yes"},
    {"Outlook": "Sunny", "Temperature": "Mild", "Humidity": "High", "Wind": "Weak", "Play Tennis": "No"},
    {"Outlook": "Sunny", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Weak", "Play Tennis": "Yes"},
    {"Outlook": "Rain", "Temperature": "Mild", "Humidity": "Normal", "Wind": "Weak", "Play Tennis": "Yes"},
    {"Outlook": "Sunny", "Temperature": "Mild", "Humidity": "Normal", "Wind": "Strong", "Play Tennis": "Yes"},
    {"Outlook": "Overcast", "Temperature": "Mild", "Humidity": "High", "Wind": "Strong", "Play Tennis": "Yes"},
    {"Outlook": "Overcast", "Temperature": "Hot", "Humidity": "Normal", "Wind": "Weak", "Play Tennis": "Yes"},
    {"Outlook": "Rain", "Temperature": "Mild", "Humidity": "High", "Wind": "Strong", "Play Tennis": "No"}
]

TARGET_ATTR = "Play Tennis"
FEATURES = ["Outlook", "Temperature", "Humidity", "Wind"]

# 2. Entropy and Information Gain calculations
def entropy(rows, target_attr):
    labels = [row[target_attr] for row in rows]
    counts = Counter(labels)
    total = len(rows)
    return -sum((cnt / total) * math.log2(cnt / total) for cnt in counts.values())

def info_gain(rows, feature, target_attr):
    base_entropy = entropy(rows, target_attr)
    values = set(row[feature] for row in rows)
    total = len(rows)
    
    weighted_entropy = 0.0
    for val in values:
        subset = [row for row in rows if row[feature] == val]
        weighted_entropy += (len(subset) / total) * entropy(subset, target_attr)
        
    return base_entropy - weighted_entropy

# 3. Recursive ID3 Tree Construction
def id3(rows, features, target_attr):
    labels = [row[target_attr] for row in rows]
    
    # Base Case 1: Pure node
    if len(set(labels)) == 1:
        return labels[0]
    
    # Base Case 2: No more features to split on -> majority vote
    if not features:
        return Counter(labels).most_common(1)[0][0]
    
    # Select feature with highest Information Gain
    best_feature = max(features, key=lambda f: info_gain(rows, f, target_attr))
    
    tree = {best_feature: {}}
    remaining_features = [f for f in features if f != best_feature]
    
    # Split across unique values of the best feature
    unique_vals = set(row[best_feature] for row in rows)
    for val in unique_vals:
        subset = [row for row in rows if row[best_feature] == val]
        if not subset:
            tree[best_feature][val] = Counter(labels).most_common(1)[0][0]
        else:
            tree[best_feature][val] = id3(subset, remaining_features, target_attr)
            
    return tree

# 4. Tree Pretty Printer
def display_tree(node, depth=0):
    indent = "  " * depth
    if not isinstance(node, dict):
        print(f"{indent}-> {node}")
        return
    
    for feature, branches in node.items():
        for branch_val, subtree in branches.items():
            print(f"{indent}[{feature} = {branch_val}]")
            display_tree(subtree, depth + 1)

# Build and display
decision_tree = id3(data, FEATURES, TARGET_ATTR)
print("Resulting Decision Tree:")
display_tree(decision_tree)
