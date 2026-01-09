"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can a ghost be eaten?
    """
    if type(power_pellet_active) is not bool or type(touching_ghost) is not bool:
        raise TypeError("Inputs must be boolean")
    
    can_eat_ghost = power_pellet_active and touching_ghost

    return can_eat_ghost


def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?
    """
    if type(touching_power_pellet) is not bool or type(touching_dot) is not bool:
        raise TypeError("Inputs must be boolean")
    
    has_scored = touching_power_pellet or touching_dot

    return has_scored


def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """
    
    if type(power_pellet_active) is not bool or type(touching_ghost) is not bool:
        raise TypeError("Inputs must be boolean")
    
    game_over = not power_pellet_active and touching_ghost

    return game_over


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """

    
    if type(has_eaten_all_dots) is not bool or type(power_pellet_active) is not bool or type(touching_ghost) is not bool:
        raise TypeError("Inputs must be boolean")
    
    victory = has_eaten_all_dots and (not touching_ghost or power_pellet_active)
    
    return victory