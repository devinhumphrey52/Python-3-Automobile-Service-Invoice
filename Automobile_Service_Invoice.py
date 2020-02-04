# Creates service option variables and associated price list 
print('Davy\'s auto shop services')

Oil_Change = 35
Tire_Rotation = 19
Car_Wash = 7
Car_Wax = 12
no_service = '-'

# Displays output of services and associated costs
print('Oil change -- $%d' % (Oil_Change))
print('Tire rotation -- $%d' % (Tire_Rotation))
print('Car wash -- $%d' % (Car_Wash))
print('Car wax -- $%d' % (Car_Wax))
print("")

# Allows User to input selected services
service_1 = str(input("Select first service: "))
print('\n')
service_2 = str(input("Select second service: \n"))
print('')
print('')
# Displays an Invoice to the Customer with previously selected services, associated costs, and re-assigns variables with ints
print("Davy\'s auto shop invoice\n")
if service_1 == 'Oil change':
    print("Service 1:", "%s, $%d" % (service_1, Oil_Change))
    service_1 = 35
if service_1 == 'Tire rotation':
    print("Service 1:", "%s, $%d" % (service_1, Tire_Rotation))
    service_1 = 19
if service_1 == 'Car wash':
    print("Service 1:", "%s, $%d" % (service_1, Car_Wash))
    service_1 = 7
if service_1 == 'Car wax':
    print("Service 1:", "%s, $%d" % (service_1, Car_Wax))
    service_1 = 12
if service_1 == '-':
    print("Service 1: No service")
    service_1 = 0
    
if service_2 == 'Oil change':
    print("Service 2:", "%s, $%d\n" % (service_2, Oil_Change))
    service_2 = 35
if service_2 == 'Tire rotation':
    print("Service 2:", "%s, $%d\n" % (service_2, Tire_Rotation))
    service_2 = 19
if service_2 == 'Car wash':
    print("Service 2:", "%s, $%d\n" % (service_2, Car_Wash))
    service_2 = 7
if service_2 == 'Car wax':
    print("Service 2:", "%s, $%d\n" % (service_2, Car_Wax))
    service_2 = 12
if service_2 == '-':
    print("Service 2: No service\n")
    service_2 = 0

# Prints total based on user service selections
total_services = service_1 + service_2
print('Total: $%d' % (total_services))
