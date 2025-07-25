from etl.extract import extract_from_file
from etl.transform import transform_data
from etl.load import load_to_mysql

def main():
    while True:
        print("\n   Chicken ETL Menu   ")
        print("1. Extract Data")
        print("2. Transform Data")
        print("3. Load Data to MySQL")
        print("5. Exit")
        
        choosen_option = input("Choose an option: ")
        
        if choosen_option == "1":
            data = extract_from_file("chicken_database.csv")
            print("Extracted" + len(data) + "records.")
        elif choosen_option == "2":
           data = extract_from_file("chicken_database.csv") 
           transformData = transform_data(data)
           print(len(data) + "transformed.")
        elif choosen_option == "3":
            data = extract_from_file("chicken_database.csv")
            transformData = transform_data(data)
            load_to_mysql(transformData)
        elif choosen_option == "4":
            break
            
        else:
            print("Invalid option.")
        
if __name__ == "__main__":
    main()
    