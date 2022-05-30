import pandas as pd
import os

dataframes = []

def main():
    #could turn this into arguments to be passed in
    path = "data/raw/cs.AI"
    path2 = "data/raw/cs.PL"
    
    #gathers the AI documents
    collect_files(path, 1)
    #gathers the PL docuemnts
    collect_files(path2, 0)
    
    #concatenates them to create a single dataframe
    df = pd.concat(dataframes, ignore_index=True)
    
    #turns the dataframe into a .csv file for use
    df.to_csv("data/longdoc.csv", index=False)
        
#takes in a folder path and the correct label we want
def add_file_to_df(file_path, label):
    with open(file_path, 'r', encoding='utf8') as f:
        contents = f.read()
        contents = contents.replace('\r', ' ').replace('\n', ' ')
        d = {"text":[contents], "labels":label}
        df = pd.DataFrame(d)
        dataframes.append(df)
        

def collect_files(path, label):
    # iterate through all files for the AI documents
    for file in os.listdir(path):
        # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = f"{path}/{file}"

            # call add file 
            add_file_to_df(file_path, label=label)


if __name__ == "__main__":
    main()