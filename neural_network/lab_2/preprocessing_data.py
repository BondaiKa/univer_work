import pandas as pd
import tensorflow as tf

def preprocessing_data(path:str,ex_columns:list,target_col:str):
    """Prepare data to train"""
    melbourne_data= pd.read_csv(path) 
    melbourne_data = melbourne_data.drop(columns=ex_columns)
    target_column = melbourne_data.pop(target_col)
    melbourne_data['Suburb']=melbourne_data['Suburb'].str.lower()
    melbourne_data['Regionname']=melbourne_data['Regionname'].str.lower()
    numeric_features = melbourne_data.dtypes[melbourne_data.dtypes != 'object'].index
    melbourne_data[numeric_features] = melbourne_data[numeric_features].apply(
        lambda x: (x - x.mean()) / (x.std()))
    melbourne_data[numeric_features] = melbourne_data[numeric_features].fillna(-1)
    melbourne_data = pd.get_dummies(melbourne_data, dummy_na=True)
    melbourne_data[target_col]=target_column
    return melbourne_data

def split_dataset(pd_data, batch_size=1)->tuple:
    """shuffle and split pandas frame to train and test dataset"""
    melbourne_data = pd_data.copy()
    melbourne_data = melbourne_data.sample(frac=1)   
    train = melbourne_data.sample(frac=0.8,random_state=200)
    target_train = train.pop('Price')
    
    validation = melbourne_data.drop(train.index)
    target_val = validation.pop('Price')

    train_dataset = tf.data.Dataset.from_tensor_slices((train.values, target_train.values)).batch(batch_size)
    val_dataset = tf.data.Dataset.from_tensor_slices((validation.values, target_val.values)).batch(batch_size)
    return train_dataset, val_dataset