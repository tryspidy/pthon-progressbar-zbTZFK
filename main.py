from tqdm import tqdm, trange

with tqdm(total = 100) as progressbar:
    for i in range(10):
        # Here your function to calculation
        progressbar.update(10)