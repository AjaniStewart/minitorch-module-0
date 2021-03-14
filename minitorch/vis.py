from project.datasets import Simple, Split, Xor

N = 100


def classify_simple(pt):
    """Classify based on x position"""
    if pt[0] > 0.5:
        return 1.0
    else:
        return 0.0


def classify_split(pt):
    """Classify based on x position"""
    if pt[0] < 0.3 or pt[0] > 0.78:
        return 1.0
    else:
        return 0.0


def classify_xor(pt):
    """Classify based on x position"""
    if (pt[0] < 0.5 and pt[1] > 0.5) or (pt[0] > 0.5 and pt[1] < 0.5):
        return 1.0
    else:
        return 0.0


# Split(N, vis=True).graph("initial", model=classify_split)
# Simple(N, vis=True).graph("initial", model=classify_simple)
# Xor(N, vis=True).graph("initial", model=classify_xor)
