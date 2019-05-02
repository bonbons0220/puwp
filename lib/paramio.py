
# coding: utf-8

# In[1]:

# ## Functions
# Functions for PUWP.


# In[2]:

import yaml
import io
import datetime
# import pyreadline


# In[11]:

def showmenu(menu):
    """Shows a menu and returns validated option or default"""

    # get option
    print('\n')  
    for k,v in menu.items():
        print( k + ' : ' + v )
    option = (raw_input('Choose an option: [X]\n') or 'X')
    
    # validate it
    if ( option in menu.keys() ) : 
        result = option
    else:
        print( '"' + option + '" is not on the menu. \n')
        result = 'X'

    return result


# In[12]:

def editparam(editable,data):
    """Shows current parameters"""
    
    print('\nParameters: \n')
    for k,v in sorted(data.items()):
        print( data[k]['label'] + ' : ' + data[k]['value'] )

    if (editable) :
        print('\nEnter a new value or [enter] to keep existing value.\n')
        for k,v in sorted(data.items()):
            data[k]['value'] = ( raw_input( data[k]['label'] + ' : [' + data[k]['value'] + '] ' ) or data[k]['value'] )
        print('\n')

        return data


# In[13]:

def readparam():
    """Read parameters from file."""
    
    # Get filename
    datafile = ( raw_input('Enter parameter filename [defaults.yaml]') or 'defaults.yaml' );
    
    # Read YAML file
    with io.open( datafile , 'r') as stream:
        try:
            data = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            
    return data


# In[14]:

def writeparam( data ):
    """Write] parameters from file."""
    
    # Get filename
    datafile = ( raw_input('Enter parameters filename [defaults.yaml]') or 'defaults.yaml' );
    
    # Write YAML file
    with io.open( datafile , 'w', encoding='utf8') as outfile:
        try:
            yaml.dump( data , outfile , default_flow_style=False, allow_unicode=True)
        except yaml.YAMLError as exc:
            print(exc)


# In[ ]:




# In[15]:

def writereport( report ):
    """Write report to file."""
    
    # Get filename
    datafile = ( input('Enter report filename [report.yaml]') or 'report.yaml' );
    
    # Write YAML file
    with io.open( datafile , 'w', encoding='utf8') as outfile:
        try:
            yaml.dump( data , outfile , default_flow_style=False, allow_unicode=True)
        except yaml.YAMLError as exc:
            print(exc)


# In[17]:

# These tests run when not called as a module
if __name__ == "__main__":
    # import sys
    
    # TEST DATA #
    d={
    '1targetdomain' : { 
        'label' : 'Target domain: ',
        'value' : 'www.example.org' } ,
    '2sourcedomain' : { 
        'label' : 'Source domain: ',
        'value'	: 'test.example.org' } ,
    '3targetpath'   : { 
        'label' : 'Target path: ',
        'value'	: '/var/www/example.org/prod' },
    '4sourcepath'   : { 
        'label' : 'Source path: ',
        'value'	: '/var/www/example.org/test' },
    '5deploypath'   : {	
        'label' : 'Deploy path: ',
        'value'	: '/var/www/example.org/deploy' },
    '6targetDB'     : { 
        'label' : 'Target database: ',
        'value'	: 'examplewp_prod ' },
    '7sourceDB'     : { 
        'label' : 'Source database: ',
        'value'	: 'examplewp_test' } 
    }

    m = {'R':'[R]ead input parameters',
           'E':'[E]dit input parameters',
           'W':'[W]rite input parameters',
           'X':'E[X]it'
    }
    
    #TEST THE MODULES
    print("\nInteractive Testing")
    print("The test parameters file is default.yaml.")

    print("\nVIEW PARAMETERS.")
    editparam( False, d )
    
    print("\nEDIT PARAMETERS. Change each value.")
    d = editparam( True, d )
    
    print("\nWRITE PARAMETERS. Validate and verify file contents.")
    writeparam( d )
    
    print("\nEDIT PARAMETERS. Change each value.")
    d = editparam( True , d )
    editparam( False, d )
    
    print("\nREAD PARAMETERS. Verify and validate loaded parameters.")
    d = readparam()
    editparam( False, d )
    
    
    print("\nSHOW MENU")
    print("Repeat tests by calling the functions with showmenu. ")
    showmenu(m)
    



# In[ ]:



