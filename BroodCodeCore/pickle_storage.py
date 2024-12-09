import pickle
import os

path = "./BroodCodeCore/storage/pickles/"

def store_to_pickle(pickle_name: str, data):
    """Store data to a pickle

    Args:
        pickle_name (str): the name the file will be given
        data (any): The data the user wants to store
    """
    with open(f"{path}{pickle_name}.pickle", "wb") as file:
        pickle.dump(data, file)

def read_from_pickle(pickle_name: str):
    """Read the data from a specific pickle

    Args:
        pickle_name (str): The name of the pickle file to read from

    Returns:
        any: The stored data in the pickle
    """
    try:
        with open(f"{path}{pickle_name}.pickle", "rb") as file:
            data = pickle.load(file)
    except FileNotFoundError:
        print("CORE ERROR: Pickle has not been found. Did you gave up the right file name?")
        return False
    return data

def delete_pickles(pickles: list):
    """Delete a list of pickles

    Args:
        pickles (list): A list of pickle file names to delete the pickle files from
    """
    for pickle in pickles:
        if os.path.exists(f"{path}{pickle}.pickle"):
            os.remove(f"{path}{pickle}.pickle")
        else:
            print("CORE ERROR: The file does not exist")