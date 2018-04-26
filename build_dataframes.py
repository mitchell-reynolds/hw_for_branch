import os
import pandas as pd
from pprint import pprint


def build_df():
    """
    Once the files have been unzipped, let's build some dataframes from the three types of data we have:
    IE phone calls, contacts, and text messages

    :return:
    Three pandas.DataFrames [calls, contacts, sms]
    """

    # Set our top-level file path to find all the data
    origin_root = "./data/user_logs/"

    # Create multiple lists so we can concat later
    call_list = list()
    contact_list = list()
    sms_list = list()

    # TODO: research about writing on the fly when unzipping the files
    for root, dirs, files in os.walk(origin_root):
        for file in files:
            if file.endswith("collated_call_log.txt"):
                user_and_device = str(root[18:])
                user_id, device_id = user_and_device.split("/")[
                    0
                ], user_and_device.split(
                    "/"
                )[
                    1
                ]
                tmp_txt = os.path.join(root, file)
                temp_df = pd.read_json(tmp_txt)
                temp_df["user_id"] = user_id
                temp_df["device_id"] = device_id
                call_list.append(temp_df)
            elif file.endswith("collated_contact_list.txt"):
                user_and_device = str(root[18:])
                user_id, device_id = user_and_device.split("/")[
                    0
                ], user_and_device.split(
                    "/"
                )[
                    1
                ]
                tmp_txt = os.path.join(root, file)
                temp_df = pd.read_json(tmp_txt)
                temp_df["user_id"] = user_id
                temp_df["device_id"] = device_id
                contact_list.append(temp_df)
            elif file.endswith("collated_sms_log.txt"):
                user_and_device = str(root[18:])
                user_id, device_id = user_and_device.split("/")[
                    0
                ], user_and_device.split(
                    "/"
                )[
                    1
                ]
                tmp_txt = os.path.join(root, file)
                temp_df = pd.read_json(tmp_txt)
                temp_df["user_id"] = user_id
                temp_df["device_id"] = device_id
                sms_list.append(temp_df)

    # Combine the respective data in their own groupings
    call_df = pd.concat(call_list, axis=0)
    contact_df = pd.concat(contact_list, axis=0)
    sms_df = pd.concat(sms_list, axis=0)

    # Throwing an error?
    # pprint(call_df.info(), contact_df.info(), sms_df.info())

    return call_df, contact_df, sms_df


if __name__ == "__main__":
    build_df()
