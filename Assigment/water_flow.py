# Prove Milestone: Water Pressure assignment by Anderson Okai

# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.80665
WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016

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
    pressure = (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000
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
    pressure_loss = -friction_factor * (pipe_length / pipe_diameter) * (WATER_DENSITY * fluid_velocity**2 / 2000)
    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calculate and return the water pressure lost due to fittings in a pipe.

    Parameters:
        fluid_velocity: velocity of the water in meters/second
        quantity_fittings: number of fittings in the pipe
    Return:
        lost pressure in kilopascals
    """
    pressure_loss = -0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings / 2000
    return pressure_loss

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculate and return the Reynolds number for a pipe with water flowing through it.

    Parameters:
        hydraulic_diameter: diameter of the pipe in meters
        fluid_velocity: velocity of the water in meters/second
    Return:
        Reynolds number (unitless)
    """
    reynolds = (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY
    return reynolds

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Calculate and return the water pressure lost due to reduction in pipe diameter.

    Parameters:
        larger_diameter: diameter of the larger pipe in meters
        fluid_velocity: velocity of the water in meters/second
        reynolds_number: Reynolds number of the flow in the larger pipe
        smaller_diameter: diameter of the smaller pipe in meters
    Return:
        lost pressure in kilopascals
    """
    k = (0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter)**4 - 1)
    pressure_loss = -k * WATER_DENSITY * fluid_velocity**2 / 2000
    return pressure_loss

def kpa_to_psi(pressure_kpa):
    """Convert pressure from kilopascals to pounds per square inch (psi).

    Parameters:
        pressure_kpa: pressure in kilopascals
    Return:
        pressure in pounds per square inch
    """
    return pressure_kpa * 0.14503773773

PVC_SCHED80_INNER_DIAMETER = 0.28687  # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013   # (unitless)
SUPPLY_VELOCITY = 1.65                # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692  # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018    # (unitless)
HOUSEHOLD_VELOCITY = 1.75             # (meters / second)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    pressure_psi = kpa_to_psi(pressure)
    
    print(f"Pressure at house: {pressure:.1f} kilopascals ({pressure_psi:.1f} psi)")

if __name__ == "__main__":
    main()
