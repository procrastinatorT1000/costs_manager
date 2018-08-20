import re

data = "t=20180806T122000&s=240.00&fn=8712000100040824&i=16588&fp=3931869026&n=1"

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

    date_time = re.split('T', params_dict["t"])
    params_dict["Dt"] = date_time[0];
    params_dict["Tm"] = date_time[1];

    print ("Data of purchase " + params_dict["Dt"] +
    		  "\nTime of purchase " + params_dict["Tm"] +
    		  "\nSumm of purchase " + params_dict["s"] + '\n')


if __name__ == "__main__":
    parse_data(data)
    