
# coding: utf-8

# # setup-param.ipynb
# Set up parameters for pushing Wordpress. 

# ## Overview
# This notebook reads and writes an input parameter file to run push-wordpress.ipynb.

# In[1]:

import yaml
import io
import datetime


# 
# ## Functions

# In[2]:

def showmenu(menu):
    """Shows a menu and returns validated option or default"""

    # get option
    print('\n')  
    for k,v in menu.items():
        print( k + ' : ' + v )
    option = (input('Choose an option: [E]\n') or 'E')
    
    # validate it
    if ( option in menu.keys() ) : 
        result = option
    else:
        print( '"' + option + '" is not on the menu. \n')
        result = 'R'

    return result


# In[3]:

def editparam(editable):
    """Shows current parameters"""
    
    print('\nParameters: \n')
    for k,v in sorted(data.items()):
        print( data[k]['label'] + ' : ' + data[k]['value'] )

    if (editable) :
        print('\nEnter a new value or [enter] to keep existing value.\n')
        for k,v in sorted(data.items()):
            data[k]['value'] = ( input( data[k]['label'] + ' : [' + data[k]['value'] + '] ' ) or data[k]['value'] )
        print('\n')

        return data


# In[4]:

def readparam():
    """Read parameters from file."""
    
    # Get filename
    datafile = ( input('Enter parameter filename [defaults.yaml]') or 'defaults.yaml' );
    
    # Read YAML file
    with io.open( datafile , 'r') as stream:
        try:
            data = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            
    return data


# In[5]:

def writeparam( data ):
    """Write] parameters from file."""
    
    # Get filename
    datafile = ( input('Enter parameters filename [defaults.yaml]') or 'defaults.yaml' );
    
    # Write YAML file
    with io.open( datafile , 'w', encoding='utf8') as outfile:
        try:
            yaml.dump( data , outfile , default_flow_style=False, allow_unicode=True)
        except yaml.YAMLError as exc:
            print(exc)


# ## Data

# In[6]:

data={
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

menu = {'R':'[Read input parameters]',
       'E':'[E]dit input parameters',
       'W':'[W]rite input parameters',
       'X':'E[X]it'}



# ## Main

# In[7]:

# main loop
while (True):

    # show parameters
    editparam(False)
    
    # show menu
    option = showmenu(menu)
    
    if (option) == 'R' : 
        data = readparam()

    if (option) == 'W' : 
        writeparam( data )
        
    if (option) == 'E' : 
        data = editparam(True)
        
    if (option) == 'X': break
    


# In[ ]:




# In[ ]:



