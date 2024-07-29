from datetime import datetime, timedelta

# Sample weather data
weather_data = [
    {'date': '2023-08-01', 'max_temp': 32, 'min_temp': 24, 'humidity': 60},
    {'date': '2023-08-02', 'max_temp': 30, 'min_temp': 22, 'humidity': 65},
    {'date': '2024-07-10', 'max_temp': 29, 'min_temp': 21, 'humidity': 55}
]

def find_extreme_temperatures(data):
    #Find the highest and lowest temperatures recorded during the period.
    max_temp = float('-inf')
    min_temp = float('inf')
    
    for entry in data:
        if entry['max_temp'] > max_temp:
            max_temp = entry['max_temp']
        if entry['min_temp'] < min_temp:
            min_temp = entry['min_temp']
    
    return max_temp, min_temp

def count_days_above_30(data):
    #Determine the number of days with temperatures above 30°C.
    count = 0
    for entry in data:
        if entry['max_temp'] > 30:
            count += 1
    return count

def average_humidity(data):
    #Compute the average humidity over the specified period.
    total_humidity = 0
    for entry in data:
        total_humidity += entry['humidity']
    
    return total_humidity / len(data) if data else 0

# Example usage
if __name__ == "__main__":
    # Compute the highest and lowest temperatures
    highest_temp, lowest_temp = find_extreme_temperatures(weather_data)
    print("Highest Temperature:", highest_temp,"°C")
    print(f"Lowest Temperature: {lowest_temp}°C")
    
    # Count the number of days with temperatures above 30°C
    days_above_30 = count_days_above_30(weather_data)
    print(f"Number of Days Above 30°C: {days_above_30}")
    
    # Compute the average humidity
    avg_humidity = average_humidity(weather_data)
    print(f"Average Humidity: {avg_humidity}%")  

