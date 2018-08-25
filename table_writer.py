# import openpyxl
from openpyxl import Workbook

# workbook
# worksheet

# def init_table(table_path = 'records.xlsx'):
#    print ('Initialize table')
#    # workbook = openpyxl.load_workbook('records.xlsx')
#    # worksheet = workbook.get_sheet_by_name("Sheet1")
#    workbook = Workbook()
#    worksheet = workbook.active

def write_record( raw_lst, empty_row_id = 1 ):

   workbook = Workbook()
   worksheet = workbook.active

   # empty_row_id = 0;
   # for row in range(1, 100):
   #    if worksheet['A'+str(row)] == worksheet['B'+str(row)] == worksheet['C'+str(row)] == None:
   #       break
   #    else:
   #       empty_row_id +=1

   # empty_row_id +=1
   print ("Saving record to records.xlsx" + str(raw_lst) + "in " + str(empty_row_id) + " raw")
   
   column_names = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   column_idx = 0;
   for cell in raw_lst:
      column = column_names[column_idx]
      worksheet[column+str(empty_row_id)] = cell;
      column_idx += 1;

   print ("Deinit table")
   workbook.save('records.xlsx')

# def deinit_table():
#    print ("Deinit table")
#    workbook.save('records.xlsx')

def test_write():
   # init_table()
   write_record([1,23,'hui', 34, '77777777777777777777777', 'bye'])
   # deinit_table()

if __name__ == '__main__':
   test_write()
