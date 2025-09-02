import pandas as pd

def log_to_file(log_path, actions):
    with open(log_path, "w") as f:
        for a in actions:
            f.write(a + "\n")

def log_to_excel(log_path, actions):
    df = pd.DataFrame(actions, columns=["Action"])
    df.to_excel(log_path, index=False)
