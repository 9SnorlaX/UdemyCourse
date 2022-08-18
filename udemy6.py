# Whos first

def shutdown(p1, p2):
    dist = p1.find("B") - p2.find("B")
    if dist < 0:
        print("Being first")
        return "p1"
    elif dist > 0:
        print("Being first")
        return "p2"
    else:
        return "tie"
print(shutdown("    Bang!", "  Bang!"))
