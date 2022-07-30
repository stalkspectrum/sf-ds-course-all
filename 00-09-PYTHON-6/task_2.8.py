#!/usr/bin/python3

#####=====----- VARIABLES -----=====#####

user_data = [
    (1, {'username': 'user1', 'age': 'age1', 'email': 'email1'}),
    (2, {'username': 'user2', 'age': 'age2', 'email': 'email2'}),
    (3, {'username': 'user3', 'age': 'age3', 'email': 'email3'}),
]


#####=====----- FUNCTIONS -----=====#####

def update_data(data_list=None):
    """ Asks for user data in a cycle.
        Enter an empty string to stop input and exit the cycle.
        Keyword Arguments:
            data_list -- List of tuples with user data (default: {None})
        Returns: Appended or zero-formed data_list
    """
    def accept_user():
        """ Asks user attributes.
            Returns: Completed dictionary for single user.
        """
        user_attribs = ['username', 'age', 'email']
        user_dict = {}
        for attrib in user_attribs:
            input_str = input(f'Enter {attrib}: ')
            if len(input_str) > 0:
                user_dict[attrib] = input_str
            else:
                return {}
        return user_dict
    
    if data_list is None:
        data_list = []
    need_input = True
    while need_input:
        next_user_num = len(data_list) + 1
        next_user = accept_user()
        if len(next_user) > 0:
            data_list.append((next_user_num, next_user))
        else:
            need_input = False
    return data_list


def reform_data(user_list):
    ''' Gathers user data into a dictionary new_dict by keys:
        'username', 'age', 'email'
        Arguments:
            user_list -- List of tuples with user data.
        Returns: Completed dictionary new_dict.
    '''
    new_dict = {
                 'username': [],
                 'age': [],
                 'email': []
                }
    for user_tup in user_list:
        for key in user_tup[1]:
            new_dict[key].append(user_tup[1][key])
    return new_dict


def output_new_data(data_dict):
    ''' Displays the resulting analytics.
        Arguments:
            data_dict -- Dictionary of user data gathered by keys.
    '''
    for key, value in data_dict.items():
        print(f'\n{key}: {value}')


#####=====----- MAIN -----=====#####

if __name__ == '__main__':
    output_new_data(reform_data(update_data(user_data)))

#####=====----- THE END -----=====#####