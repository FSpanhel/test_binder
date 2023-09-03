from datetime import datetime

today = datetime.now().strftime("%Y_%m_%d")  # noqa

save_csv = True
path_csv = "/home/spa0001f/github/teach/dsc/data/_create/csv"
format_ = "zip"

# path_load_csv = "/home/spa0001f/github/teach/dsc/data/_create/csv/2022_10_06"  # data is only loaded if load_data is set to True in the notebook!  # noqa
path_load_csv = "/home/spa0001f/github/teach/dsc/data/_create/csv/2022_10_11"

save_csv_public = True
# csv_public_date = '2022_10_11' obsolete
path_csv_public = "/home/spa0001f/github/teach/dsc/data/csv"
