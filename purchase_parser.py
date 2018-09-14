import re
from datetime import datetime
import table_writer

data = "t=20180806T122000&s=240.00&fn=8712000100040824&i=16588&fp=3931869026&n=1"
processed_check_info_list = []

def is_unique_data(data):
   if data in processed_check_info_list:
      print('Data: [%s] already processed' %data)
      return False
   else:
      processed_check_info_list.append(data)
      return True

def conv_split_date_time( yyyymmddThhmmss ):
   date = ""
   time = ""
   status = False

   try:
      dt = datetime.strptime( yyyymmddThhmmss, "%Y%m%dT%H%M%S" )
      print(dt)
      type(dt)

      date = dt.strftime("%d.%m.%Y")
      time = dt.strftime("%H:%M:%S")

      status = True
   except:
      print("Invalid Date-Time format: " + yyyymmddThhmmss + '\nshould be yyyymmddThhmmss')

   return  date, time, status;

def parse_data(data):

   """
   :type data: str
   """
   status = False

   if is_unique_data(data) == False:
      return status

   print("**************************************")
   print(data)

   """ Split different tags separated by '&' """
   tag_list = re.split('&', data)
   params_dict = {}

   for tag in tag_list:
      name_val = re.split('=', tag)
      params_dict[name_val[0]] = name_val[1]

   try:
      date_str, time_str, status = conv_split_date_time( params_dict["t"] )
   except:
      status = False

   if status:
      params_dict["D"] = date_str;
      params_dict["T"] = time_str;

      print ("Date of purchase " + params_dict["D"] +
           "\nTime of purchase " + params_dict["T"] +
           "\nSumm of purchase " + params_dict["s"] + '\n')

      row = [params_dict["D"], params_dict["T"], params_dict["s"]]

      try:
         book, sheet = table_writer.init_table('records.xlsx')
         table_writer.write_record(sheet, row)
         table_writer.deinit_table(book)
      except:
         print("ERROR! Writing table: Something went wrong!")

   return status

if __name__ == "__main__":
    parse_data(data)
    