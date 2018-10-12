import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name("imdb.json", scope)
client = gspread.authorize(creds)

sheet = client.open("movie_metadata").sheet1

data = sheet.get_all_records()

pp = pprint.PrettyPrinter()

pp.pprint(data)
