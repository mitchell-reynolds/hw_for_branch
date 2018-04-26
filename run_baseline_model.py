import pandas as pd
import build_dataframes
import pprint

from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import accuracy_score


def baseline_model():
    """
    Creating baseline model based on simple feature extraction.

    Variables are the Number of unique: [threads, messages, sms_addresses, country_iso, geocoded_location, devices, contacts, and contacts_with_photos]

    :return:
    Prints out Logistic Regression Accuracy Score
    """

    # Set our top-level file path to find all the data, then append our loan dataframe
    origin_root = "./data/user_logs/"
    path_loan = origin_root + "user_status.csv"

    loan_df = pd.read_csv(path_loan, parse_dates=['disbursement_date'])
    loan_df['clean_user_id'] = "user-" + loan_df['user_id'].apply(str)
    dummy_loans = pd.get_dummies(loan_df['status'])
    loan_df = pd.concat([loan_df, dummy_loans], axis=1)

    call_df, contact_df, sms_df = build_dataframes.build_df()

    vars_df_sms = sms_df.groupby('user_id')[['thread_id', 'message_body', 'sms_address']].nunique().reset_index()
    vars_df_call = call_df.groupby('user_id')[['country_iso', 'geocoded_location', 'device_id']].nunique().reset_index()
    vars_df_contact = contact_df.groupby('user_id')[['display_name', 'photo_id']].nunique().reset_index()

    baseline_df = vars_df_sms.merge(vars_df_call).merge(vars_df_contact).merge(loan_df).set_index('user_id')

    pprint.pprint(baseline_df.head())

    del baseline_df['status']
    del baseline_df['defaulted']
    del baseline_df['disbursement_date']

    target = 'repaid'
    variables = baseline_df.columns[baseline_df.columns != target]

    x = baseline_df[variables]
    y = baseline_df[target]

    train_x, test_x, train_y, test_y = model_selection.train_test_split(x, y, test_size=0.33, random_state=42)

    lr = linear_model.LogisticRegression()
    lr = lr.fit(train_x, train_y)
    y_pred = lr.predict(test_x)
    acc_lr = accuracy_score(test_y, y_pred)
    print("Vanilla Logistic Regression Accuracy = %3.2f" % (acc_lr))

    return

if __name__ == "__main__":
    baseline_model()
