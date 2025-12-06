import pandas as pd
import os

csv_path="sales.csv"
if not os.path.exists(csv_path) :
    data=[
        {"date":"2025-12-01","product":"camisa","quantity":50,"price":70},
        {"date":"2025-12-01","product":"calça","quantity":4,"price":200},
        {"date":"2025-12-01","product":"chapeu","quantity":7,"price":150},
        {"date":"2025-12-01","product":"vestido","quantity":56,"price":55},
        {"date":"2025-12-01","product":"saia","quantity":70,"price":45},
        {"date":"2025-12-01","product":"sapato" ,"quantity":100,"price":450},
        {"date":"2025-12-01","product":"cachecol", "quantity":10,"price":48},
        {"date":"2025-12-01","product":"tenis", "quantity":60,"price":560},
        {"date":"2025-12-01","product":"moletom", "quantity":85,"price":250}
         
         ]
    df_exemplo = pd.DataFrame(data)
    df_exemplo.to_csv(csv_path,index=False)
    print("uhul criou!",csv_path)

df=pd.read_csv(csv_path,parse_dates=["date"])

required={"date","product","price","quantity"}
if not required.issubset(set(df.columns)):
    print("as colunas estão esrradas meu chapa!")

df["total"]=df["price"]*df["quantity"]
df[["total"]].to_csv("total.csv",index=False)
print("uhuuu funcionou de novo!")

