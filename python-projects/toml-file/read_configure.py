import toml

# Load the TOML file into a dictionary

with open('configure.toml', 'r') as f:
    config = toml.load(f)

# Print out values from the TOML dictionary

print('title is:\t\t', config['title'])
print('ports are:\t\t', config['database']['ports'])
print('servers alpha role is:\t', config['servers']['alpha']['role'])
