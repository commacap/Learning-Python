#parameters
name = input('What is your name? ')
service = input('How would you like to be assisted today? ')

def greeting (name, service):
    print(f'Hello {name}, you are here for {service}')

greeting(name, service)