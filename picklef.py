import pickle

with open('spn500.pickle', 'rb') as f:
    ticker = pickle.load(f)

print(ticker)