def normalizeData(arr):
	return (arr - arr.min()) / (arr.max() - arr.min())

def normalize(arr, i):
	return (i - arr.min()) / (arr.max() - arr.min())

def denormalize(arr, i):
	return i * (arr.max() - arr.min()) + arr.min()