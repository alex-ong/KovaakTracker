import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
from util import modulePath
from os.path import join
from task import Task
import time
from fileinfo import latest_file, num_files

# sheet == worksheet
# spreadsheets are composed of sheets
scope = ["https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",]

credentials = ServiceAccountCredentials.from_json_keyfile_name(join(modulePath(), "authentication.json"), scope)
gc = gspread.authorize(credentials)


def refresh_credentials():
    global gc
    gc = gspread.authorize(credentials)


def safe_get_sheet(spreadsheet_id, sheet_id, first=True):
    global gc
    try:
        ss = gc.open_by_key(spreadsheet_id)
        result = ss.worksheet(sheet_id)
        return result
    except gspread.exceptions.APIError:
        if not first:
            raise
        else:
            refresh_credentials()
            return safe_get_sheet(spreadsheet_id, sheet_id, False)


def getLeagueInfo():
    sheetID = None
    with open(join(modulePath(), "sheetinfo.json")) as f:
        data = json.load(f)
        spreadsheetID = data["spreadsheetID"]
        sheetID = data["sheetName"]
        tasks = data["tasks"]

    return (spreadsheetID, sheetID, tasks)


def loadLeagueData():
    spreadsheetID, sheetID, tasks = getLeagueInfo()
    sheet = safe_get_sheet(spreadsheetID, sheetID)
    data = sheet.range(1,1,sheet.row_count + 1,sheet.col_count + 1)
    data = SplitDatabaseRows(data)
    return (sheet, data, tasks)

def SplitDatabaseRows(fullData):
    if len(fullData) == 0:
        return []
    currentRowIdx = None
    currentRow = []
    result = []
    for item in fullData:
        if item.row != currentRowIdx:
            if currentRowIdx is not None:
                result.append(currentRow)
            currentRow = [item]
            currentRowIdx = item.row
        else:
            currentRow.append(item)
    if len(currentRow) > 0:
        result.append(currentRow)

    return result

def find_latest_session(data):
    headerOffset = 1
    for rowNum, row in enumerate(data):
        if rowNum < headerOffset:
            continue        
        if row[0].value != '' and row[1].value == '':
            return row[0].row - 1
    return None

def update_cell(worksheet, cell, value):
    cell.value = value
    worksheet.update_cells([cell])

def main():
    worksheet, data, tasks = loadLeagueData()
    sessionRow = find_latest_session(data)

    if sessionRow is None:
        print("Couldn't find current session")
        return
    
    task_data = {}
    for i, task in enumerate(tasks):
        task_data[task] = Task(task,1+i*2)
        
    for task in task_data.values():
        print(task)

    current_file_count = num_files()
    while True:
        file_count = num_files()
        if file_count == current_file_count:
            continue
        
        latest = latest_file()
        current_file_count = file_count
        print("Got new file:", latest)
        

        

if __name__ == "__main__":
    # simple test
    main()
