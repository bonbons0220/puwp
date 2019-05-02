
# coding: utf-8

# ## Functions
# Functions for PUWP.

import yaml
import io
import datetime
import pyreadline

def showmenu(menu):
    """Shows a menu and returns validated option or default"""

    # get option
    print('\n')  
    for k,v in menu.items():
        print( k + ' : ' + v )
    option = (raw_input('Choose an option: [E]\n') or 'E')
    
    # validate it
    if ( option in menu.keys() ) : 
        result = option
    else:
        print( '"' + option + '" is not on the menu. \n')
        result = 'R'

    return result


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
