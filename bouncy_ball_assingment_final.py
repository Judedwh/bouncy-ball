"""
PHYS20161 1st assignment: Bouncy Ball

Given user input for what space object they are on, initial height, minimum
height
of interest and 'bounce efficiency' this program returns the number of bounces
over the minimum height and how many seconds it takes to complete the bounces.
The program also validates user inputs to ensure they work in the code. An
additional validation of the inital height being in line with the mgh
approximation is also included


JUDE WASDELL HARRIS 11/10/22

"""
import math

SPACE_BODY_DATA = [["SUN", 274.1, 695508000], ["MERCURY", 3.7, 2439000],
                   ["VENUS", 8.9, 6052000], ["EARTH", 9.8, 6371000],
                   ["MOON", 1.6, 1737000], ["MARS", 3.7, 3389000],
                   ["CERES", 0.3, 469000], ["JUPITER", 25.9, 69911000],
                   ["SATURN", 11.2, 58232000], ["URANUS", 9.0, 25362000],
                   ["NEPTUNE", 11.3, 24622000], ["PLUTO", 0.61, 1188000]]


def choose_space_body():
    """
    Asks user to pick from a list which space body the ball will be dropped
    on and returns the respective value of g.

    Returns
    -------
    chosen_space_body_g: float
        value of g for the respective space body

    """
    chosen_space_body_input = input(
        "Please enter, from the above options, the space object the ball is being"
        " dropped on: ").upper()
    for i, _ in enumerate(SPACE_BODY_DATA):
        if chosen_space_body_input == SPACE_BODY_DATA[i][0]:

            return SPACE_BODY_DATA[i][1], SPACE_BODY_DATA[i][2]
    print("Invalid space object, please enter from the options above")

    return choose_space_body()


def get_positive_initial_height(chosen_space_body_r):
    """
    Asks user for initial height, h_0, (in metres) validates the input as well
    has ensuring h_0 is within the condition h_0<<R such that mgh approximation
    is valid. This also ensures that issues due to maximum recursion errors do
    happen.

    h_0 > 0.026 * R_i is based off the value of g at h_0 being within 5% of g
    value at the surface of the space object.
    Parameters
    ----------
    chosen_space_body_r : float
        radius of chosen space body

    Returns
    -------
   initial_height_input : float
       initial height ball dropped from
    """

    while True:
        try:
            initial_height_input = float(input(
                "Please enter the initial height that the bouncy ball is being"
                " dropped from in metres: "))
        except ValueError:
            print("Please enter a valid height")
            continue
        if initial_height_input < 0:
            print("Please enter a non negative height")
            continue
        if initial_height_input == 0:
            print(
                "Your bouncy ball will not be very interesting then... please"
                " enter a height greater than 0")
            continue
        if initial_height_input > 0.026 * chosen_space_body_r:
            print(
                "Please enter an initial height that is in line with the mgh "
                "approximation")
        else:
            break
    return initial_height_input


def get_positive_minimum_height(initial_height):
    """
    Asks user for minimum height of interest that the ball must bounce above
    for a bounce to be counted. Validating the input h_min is less than the
    input h_0.

    Parameters
    ----------
    initial_height_string : float
        initial height ball dropped from set by user input

    Returns
    -------
    minimum_height_input : float
        minimum height ball is to bounce above for bounce to be counted

    """

    while True:
        try:
            minimum_height_input = float(input(
                "Please enter the minimum height in metres that the bouncy ball"
                " must bounce above for a bounce to be counted: "))

        except ValueError:
            print("Please enter a valid height")
            continue
        if minimum_height_input >= initial_height:
            print("Please enter a height less than the initial height")
            continue
        if minimum_height_input == 0:
            print(
                "Your bouncy ball will not be very interesting then... please"
                " enter a height greater than 0")
        else:
            break
    return minimum_height_input


def get_energy_efficiiency():
    """
    Asks user for energy efficiency validates the input as well as ensuring the
    value is between 0 and 1.

    Returns
    -------
    bounce_energy_efficiency_input : float
       efficiency of bounce between 0 and 1
    """
    while True:
        try:
            bounce_energy_efficiency_input = float(
                input("Please enter the energy efficiency, n, of your bounces"
                      " (0 < n < 1): "))
        except ValueError:
            print("Please enter a valid efficiency")
            continue
        if not 0 < bounce_energy_efficiency_input < 1:
            print("Please enter an efficiency between 0 and 1")
        else:
            break
    return bounce_energy_efficiency_input


def number_of_bounces_counter(initial_height, minimum_height, efficiency):
    """
    Given user inputs for initial height, minimum height and efficiency
    counts the number of bounces above minimum height.

    Parameters
    ----------
    initial_height : float
        height ball is dropped from input by user
    minimum_height : float
        height ball must bounce above for bounce to be counted input by user
    efficiency : float
        energy efficiency of the bounce input by user

    Returns
    -------
    number_of_bounces: int
        number of bounces above the minimum height.

    """
    height_following_bounce = initial_height
    count = 0
    while height_following_bounce > minimum_height:
        count += 1
        height_following_bounce = initial_height * efficiency ** count
    bounces = count - 1
    return bounces


def time_taken(initial_height, efficiency, chosen_space_body_g, number_of_bounces):
    """
    Given user inputs for initial_height, efficiency, acceleration and bounces
    calcualted previsouly the total time taken to complete bounces is
    calculated

    Parameters
    ----------
    initial_height : float
        height ball is dropped from input by user.
    efficiency : float
        height ball must bounce above for bounce to be counted input by user.
    chosen_space_body_g : float
        value of g on chosen space body.
    number_of_bounces : int
        number of bounces above minimum height

    Returns
    -------
    total_time : float
        total time for all counted bounces to be completed

    """
    total_time = math.sqrt(2 * (initial_height/chosen_space_body_g))
    for i in range(number_of_bounces):
        height_following_bounce = initial_height * efficiency ** (i + 1)
        total_time += 2 * \
            math.sqrt(2*(height_following_bounce/chosen_space_body_g))
    return total_time


def main():
    """
    Runs whole program as well as asking user if they wish to run again

    Returns
    -------
    String with bounces and total time as above

    """
    for value in SPACE_BODY_DATA:
        print('{0}          (g = {1} ms^-2)'.format(value[0], value[1]))
    chosen_space_body_g, chosen_space_body_r = choose_space_body()
    initial_height = get_positive_initial_height(chosen_space_body_r)
    minimum_height = get_positive_minimum_height(initial_height)
    efficiency = get_energy_efficiiency()
    bounces = number_of_bounces_counter(
        initial_height, minimum_height, efficiency)
    total_time = time_taken(initial_height, efficiency,
                            chosen_space_body_g, bounces)
    if bounces > 0:
        print("The ball does {0} bounces above the minimum height in {1:.2f} "
              "seconds".format(
                  bounces, total_time))
    else:
        print("The ball does {0} bounces above the minimum height but reaches "
              "the ground in {1:.2f} seconds".format(
                  bounces, total_time))

    drop_again_loop = True
    while drop_again_loop:
        try:
            drop_again = str(input(
                "Would you like to drop another ball? (YES/NO): ").upper())
        except ValueError:
            print("Please enter 'YES' or 'NO'")

        if drop_again == ("YES"):
            main()

        elif drop_again == ("NO"):
            print("Thank you, have a nice day. ")
            drop_again_loop = False
        else:
            print("Please enter 'YES' or 'NO")


if __name__ == "__main__":
    main()
