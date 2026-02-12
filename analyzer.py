def tag_traffic(data):
    tagged_data = [line + ['LARGE'] if int(line[5]) > 5000
         else line + ['NORMAL'] for line in data]
    return tagged_data
