def get_data_list(file_name):
	data_file = open(file_name, "r")
	data_list = []
	for line_str in data_file:
		data_list.append(line_str.strip().split(','))
	return data_list

def get_monthly_averages(data_list):
	avg_list = []
	current_month = data_list[1][0][0:7]
	avg_top = 0
	avg_bottom = 0
	for line in data_list[1:]:
		if line[0][0:7] == current_month:
			avg_top += int(line[5]) * float(line[6])
			avg_bottom += int(line[5])
		else:
			avg_list.append((float(avg_top/avg_bottom),current_month))
			current_month = line[0][0:7]
			avg_top += int(line[5]) * float(line[6])
			avg_bottom += int(line[5])
	return avg_list

def print_info(avg_list):
	avg_list.sort()
	print("Six best months")
	print("Price{:>10}".format("Month"))
	for item in avg_list[0:5]:
		print("{:.2f}{:>10s}".format(item[0], item[1]))
		
	avg_list.reverse()
	print("\nSix worst months")
	print("Price{:>10}".format("Month"))
	for item in avg_list[0:5]:
		print("{:.2f}{:>10s}".format(item[0], item[1]))
	
def main():
	data_list = get_data_list("GOOG.csv")
	avg_list = get_monthly_averages(data_list)
	print_info(avg_list)

main()
