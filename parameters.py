#parameters
#Default Parameters
def greeting (name = 'Investor', service = 'Tips'):
    print(f'Hello {name}, you are here for {service}')
#'Investor' and 'Tips' will be the default arguments if either a name or service are nt input

#positional parameters - are in the order of definition of parameters
greeting('Comma','Weekly Brief')
greeting('Sam','Monthly Statement')
greeting('Chief','Investor Outlook')
greeting() #Will return the default parameter

#keyword parameters - are dynamic, don't need t follow the order defined
greeting(service='CEO Letters',name='John')