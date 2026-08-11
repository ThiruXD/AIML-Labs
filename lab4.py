# ============================================================
# Candidate Elimination Algorithm
# ============================================================
# Dataset: EnjoySport
# Attributes: Sky, AirTemp, Humidity, Wind
# Target: EnjoySport
# ============================================================


# Training Dataset
data = [
    ["Sunny", "Warm", "Normal", "Strong", "Yes"],  # D1
    ["Sunny", "Warm", "High",   "Strong", "Yes"],  # D2
    ["Rainy", "Cold", "High",   "Strong", "No"],   # D3
    ["Sunny", "Warm", "High",   "Weak",   "Yes"]   # D4
]


# Attribute domains
domains = [
    ["Sunny", "Rainy"],       # Sky
    ["Warm", "Cold"],         # AirTemp
    ["Normal", "High"],       # Humidity
    ["Strong", "Weak"]        # Wind
]


# ------------------------------------------------------------
# Function to check whether a hypothesis covers an instance
# ------------------------------------------------------------
def covers(hypothesis, instance):
    for h, value in zip(hypothesis, instance):

        # '?' matches any value
        if h == "?":
            continue

        # '∅' does not cover anything
        if h == "∅":
            return False

        # Different values means hypothesis does not cover instance
        if h != value:
            return False

    return True


# ------------------------------------------------------------
# Check whether h1 is more general than or equal to h2
# ------------------------------------------------------------
def more_general_or_equal(h1, h2):

    for a, b in zip(h1, h2):

        if a == "?":
            continue

        if a != b:
            return False

    return True


# ------------------------------------------------------------
# Minimal Generalization
# Used for a positive example
# ------------------------------------------------------------
def minimal_generalization(S, instance):

    new_S = S.copy()

    for i in range(len(S)):

        # If S is completely specific initially
        if S[i] == "∅":
            new_S[i] = instance[i]

        # If S has a different value, generalize to '?'
        elif S[i] != instance[i]:
            new_S[i] = "?"

    return new_S


# ------------------------------------------------------------
# Minimal Specializations
# Used for a negative example
# ------------------------------------------------------------
def minimal_specializations(hypothesis, instance):

    specializations = []

    for i in range(len(hypothesis)):

        # Only '?' can be specialized
        if hypothesis[i] == "?":

            for value in domains[i]:

                # Do not use the value present in
                # the negative example
                if value != instance[i]:

                    new_hypothesis = hypothesis.copy()
                    new_hypothesis[i] = value

                    specializations.append(new_hypothesis)

    return specializations


# ------------------------------------------------------------
# Print G nicely
# ------------------------------------------------------------
def print_G(G):

    if len(G) == 0:
        print("G = {}")
        return

    print("G = {")

    for hypothesis in G:
        print("     <" + ", ".join(hypothesis) + ">")

    print("}")


# ============================================================
# INITIALIZATION
# ============================================================

# Most Specific Boundary
S = ["∅", "∅", "∅", "∅"]

# Most General Boundary
G = [["?", "?", "?", "?"]]


print("=" * 60)
print("       CANDIDATE ELIMINATION ALGORITHM")
print("=" * 60)

print("\nInitial Boundaries:")
print("S = <" + ", ".join(S) + ">")
print_G(G)


# ============================================================
# PROCESS TRAINING INSTANCES
# ============================================================

for step, row in enumerate(data, start=1):

    instance = row[:4]
    target = row[4]

    print("\n" + "=" * 60)
    print(f"Processing D{step}")
    print("Instance:", row)
    print("=" * 60)

    # --------------------------------------------------------
    # POSITIVE INSTANCE
    # --------------------------------------------------------
    if target == "Yes":

        # Step 1: Generalize S to cover the positive example
        if not covers(S, instance):
            S = minimal_generalization(S, instance)

        # Step 2: Remove hypotheses from G
        # that do not cover the positive example
        new_G = []

        for g in G:
            if covers(g, instance):
                new_G.append(g)

        G = new_G

        print("\nPositive Instance (Yes)")
        print("After Generalization:")

    # --------------------------------------------------------
    # NEGATIVE INSTANCE
    # --------------------------------------------------------
    else:

        # Step 1: Specialize G to exclude the negative example
        new_G = []

        for g in G:

            # If G hypothesis covers the negative example,
            # it must be specialized
            if covers(g, instance):

                specializations = minimal_specializations(
                    g, instance
                )

                for h in specializations:

                    # Keep only hypotheses that are
                    # at least as general as S
                    if more_general_or_equal(h, S):
                        new_G.append(h)

            else:
                # If it already excludes the negative example,
                # keep it
                new_G.append(g)

        G = new_G

        print("\nNegative Instance (No)")
        print("After Specialization:")

    # --------------------------------------------------------
    # Display boundaries after each instance
    # --------------------------------------------------------

    print("\nS =", "<" + ", ".join(S) + ">")
    print_G(G)


# ============================================================
# FINAL VERSION SPACE
# ============================================================

print("\n" + "=" * 60)
print("             FINAL VERSION SPACE")
print("=" * 60)

print("\nMost Specific Boundary (S):")
print("<" + ", ".join(S) + ">")

print("\nMost General Boundary (G):")
print_G(G)

print("\n" + "=" * 60)
print("                 PROGRAM END")
print("=" * 60)
