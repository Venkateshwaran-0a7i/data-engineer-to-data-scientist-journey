import pandas as pd

data=pd.read_csv('Data/Profiles.csv')

def remove_duplicates(data):
    """Remove duplicate rows from the DataFrame."""
    return data.drop_duplicates()

def calculated_status_counts(data):
    unique = remove_duplicates(data)
    minimum = min(unique['Status'].value_counts())
    maximum = max(unique['Status'].value_counts())
    mean = sum(unique['Status'].value_counts()) / len(unique['Status'].value_counts())
    count = len(unique['Status'].value_counts())
    return minimum, maximum, mean, count

def main():
    min_count, max_count, mean_count, unique_status_count = calculated_status_counts(data)
    print(f"Minimum count of any status: {min_count}")
    print(f"Maximum count of any status: {max_count}")
    print(f"Mean count of statuses: {mean_count}")
    print(f"Number of unique statuses: {unique_status_count}")
    
if __name__ == "__main__":
    main()