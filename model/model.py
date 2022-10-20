import torch
from torch import nn
import torch.optim as optim


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        
        p = 0.2
        
        self.conv1 = nn.Conv2d(1, 10, kernel_size=3)
        self.maxpool1 = nn.MaxPool2d(3, stride=2, padding=1)
        self.dropout1 = nn.Dropout2d(p=p)
        self.activation1 = nn.LeakyReLU()
        
        self.conv2 = nn.Conv2d(10, 20, kernel_size=3)
        self.maxpool2 = nn.MaxPool2d(3, stride=2, padding=1)
        self.dropout2 = nn.Dropout2d(p=p)
        self.activation2 = nn.LeakyReLU()
        
        self.conv3 = nn.Conv2d(20, 30, kernel_size=3)
        self.maxpool3 = nn.MaxPool2d(3, stride=2, padding=1)
        self.dropout3 = nn.Dropout2d(p=p)
        self.activation3 = nn.LeakyReLU()
        
        self.conv2_drop = nn.Dropout2d()
        self.flatten = nn.Flatten()
        self.fc4 = nn.Linear(120, 50)
        self.dropout4 = nn.Dropout(p=p)
        self.activation4 = nn.LeakyReLU()
        
        self.fc5 = nn.Linear(50, 10)
        self.optimizer = optim.Adam(self.parameters())
        self.loss_func = nn.CrossEntropyLoss()

    def forward(self, x, training=True):
        x = self.conv1(x)
        x = self.maxpool1(x)
        if training:
            x = self.dropout1(x)
        x = self.activation1(x)

        x = self.conv2(x)
        x = self.maxpool2(x)
        if training:
            x = self.dropout2(x)
        x = self.activation2(x)
        
        x = self.conv3(x)
        x = self.maxpool3(x)
        if training:
            x = self.dropout3(x)
        x = self.activation3(x)
    
        x = self.flatten(x)
        x = self.fc4(x)
        if training:
            x = self.dropout4(x)
        x = self.activation4(x)
        
        x = self.fc5(x)
        return x
    
    def predict(self, x):
        x = torch.Tensor(x)
        with torch.no_grad():
            return self.forward(x, training=False).numpy().argmax(axis=1)
        
    def predict_one(self, x):
        x = x.reshape(-1, 1, 28, 28)
        return self.predict(x)[0]

    def train_on_batch(self, x, y):
        self.optimizer.zero_grad()
        
        x = torch.Tensor(x)
        y = torch.Tensor(y).long()
        
        pred = self.forward(x)
        loss = self.loss_func(pred, y)
        loss.backward()
        self.optimizer.step()
        return loss
    
model = Model()