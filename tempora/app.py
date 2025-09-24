import datetime

def calculate_time_difference(main_time_str, clock_times_list):
    """
    Calculates the difference in minutes between a main clock and a list of other clocks.

    Args:
        main_time_str (str): The time of the main clock in 'HH:MM' format.
        clock_times_list (list): A list of time strings in 'HH:MM' format.

    Returns:
        list: A list of integers representing the time difference in minutes.
              Positive values mean ahead, negative values mean behind.
    """
    # Helper function to convert a time string into total minutes from midnight
    def time_to_minutes(time_str):
        t = datetime.datetime.strptime(time_str, '%H:%M')
        return t.hour * 60 + t.minute

    # Convert the Grand Clock Tower's time to minutes
    main_time_minutes = time_to_minutes(main_time_str)

    # Calculate the difference for each clock using a list comprehension
    differences = [time_to_minutes(clock_time) - main_time_minutes for clock_time in clock_times_list]
    
    return differences

# --- Simulation Data ---
grand_clock_tower = "15:00"
town_clocks = [
    "14:45",  # Clock 1
    "15:05",  # Clock 2
    "15:00",  # Clock 3
    "14:40"   # Clock 4
]

# --- Run the Simulation and Print Output ---
time_differences = calculate_time_difference(grand_clock_tower, town_clocks)

print("Tempora Clock Synchronization System")
print("====================================")
print(f"Grand Clock Tower Time: {grand_clock_tower}")
print(f"Town Clock Times: {town_clocks}")
print("------------------------------------")
print(f"Time Differences (in minutes): {time_differences} 🕒")
