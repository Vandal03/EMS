import configparser

config = configparser.ConfigParser()

config.add_section('paths')
config.set('paths', 'gdpath', '')

config.add_section('selected')
config.set('selected', 'store', '')

config.add_section("absent_types")
config.set('absent_types', "ncns", "No Call, No Show")
config.set('absent_types', "lt", "Late")
config.set('absent_types', "co", "Called Off")

config.add_section('stores')
config.set('stores', 'Lagro', 'Lagro')
config.set('stores', 'Hoosier_Point', 'Hoosier Point')
config.set('stores', 'South_Whitley', 'South Whitley')
config.set('stores', 'Silver_Lake', 'Silver Lake')
config.set('stores', 'Fast_Mart', 'Fast Mart')


with open(r"/Users/avanderpool/Documents/Programming/EMS/configfile.ini", 'w') as configfile:
    config.write(configfile)