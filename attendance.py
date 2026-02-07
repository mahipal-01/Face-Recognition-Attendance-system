import pandas as pd
from datetime import datetime

FILE = "attendance.csv"

# checking last state of attendance for a person
def get_last_state(name):
    try:
        df=pd.read_csv(FILE)
    except:
        return None

    today = datetime.now().strftime("%Y-%m-%d")
    data = df[(df.Name==name) & (df.Date==today)]
    # if it is first time, then return None
    if data.empty:
        return None

    row = data.iloc[-1]
    if row["Out"] == "" or pd.isna(row["Out"]):
        return "IN"
    else:
        return "OUT"

def mark(name):
    today = datetime.now().strftime("%Y-%m-%d")
    now = datetime.now().strftime("%H:%M:%S")

    try:
        df = pd.read_csv(FILE)
    except:
        df = pd.DataFrame(columns=["Name","Date","In","Out"])

    state = get_last_state(name)

    if state is None or state == "OUT":
        # Punch IN
        df.loc[len(df)] = [name, today, now, ""]
        action = "PUNCH IN"
    else:
        # Punch OUT
        idx = df[(df.Name==name)&(df.Date==today)].index[-1]
        df.loc[idx,"Out"] = now
        action = "PUNCH OUT"
    
    df.to_csv(FILE, index=False)
    return action
