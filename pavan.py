import json




# Input data
clean_ecg_str = "[-7.987,-7.715,-7.353,-7.179,-7.144,-7.015,-7.765,-9.631,-12.096,-15.41,-18.511,-20.458,-22.389,-25.371,-27.607,-27.275,-26.779,-26.845,-22.532,-6.799,19.184,43.641,61.8]"
timestamps_str = "[1748841962916,1748841962917,1748841963081,1748841963081,1748841963082,1748841963085,1748841963086,1748841963087,1748841963088,1748841963089,1748841963089,1748841963090,1748841963091,1748841963092,1748841963093,1748841963094,1748841963094,1748841963097,1748841963108,1748841963108,1748841963115,1748841963130,1748841963131,1748841963164,174884196]"

# Convert strings to lists
clean_ecg = json.loads(clean_ecg_str)
timestamps = json.loads(timestamps_str)

# Find the index of the desired value
target_value = -25.371
if target_value in clean_ecg:
    index = clean_ecg.index(target_value)
    if index < len(timestamps):
        corresponding_time = timestamps[index]
        print(f"e: {target_value}, time: {corresponding_time}")
    else:
        print("Timestamp for this ECG value is missing or misaligned.")
else:
    print("ECG value not found.")
