import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']


credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
gc = gspread.authorize(credentials)

gsheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1sx01sSnfVqaSRSZBpeudEif5tpztxGjkJta3GzLGza4/')

spreadsheets = [spreadsheet.get_all_values() for spreadsheet in gsheet.worksheets()]
headers = [data.pop(0) for data in spreadsheets]
data = [pd.DataFrame(spreadsheets[i], columns = headers[i]) for i in range(0,len(spreadsheets))]

print(data)
