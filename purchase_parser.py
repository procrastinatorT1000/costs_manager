import re
from datetime import datetime
import table_writer

data = "t=20180806T122000&s=240.00&fn=8712000100040824&i=16588&fp=3931869026&n=1"

def conv_split_date_time( yyyymmddThhmmss ):
   date = ""
   time = ""

   dt = datetime.strptime( yyyymmddThhmmss, "%Y%m%dT%H%M%S" )
   print(dt)
   type(dt)

   date = dt.strftime("%d.%m.%Y")
   time = dt.strftime("%H:%M:%S")

   return  date, time;

def parse_data(data):

   """
   :type data: str
   """
   print("**************************************")
   print(data)

   params_arr = re.split('&', data)
   params_dict = {}

   for param in params_arr:
      param_arr = re.split('=', param)
      params_dict[param_arr[0]] = param_arr[1]

   date_str, time_str = conv_split_date_time( params_dict["t"] )

   params_dict["D"] = date_str;
   params_dict["T"] = time_str;

   print ("Date of purchase " + params_dict["D"] +
        "\nTime of purchase " + params_dict["T"] +
        "\nSumm of purchase " + params_dict["s"] + '\n')

   raw = [params_dict["D"], params_dict["T"], params_dict["s"]]

   book, sheet = table_writer.init_table('records.xlsx')
   table_writer.write_record(sheet, raw)
   table_writer.deinit_table(book)


if __name__ == "__main__":
    parse_data(data)
    