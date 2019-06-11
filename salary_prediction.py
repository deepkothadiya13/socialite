import pandas as pd
data = pd.read_csv("file.csv")
print(data['income_bucket'].unique())
def label_fix(label):
    if label == '<=50k':
        return 0
    else:
        return 1
data['income_bucket'] = data ['income_bucket'].apply(label_fix)
from sklearn.model_selection import train_test_split
x_data = data.drop('income_bucket',axis=1)
y_labels = data['income_bucket']
x_train,x_test,y_train,y_test = train_test_split(x_data, y_labels, test_size= 0.3)
import tensorflow as tf
gender = tf.feature_column.categorical_column_with_vocabulary_list("gender",["female","male"])
occupation = tf.feature_column.categorical_column_with_hash_bucket("occupation", hash_bucket_size=1000)
marital_status = tf.feature_column.categorical_column_with_hash_bucket("marital_status", hash_bucket_size=1000)
relationship = tf.feature_column.categorical_column_with_hash_bucket("relationship", hash_bucket_size=1000)
education = tf.feature_column.categorical_column_with_hash_bucket("education", hash_bucket_size=1000)
workclass = tf.feature_column.categorical_column_with_hash_bucket("workclass", hash_bucket_size=1000)
native_country =tf.feature_column.categorical_column_with_hash_bucket("native_country", hash_bucket_size=1000)
age = tf.feature_column.numeric_column("age")
educction_num = tf.feature_column.numeric_column("educction_num")
capital_gain = tf.feature_column.numeric_column("capital_gain")
capital_loss = tf.feature_column.numeric_column("capital_loss")
hours_per_week = tf.feature_column.numeric_column("hours_per_week")
feat_cols =  [gender,occupation,marital_status,relationship,education,workclass,native_country,age,educction_num,capital_gain,
              capital_loss,hours_per_week]
input_func = tf.estimator.inputs.pandas_input_fn(x=x_train,y=y_train,batch_size = 100,num_epochs=3)
model =  tf.estimator.linearClassifier(feature_columns=feat_cols)
model.train(input_fn=input_func,steps=1000)
pred_fn = tf.estimator.inputs.pandas_input_fn(x=x_test,batch_size=len(x_test))
predictions = list(model.predict(input_fn= pred_fn))
final_preds = []
for pred in predictions:
    final_preds.append(pred['class_ids'][0])
from skelearn.metrics import classification_report
print(classification_report(y_test,final_preds))