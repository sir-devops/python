import os

# Get all environment variable names
env_vars = os.environ.keys()

# Print each environment variable name and value
for var_name in env_vars:
    var_value = os.getenv(var_name)
    print(var_name + ": " + var_value)
