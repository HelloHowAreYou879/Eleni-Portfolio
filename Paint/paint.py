# Constants assigned at the top for readability (easier to read) and to prevent the value being changed accidently later on
METRE_PER_LITRE = 5
DOOR_AREA = 2.5
LABOUR_COST_PER_METRE = 5

COST_5LIT_TIN = 50
COST_3LIT_TIN = 35
COST_2LIT_TIN = 25
COST_1LIT_TIN = 15

# Validate number of walls
def validate_wall_count(n_walls):
    while n_walls <= 0 or n_walls > 20:
        print("Invalid data, number of walls must be 1 to 20.")
        n_walls = int(input("Enter number of walls: "))
    return n_walls

# Calculate paintable area for a wall
def calculate_paint_area(length, width, door_exists, win_length, win_width):
    wall_area = length * width
    if door_exists.lower() == "yes":
         door_area = DOOR_AREA
    else:
        door_area = 0

    window_area = win_length * win_width
    paint_area = wall_area - door_area - window_area
    return paint_area

# Calculate total paint cost and return it
def calculate_paint_cost(litres_required):
    num_five_litre = litres_required // 5
    remainder = litres_required % 5

    num_three_litre = remainder // 3
    remainder = remainder % 3

    num_two_litre = remainder // 2
    num_one_litre = remainder % 2

#calculate the total cost of tins
    print("Paint tins breakdown:")
    print("  5L tins:", num_five_litre)
    print("  3L tins:", num_three_litre)
    print("  2L tins:", num_two_litre)
    print("  1L tins:", num_one_litre)

    paint_cost = (
        num_five_litre * COST_5LIT_TIN +
        num_three_litre * COST_3LIT_TIN +
        num_two_litre * COST_2LIT_TIN +
        num_one_litre * COST_1LIT_TIN
    )
    return paint_cost

# Main program
def main():
    num_walls = int(input("Enter number of walls: "))
    number_walls = validate_wall_count(num_walls)

    total_paint_area = 0

    for i in range(1, number_walls + 1):
        print(f"\nWall {i}:")
        len_wall = float(input("  Enter length of the wall: "))
        wid_wall = float(input("  Enter width of the wall: "))
        door_exist = input("  Is there a door for this wall (Yes/No): ")
        len_win = float(input("  Enter length of the window: "))
        wid_win = float(input("  Enter width of the window: "))

#def paint area
        wall_paint_area = calculate_paint_area(len_wall, wid_wall, door_exist, len_win, wid_win)
        total_paint_area += wall_paint_area

    print(f"\nTotal paintable area: {total_paint_area:.2f} m²")

    litres_required = int(total_paint_area / METRE_PER_LITRE)
    print("Litres of paint required:", litres_required)

    paint_cost = calculate_paint_cost(litres_required)
    print(f"Total cost of paint: ${paint_cost}")

    labour_cost = total_paint_area * LABOUR_COST_PER_METRE
    print(f"Labour cost: ${labour_cost:.2f}")

    total_cost = paint_cost + labour_cost
    print(f"\nTotal cost (paint + labour): ${total_cost:.2f}")

# Run the program
if __name__ == "__main__":
    main()


