import numpy as np
import torchvision
from tqdm.notebook import trange

from model.augment import fonts, ImageGenerator
from model.helpers import transform_white_on_black, transform_black_on_white

class BatchGenerator:
    def __init__(self, batch_size=256, batches_per_epoch=300):
        self.batch_size = batch_size
        self.batches_per_epoch = batches_per_epoch
        
        self.augmenter = ImageGenerator(fonts)
        
        self.train_X, self.train_y = self.give_dataset(train=True, augment=20000)
        self.test_X, self.test_y = self.give_dataset(train=False, augment=3000)
        
        
    def give_dataset(self, train=True, augment=10000):
        dataset = torchvision.datasets.MNIST('./MNIST/', download=True, train=train)
        X, y = zip(*[
            (np.array(x).reshape(-1, 28, 28), y)
            if y != 0 else (self._make_random_noise(), y)
            for x, y in dataset])
        X, y = np.array(X), np.array(y)
        X = transform_white_on_black(X)
        
        augmented_X, augmented_y = self.augmenter.generate(augment)
        augmented_X = transform_black_on_white(augmented_X)

        X = np.concatenate((X, augmented_X), axis=0)
        y = np.concatenate((y, augmented_y), axis=0)
        return X, y
    
    def _make_random_noise(self):
        max_val = np.random.randint(1, 100)
        min_val = np.random.randint(0, max_val)
        return np.random.randint(min_val, high=max_val, size=(1, 28, 28))

    def __iter__(self):
        for _ in trange(self.batches_per_epoch, leave=False):
            batch = np.random.randint(0, len(self.train_X), self.batch_size)
            x_batch = self.train_X[batch]
            y_batch = self.train_y[batch]
            yield x_batch, y_batch
