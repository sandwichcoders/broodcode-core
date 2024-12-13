import pickle
from pickle import load, dump
from os import path, remove, makedirs

pickle_path = "./BroodCodeCore/storage/pickles/"

def store_to_pickle(pickle_name: str, data):
    """Store data to a pickle

    Args:
        pickle_name (str): the name the file will be given
        data (any): The data the user wants to store
    """
    if not path.exists(path.join(pickle_path, 'test.pickle')):
        makedirs("storage/pickles") # TEST THIS LATER

    with open(f"{pickle_path}{pickle_name}.pickle", "wb") as file:
        dump(data, file)

def read_from_pickle(pickle_name: str):
    """Read the data from a specific pickle

    Args:
        pickle_name (str): The name of the pickle file to read from

    Returns:
        any: The stored data in the pickle
    """
    try:
        with open(f"{pickle_path}{pickle_name}.pickle", "rb") as file:
            data = load(file)
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
        if path.exists(f"{pickle_path}{pickle}.pickle"):
            remove(f"{pickle_path}{pickle}.pickle")
        else:
            print("CORE ERROR: The file does not exist")