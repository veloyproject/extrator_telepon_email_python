import pyperclip, re

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # kode area
    (\s|-|\.)?                      # separator
    (\d{4})                         # mencari 3 digit pertama
    (\s|-|\.)                       # separator
    (\d{4})                         # mencari 4 digit terakhir
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # ekstensi
    )''', re.VERBOSE)

# Membuat regex untuk pencarian email.
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # pola username
    @                               # symbol @
    [a-zA-Z0-9.-]+                  # pola nama domain
    (\.[a-zA-Z]{2,4})               # pola ekstensi domain
    )''', re.VERBOSE)


# Mencari dan menemukan teks clipboard.
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        groups += ' x' + groups[8]
    matches.append(phone_num)

for groups in email_regex.findall(text):
    matches.append(groups[0])

# Menyalin hasil ke clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found!')

