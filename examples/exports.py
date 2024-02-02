import os
import sys
import json
import time
sys.path.append("../")
from letterboxdpy import user

username = ''

if not len(username):
    try:
        username = sys.argv[1]
    except IndexError:
        print(f'Quick usage: python {sys.argv[0]} <username>')
        username = input('Enter username: ')

nick = user.User(username.lower())

methods = [
    user.user_films,
    user.user_following,
    user.user_followers,
    user.user_genre_info,
    user.user_reviews,
    user.user_diary,
    user.user_wrapped,
    user.user_activity,
]

EXPORTS_DIR = 'exports'
USERS_FOLDER = os.path.join(EXPORTS_DIR, 'users')
USER_FOLDER = os.path.join(USERS_FOLDER, nick.username)


print('\nChecking directories...')
for dir in [EXPORTS_DIR, USERS_FOLDER, USER_FOLDER]:
    if not os.path.exists(dir):
        print(f'\tCreating {dir}')
        os.mkdir(dir)
    else:
        print(f'\tFound {dir}')
else:
    print('All directories checked, continuing...', end='\n\n')

total_time = time.time()
for no, method in enumerate(methods, 1):
    os.system(f'title Exporting {method.__name__}... ({no}/{len(methods)})')
    print(f'[{no}/{len(methods)}]: Processing "{method.__name__}" method...', end='\r')
    method_start_time = time.time()
    data = method(nick)
    file_path = os.path.join(USER_FOLDER, f'{method.__name__}.json')

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

    click_url = 'file:///' + os.path.join(os.getcwd(), file_path).replace("\\", "/").replace("Aade", "?")
    print(f'{time.time() - method_start_time:<7.2f} seconds - {method.__name__:<16} - {click_url}')

os.system('title Completed!')
print('\nProcessing complete!')
print(f'\tTotal time: {time.time() - total_time:.2f} seconds')
click_url = 'file:///' + os.path.join(os.getcwd(), USER_FOLDER).replace("\\", "/").replace("Aade", "?")
print('\tAt', click_url, end='\n\n')
os.system('pause')