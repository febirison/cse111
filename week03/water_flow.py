# Prove Milestone: Water Pressure assignment by Anderson Okai

def water_column_height(tower_height, tank_height):
    """Calculate and return the height of the water column.

    Parameters:
        tower_height: height of the tower in meters
        tank_height: height of the walls of the tank in meters
    Return:
        height of the water column in meters
    """
    return tower_height + (3/4) * tank_height

def pressure_gain_from_water_height(height):
    """Calculate and return the pressure caused by Earth's gravity on the water.

    Parameters:
        height: height of the water column in meters
    Return:
        pressure in kilopascals
    """
    water_density = 998.2  # kg/m^3
    gravity = 9.80665  # m/s^2
    pressure = (water_density * gravity * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculate and return the water pressure lost due to friction in a pipe.

    Parameters:
        pipe_diameter: diameter of the pipe in meters
        pipe_length: length of the pipe in meters
        friction_factor: friction factor of the pipe
        fluid_velocity: velocity of the water in meters/second
    Return:
        lost pressure in kilopascals
    """
    water_density = 998.2  # kg/m^3
    pressure_loss = -friction_factor * (pipe_length / pipe_diameter) * (water_density * fluid_velocity**2 / 2000)
    return pressure_loss
