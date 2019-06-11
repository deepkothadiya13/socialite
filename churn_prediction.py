import pandas as pd
employee_data = pd.read_csv("company_sheet.csv")
print(employee_data["Year_on_Year_Increment"])

from sklearn.model_selection import train_test_split

x_data = employee_data.drop('result',axis=1)

y_labels = employee_data["Year_on_Year_Increment"]

x_train, x_test, y_train, y_test = train_test_split(x_data, y_labels, test_size=0.3)

print(x_test)

import tensorflow as tf

Comparison_with_Other_in_same_department = tf.feature_column.categorical_column_with_hash_bucket("Comparison_with_Other_in_same_department", hash_bucket_size= 50)

age = tf.feature_column.numeric_column("age")

doj = tf.feature_column.numeric_column("Doj")

Total_Absents_Per_Month = tf.feature_column.numeric_column("Total_Absents_Per_Month")

Total_Leaves_Per_Month = tf.feature_column.numeric_column("Total_Leaves_Per_Month")

No_of_minutes_spent_per_month = tf.feature_column.numeric_column("No_of_minutes_spent_per_month")

Last_Increment_Promotion = tf.feature_column.numeric_column("Last_Increment_Promotion")

Target_Achievement = tf.feature_column.numeric_column("Target_Achievement")

feat_col = [age, Total_Absents_Per_Month, Total_Leaves_Per_Month, Comparison_with_Other_in_same_department,
            No_of_minutes_spent_per_month, Last_Increment_Promotion, Target_Achievement]

input_func = tf.estimator.inputs.pandas_input_fn(x= x_train, y= y_train, batch_size = 10, num_epochs = 10, shuffle = True)

print(input_func)

model = tf.estimator.LinearClassifier(feature_columns = feat_col)

model.train(input_fn=input_func,steps=5)

pred_fn = tf.estimator.inputs.pandas_input_fn(x=x_test,batch_size = len(x_test),shuffle = False)

predictions = list(model.predict(input_fn=pred_fn))

print(len(predictions))

final_preds = []

for pred in predictions:
    final_preds.append(pred['class_ids'][0])

print("final prediction",final_preds)

from sklearn.metrics import classification_report

print(classification_report(y_test,final_preds))











