# Read all data from 'log.txt'.
# Each line represents a log message from a web server
# Write a function that returns an array with the unique IP adresses.
# Write a function that returns the GET / POST request ratio.

log_file = 'week5/log.txt'

def get_ips(log):
    with open(log_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            index = line.find("   ")
            #3 to get rid of spaces before,
            # 14 as 14 - 3 == length of IP address,
            # so it cuts off everything after IP
            print(line[index + 3:index + 14])

def get_or_post(log):
    num_post = 0
    num_get = 0
    with open(log_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "POST" in line:
                num_post += 1
            elif "GET" in line:
                num_get += 1
        gp_ratio = (num_get / num_post) #TODO round to how much?
        return gp_ratio

get_ips(log_file)
print(round(get_or_post(log_file), 2))